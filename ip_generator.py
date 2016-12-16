import numpy as np
import math
import ipcalc


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
        init = "10.10"
        for a in range(256):
            for i in range(256):
                ip_addres = init+"."+str(a)+"."+str(i)
                ip_table.append(ip_addres)
    if prefix == 22:
        for x in range(64):
            ip_blocks = "10."+str(x)+".4/22"
            for ip in ipcalc.Network(ip_blocks):
                ip_table.append(str(ip))
    if prefix == 20:
        for x in range(16):
            ip_blocks = "10."+str(x)+".16/20"
            for ip in ipcalc.Network(ip_blocks):
                ip_table.append(str(ip))
        # for ip in ipcalc.Network("10.10.16/20"):
        #     print ip
    if prefix == 18:
        for x in range(4):
            ip_blocks = "10."+str(x)+".32/18"
            for ip in ipcalc.Network(ip_blocks):
                ip_table.append(str(ip))
    if prefix == 16:
        for ip in ipcalc.Network("10.10/16"):
            ip_table.append(str(ip))
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
    # read_ip_table()
    read_formal_ip_table(18)
