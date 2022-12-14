import psutil


def my_ip():
    my_dict = (psutil.net_if_addrs())
    for key in my_dict:
        if key.startswith("Ethernet"):
            return my_dict[key][1][1], my_dict[key][1][2], my_dict[key][0][1]


print('IP {}, mask {}, mac {}'.format(my_ip()[0], my_ip()[1], my_ip()[2]))
