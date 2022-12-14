import psutil
from netaddr import IPNetwork
import ipaddress
from ping3 import ping
from scanport_params import ports, report_file
import socket
import datetime

"""Находим наши данные"""


def my_ip():
    my_dict = (psutil.net_if_addrs())
    for key in my_dict:
        if key.startswith("Ethernet"):
            return my_dict[key][1][1], my_dict[key][1][2], my_dict[key][0][1]


"""Пишем данные, формируем адрес сети для последующей работы"""

print('IP: {} Mask: {} MAC: {}'.format(my_ip()[0], my_ip()[1], my_ip()[2]))
IP_m = str(my_ip()[0])
Mask_m = str(my_ip()[1])
ip_eth = (str(IPNetwork(f'{IP_m}/{Mask_m}').cidr))

"""Наследуем процедуру проверки портов"""


def scan_port(ip_add, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    now = datetime.datetime.now()
    current_time = now.strftime("%Y %b %d %A %H:%M:%S ")
    try:
        with open(report_file, 'a+') as file:
            sock.connect((ip_add, port))
            print(current_time, ('-' * 10), 'IP :', ip_add, 'Port :', port, ' its open', 'Protocol :',
                  ports[port], ('-' * 10))
            file.write('{0} IP: {1}, Port: {2}, Protocol: {3}\n'.format(current_time, ip_add, port, ports[port]))
            sock.close()
    except:
        print(current_time, 'its block', port, ports[port])
        pass


"""Проверяем сеть по адресу, последовательно проверяя каждый узел. При успехе проверяем порты, пишем отчет.
Узнаем время проверки всего пула."""


def run_poc():
    time_start = datetime.datetime.now()
    for result in ipaddress.IPv4Network(ip_eth):
        result = str(result)
        ping(result, timeout=1)
        if ping(result):
            print(('-' * 10), "{} - успех".format(result))
            for i in ports:
                scan_port(result, i)
        else:
            print("{} - провал".format(result))
    time_stop = datetime.datetime.now()
    print('Потрачено времени на проверку: {}'.format(time_stop - time_start))
    with open(report_file, 'a+') as file:
        file.write('Потрачено времени на проверку: {}\n'.format(time_stop - time_start))
        file.close()


run_poc()
