import psutil


def my_ip():
    my_dict = (psutil.net_if_addrs())
    for key in my_dict:
        if key.startswith("Ethernet"):
            print("found {} : {}".format(key, my_dict[key][1][1]))


