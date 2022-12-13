import socket
import datetime
import os
import sys

from scanport_params import report_file, ports

"""Основная процедура, проверяет и пишет"""


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


"""Контроль лога. Если пустой, то удаляем. Оставляем только с результатом."""


def null_files():
    is_empty = os.stat(report_file).st_size == 0
    if is_empty is True:
        os.remove(report_file)
    else:
        pass


"""Получаем данные хоста, перебираем словарь. В случае если ничего не ввели подменяем значение на localhost"""


def run_poc():
    print('Внимание! Некоторые антивирусы могут посчитать это ПО вредоносным. ')
    resp_ed = input('Введи "Да" и нажмите Enter, если хотите продолжить.\nЛюбой другой символ чтобы завершить работу: ')
    if resp_ed.lower() == 'да':
        ip_add = input('Введите IP хоста для сканирования: ')
        if ip_add:
            for i in ports:
                scan_port(ip_add, i)
        else:
            ip_add = 'localhost'
            for i in ports:
                scan_port(ip_add, i)
    else:
        print('Работа прервана пользователем.')
        sys.exit(0)
    null_files()


run_poc()
