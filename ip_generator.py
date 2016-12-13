import numpy as np
import math


def ip_generator(total_num):
    init = "10.10.10"
    ip_table = []
    i = 0
    l = 0
    if not init == "":
        arr = init.split(".")
        l = len(arr)
    while (i < total_num):
        end = ""
        for a in range(4-l):
            end += "."+str(np.random.randint(0, 256))
        ip_addres = init + end
        if ip_addres not in ip_table:
            ip_table.append(ip_addres)
            i += 1
    return ip_table


def dataCenter_ip_generator(total_num, block_num):
    init = "10.10"
    ip_table = []
    blocks = np.random.dirichlet(np.ones(block_num), size=1)
    block_ids = []
    for i in blocks[0]:
        # print i
        id = np.random.randint(0, 256)
        while id in block_ids:
            id = np.random.randint(0, 256)
        block_ids.append(id)
        block_id = "."+str(id)
        a = 0
        while a < int(i*total_num):
            ip_addres = init+block_id+"."+str(np.random.randint(0, 256))
            # print ip_addres
            if ip_addres not in ip_table:
                ip_table.append(ip_addres)
                a += 1
        # for a in range(int(i*total_num)):
        #     ip_addres = init+block_id+"."+str(np.random.randint(0, 256))
        #     # print ip_addres
        #     if ip_addres not in ip_table:
        #         ip_table.append(ip_addres)
    return ip_table


def read_formal_ip_table(prefix):
    # https://www.ripe.net/about-us/press-centre/understanding-ip-addressing
    ip_table = []
    if prefix == 24:
        init = "10.10.10"
        for i in range(256):
            ip_addres = init+"."+str(i)
            ip_table.append(ip_addres)
    if prefix == 22:
        init = "10.10.252"
        for i in range(105):
            ip_addres = init+"."+str(i)
            ip_table.append(ip_addres)
        init = "10.10.253"
        for i in range(51):
            ip_addres = init+"."+str(i)
            ip_table.append(ip_addres)
        init = "10.10.254"
        for i in range(50):
            ip_addres = init+"."+str(i)
            ip_table.append(ip_addres)
        init = "10.10.255"
        for i in range(50):
            ip_addres = init+"."+str(i)
            ip_table.append(ip_addres)
    if prefix == 20:
        init = "10.10.240"
        for i in range(105):
            ip_addres = init+"."+str(i)
            ip_table.append(ip_addres)
        init = "10.10.243"
        for i in range(51):
            ip_addres = init+"."+str(i)
            ip_table.append(ip_addres)
        init = "10.10.254"
        for i in range(50):
            ip_addres = init+"."+str(i)
            ip_table.append(ip_addres)
        init = "10.10.255"
        for i in range(50):
            ip_addres = init+"."+str(i)
            ip_table.append(ip_addres)
    if prefix == 18:
        init = "10.10.192"
        for i in range(105):
            ip_addres = init+"."+str(i)
            ip_table.append(ip_addres)
        init = "10.10.200"
        for i in range(51):
            ip_addres = init+"."+str(i)
            ip_table.append(ip_addres)
        init = "10.10.210"
        for i in range(50):
            ip_addres = init+"."+str(i)
            ip_table.append(ip_addres)
        init = "10.10.245"
        for i in range(50):
            ip_addres = init+"."+str(i)
            ip_table.append(ip_addres)
    if prefix == 16:
        init = "10.10.0"
        for i in range(105):
            ip_addres = init+"."+str(i)
            ip_table.append(ip_addres)
        init = "10.10.10"
        for i in range(51):
            ip_addres = init+"."+str(i)
            ip_table.append(ip_addres)
        init = "10.10.101"
        for i in range(50):
            ip_addres = init+"."+str(i)
            ip_table.append(ip_addres)
        init = "10.10.225"
        for i in range(50):
            ip_addres = init+"."+str(i)
            ip_table.append(ip_addres)
    return ip_table

def read_ip_table():
    f = open('IPs.txt')
    ip_table = []
    for ip in iter(f):
        ip_table.append(ip.replace('\n', ''))
    return ip_table

if __name__ == "__main__":
    # ip_generator(10)
    # dataCenter_ip_generator(10, 2)
    read_ip_table()
