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
    d = d ^ key * 16777619 & 0xffffffff
    return d
    # return math.pow(d, key)


def CreateMinimalPerfectHash(dict):
    size = len(dict)
    buckets = [[] for i in range(size)]
    G = [0] * size
    values = [None] * size
    for key in dict.keys():
        buckets[dict[key] % size].append(key)
    buckets.sort(key=len, reverse=True)
    for b in xrange(size):
        bucket = buckets[b]
        if len(bucket) > 1:
            item = 0
            slots = []
            # print "bucket: ", +b
            d = 1
            while(item < len(bucket)):
                if dict[bucket[item]] == 0:
                    slot = size-1
                    slots.append(slot)
                    item += 1
                else:
                    slot = int(hash(dict[bucket[item]], d) % size)
                    if values[slot] != None or slot in slots:
                        print "wrong hash"
                        item = 0
                        slots = []
                        d += 1
                    else:
                        slots.append(slot)
                        item += 1
            # print slots
            G[dict[bucket[0]] % size] = d
            for i in range(len(bucket)):
                values[slots[i]] = dict[bucket[i]]

    # Process patterns with one key and use a negative value of d
    freelist = []
    for i in xrange(size):
        if values[i] is None:
            freelist.append(i)
    for b in xrange(size):
        bucket = buckets[b]
        if len(bucket) == 1:
            slot = freelist.pop()
            G[dict[bucket[0]] % size] = -slot-1
            values[slot] = dict[bucket[0]]
    return values


if __name__ == "__main__":
    ip_table = ip_generator.read_ip_table()
    # ip_table = ip_generator.ip_generator(100)
    int_ip_table, ip_map = encode_IP(ip_table)
    min_key = min(int_ip_table)
    ip_opt = dict()
    for key, value in ip_map.iteritems():
        ip_opt[key] = value - min_key
    hash_table = CreateMinimalPerfectHash(ip_opt)
    # print hash_table
    for index in range(len(hash_table)):
        hash_value = hash_table[index]
        the_ip = int_to_ip(min_key+hash_value)
        print the_ip, "->", hash_value, "->", index
