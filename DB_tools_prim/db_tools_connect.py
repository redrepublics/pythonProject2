import os
import os.path
import sys

import pyodbc
import time
from db_tools_params import *
from db_tools_request import req_1, req_2, req_3, req_5, req_6, req_7, req_8, req_9, req_10
from db_tools_request import Request5


def sql_return():
    try:
        conn = pyodbc.connect(
            'DRIVER={' + get_folder()[1] + '};SERVER=' + get_folder()[2] + ';DATABASE=' + get_folder()[3] + ';UID=' +
            get_folder()[4] + ';PWD=' + get_folder()[5] + ';', autocommit=True)
    except pyodbc.Error as err:
        with open(os.path.join(get_folder()[0], f'{TODAY}_pyodbc.txt'), 'w+') as file_error:
            file_error.write(f"line:12 (db_tools_connect) Сервер не запущен, или неправильно указаны параметры "
                             f"подключения\n{err}")
            file_error.close()
    else:
        return conn


def bak_search():
    path = os.path.join(get_folder()[0], f'SRW_688-{pars_files_bak[-1]}')
    if os.path.isfile(path) is True:
        return True
    else:
        return False


def del_tables():
    cursor = sql_return().cursor()
    cursor.execute(req_1)
    cursor.execute(req_2)
    cursor.execute(req_3)
    cursor.execute(req_5)
    cursor.execute(req_6)
    cursor.execute(req_7)
    cursor.execute(req_8)
    cursor.execute(req_9)
    cursor.execute(req_10)
    print('Очистка таблиц закончена.')


def sh_sql():
    cursor = sql_return().cursor()
    cursor.execute(Request5)
    time.sleep(1)
    for row in cursor:
        print('row = %r' % (row,))


def request_log():
    re_log = 'rs.sql'
    cursor = sql_return().cursor()
    with open(re_log, 'r', encoding='utf-8') as re_log_file:
        cursor.execute(re_log_file.read())


def start_password():
    n = 0
    n_max = 3
    password_db = int(17110367)
    while True:
        print(f'Попытка № {n} из {n_max}')
        try:
            pp = int(input('Введите цифровой пароль:'))
        except ValueError as err:
            with open(os.path.join(get_folder()[0], f'{TODAY}_ValueError.txt'), 'w+') as file_error:
                file_error.write(f"line:70 (db.tools) Некорректный ввод пароля\n{err}")
                file_error.close()
                n = n + 1
                if n == n_max:
                    print('Вы превысили количество попыток.')
                    with open(os.path.join(get_folder()[0], f'{TODAY}_PassError.txt'), 'w+') as file_error_pass:
                        print('Вы превысили количество попыток.')
                        file_error_pass.write("Исчерпаны попытки ввода пароля.")
                        file_error_pass.close()
                    sys.exit(0)
                else:
                    continue
        else:
            if pp == password_db:
                print('Пароль корректный.')
                break
            elif n < n_max and pp != password_db:
                n = n + 1
                print('Неправильный ввод. Осталось попыток', n_max - n)
                continue
            else:
                print('Что-то пошло не так.')
