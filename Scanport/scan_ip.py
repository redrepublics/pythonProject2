import psutil


def my_ip():
    my_dict = (psutil.net_if_addrs()['Ethernet'])
    result = my_dict[1]
    return result[1]
