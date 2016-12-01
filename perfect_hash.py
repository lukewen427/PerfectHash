import ip_generator
import math
import numpy as np
from scipy.sparse import csr_matrix
import operator

def ip_to_int(s):
    # the rule can be found here: http://www.aboutmyip.com/AboutMyXApp/IP2Integer.jsp
    return reduce(lambda a, b: a << 8 | b, map(int, s.split(".")))


def int_to_ip(num):
    return ".".join(map(lambda n: str(num >> n & 0xFF), [24, 16, 8, 0]))


def encode_IP(ip_table):
    int_ips = [ip_to_int(ip) for ip in ip_table]
    return int_ips


def sort_row(array):
    dict_row = dict()
    for i in range(len(array)):
        temp = np.nonzero(array[i])
        dict_row[i] = len(temp[0])
    sorted_array = sorted(
        dict_row.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_array


def shift_row(sorted_array, array):
    row = dict()
    block_array = np.zeros([10000], dtype=np.int)
    print block_array

    # print sorted_array
    for single_row in sorted_array:
        count = 0
        row_id = single_row[0]
        h = np.nonzero(block_array)
        row_data = array[row_id]
        if len(h[0]) == 0:
            row[row_id] = 0
            no_zero = np.nonzero(row_data)
            for col_id in no_zero[0]:
                block_array[col_id] = 1
        else:
            no_zero = np.nonzero(row_data)
            array_no_zero = h[0]
            isFound = False
            while(isFound is False):
                if count in array_no_zero:
                    count += 1
                else:
                    no_zero = np.nonzero(row_data)
                    temp = no_zero[0]
                    if len(temp) > 0:
                        # header = temp[0]
                        isExe = True
                        for col_id in temp:
                            if block_array[count + col_id] > 0:
                                isExe = False
                                break
                        if isExe is True:
                            isFound = True
                            for col_id in temp:
                                block_array[count + col_id] = 1
                            row[row_id] = count
                        count += 1
                    else:
                        break
    # print np.nonzero(block_array)
    return row


def simpe_perfect_hash():
    int_ip_table = encode_IP(ip_table)
    min_key = min(int_ip_table)
    max_key = max(int_ip_table)
    t = int(math.sqrt(max_key-min_key))+1
    array = csr_matrix((t, t), dtype=np.int).toarray()
    index_table = []
    for key in int_ip_table:
        ab_key = (key-min_key)
        x = ab_key/t
        y = ab_key % t
        array[x][y] = ab_key
    sorted_array = sort_row(array)
    row = shift_row(sorted_array, array)
    # print row
    for key in int_ip_table:
        ab_key = (key-min_key)
        x = ab_key/t
        y = ab_key % t
        index = row[x]+y
        index_table.append(index)
        the_ip = int_to_ip(key)
        # print the_ip, "->", key, "->", index
    # print int_ip_table
    print sorted(index_table)


if __name__ == "__main__":
    ip_table = ip_generator.ip_generator(100)
    simpe_perfect_hash()
