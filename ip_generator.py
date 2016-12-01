import numpy as np, numpy.random

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
    blocks = np.random.dirichlet(np.ones(block_num),size=1)
    for i in range (block_num):
        print i
        block_id = "."+str(np.random.randint(0, 256))
        for a in range(int(i*total_num)):
            ip_addres = init+block_id+"."+str(np.random.randint(0, 256))
            print ip_addres
            if ip_addres not in ip_table:
                ip_table.append(ip_addres)
    return ip_table

if __name__ == "__main__":
    # ip_generator(10)
    dataCenter_ip_generator(10, 1)
