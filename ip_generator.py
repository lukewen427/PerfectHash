import random

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
            end += "."+str(random.randint(0, 256))
        ip_addres = init + end
        if ip_addres not in ip_table:
            ip_table.append(ip_addres)
            i += 1
    return ip_table

if __name__ == "__main__":
    ip_generator(10)
