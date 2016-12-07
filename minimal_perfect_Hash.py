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


def hash_one(key):
    return key % gap

def CreateMinimalPerfectHash(dict):
    size = len(dict)
    buckets = [[] for i in range(size)]
    G = [0] * size
    values = [None] * size
    for key in dict.keys():
        buckets[hash(dict[key]) % size].append(key)
    buckets.sort(key=len, reverse=True)
    # bucket = buckets[0]
    # print hash_one(dict[bucket[0]])
    # print dict[bucket[0]]
    # print hash_one(dict[bucket[1]])
    # print dict[bucket[1]]
    # print gap
    for b in xrange(1):
        bucket = buckets[b]
        if len(bucket) <= 1:
            break
        d = 1
        item = 0
        slots = []
        print hash_one(dict[bucket[0]])
        print hash_one(dict[bucket[1]])
        print size
        print hash_one(dict[bucket[0]]) % size
        print hash_one(dict[bucket[1]]) % size
        # while item < len(bucket):
        #     slot = hash_one(dict[bucket[item]]) % size
        #     print slot
        #     print slots, item
        #     if values[slot] != None or slot in slots:
        #         d += 1
        #         item = 0
        #         slots = []
        #     else:
        #         slots.append(slot)
        #         item += 1
        # print slots
        # G[dict(bucket[0]) % size] = d
        # for i in range(len(bucket)):
        #     values[slots[i]] = dict[bucket[i]]
        #
        # if ( b % 1000 ) == 0:
        #     print "bucket %d    r" % (b),
        #     sys.stdout.flush()

if __name__ == "__main__":
    ip_table = ip_generator.ip_generator(100)
    int_ip_table, ip_map = encode_IP(ip_table)
    min_key = min(int_ip_table)
    max_key = max(int_ip_table)
    gap = max_key - min_key
    ip_opt = dict()
    for key, value in ip_map.iteritems():
        ip_opt[key] = value - min_key
    CreateMinimalPerfectHash(ip_opt)
