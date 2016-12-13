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
    ip_map = dict()
    int_ips = []
    for ip in ip_table:
        num_ip = ip_to_int(ip)
        int_ips.append(num_ip)
        ip_map[ip] = num_ip
    return int_ips, ip_map


def hash(key, d):
    # print math.pow(key, d)
    if d == 0:
        # d = 0x811C9DC5
        return key
    d = (key * d + d) % 16777619
    # d = d ^ (key) * 16777619 & 0xffffffff
    # if d == 0:
    #     d = 0x811C9DC5
    # d = d ^ key * 2654435761
    # print d
    return d
    # return math.pow(d, key)


def CreateMinimalPerfectHash(dict):
    size = len(dict)
    buckets = [[] for i in range(size)]
    values = [None] * size
    for key in dict.keys():
        buckets[hash(dict[key], 0) % size].append(key)
    buckets.sort(key=len, reverse=True)
    for b in xrange(size):
        # print "bucket_num ", b
        bucket = buckets[b]
        # print bucket
        # for ip in bucket:
        #     print dict[ip]
        if len(bucket) == 1:
            break
        if len(bucket) >= 1:
            item = 0
            slots = []
            print "bucket: ", +b
            d = 1
            while(item < len(bucket)):
                slot = int(hash(dict[bucket[item]], d) % size)
                if values[slot] != None or slot in slots:
                    # print "wrong hash"
                    item = 0
                    slots = []
                    d += 1
                else:
                    slots.append(slot)
                    item += 1
            G[hash(dict[bucket[0]], 0) % size] = d
            for i in range(len(bucket)):
                values[slots[i]] = dict[bucket[i]]
    # # Process patterns with one key and use a negative value of d
    freelist = []
    for i in xrange(size):
        if values[i] is None:
            freelist.append(i)
    for b in xrange(b, size):
        bucket = buckets[b]
        if len(bucket) == 1:
            ind = hash(dict[bucket[0]], 0) % size
            if values[ind] is None:
                values[ind] = dict[bucket[0]]
                freelist.remove(ind)
            else:
                slot = freelist.pop()
                G[hash(dict[bucket[0]], 0) % size] = -slot-1
                values[slot] = dict[bucket[0]]
    return values


if __name__ == "__main__":
    # ip_table = ip_generator.read_ip_table()
    # ip_table = ip_generator.ip_generator(100)
    ip_table = ip_generator.read_formal_ip_table(16)
    int_ip_table, ip_map = encode_IP(ip_table)
    min_key = min(int_ip_table)
    ip_opt = dict()
    G = dict()
    for key, value in ip_map.iteritems():
        ip_opt[key] = value - min_key
    hash_table = CreateMinimalPerfectHash(ip_opt)
    print "offset_table", len(G)
    # for index in range(len(hash_table)):
    #     hash_value = hash_table[index]
    #     the_ip = int_to_ip(min_key+hash_value)
    #     print the_ip, "->", hash_value, "->", index
    # print "total_ip: ", len(ip_table)
