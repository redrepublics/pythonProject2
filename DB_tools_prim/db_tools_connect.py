import os
import os.path
import sys
import pyodbc
import time
from db_tools_params import *
from db_tools_request import req_1, req_2, req_3, req_5, req_6, req_7, req_8, req_9, req_10, req_11, req_12, req_13
from db_tools_request import req_14, req_15, req_16, req_17, req_18, req_19, req_20, req_21, req_22, req_23, req_24, req_25
from db_tools_request import Request5
from exam_del import *


def sql_return():
    try:
        conn = pyodbc.connect(
            'DRIVER={' + get_folder()[1] + '};SERVER=' + get_folder()[2] + ';DATABASE=' + get_folder()[3] + ';UID=' +
            get_folder()[4] + ';PWD=' + get_folder()[5] + ';', autocommit=True)
    except pyodbc.Error as err:
        with open(os.path.join(get_folder()[0], f'{TODAY}_pyodbc.txt'), 'w+') as file_error:
            file_error.write(f"{datetime_res()} line:14 (db_tools_connect) Сервер не запущен, или неправильно указаны "
                             f"параметры "
                             f"подключения\n{err}")
            file_error.close()
    else:
        return conn


def bak_search():
    path = os.path.join(get_folder()[0], f'{get_folder()[3]}-{pars_files_bak[-1]}')
    if os.path.isfile(path) is True:
        return True
    else:
        return False


def del_exams():
    cursor = sql_return().cursor()
    cursor.execute(del_exam)
    time.sleep(1)
    cursor.execute('select count(*) from tExaminations')
    for row in cursor:
        print('Измерений = %r' % (row,))


def del_tables():
    cursor = sql_return().cursor()
    with open(os.path.join(get_folder()[0], f'{TODAY}_db_tools_no_table.txt'), 'w+') as file_error:
        try:
            cursor.execute(req_1)
        except pyodbc.ProgrammingError as file:
            file_error.write('Старая версия АСПО. Таблица отсутствует. \n')
            file_error.write(str(file))
            pass
        try:
            cursor.execute(req_2)
        except pyodbc.ProgrammingError as file:
            file_error.write('Старая версия АСПО. Таблица отсутствует. \n')
            file_error.write(str(file))
            pass
        try:
            cursor.execute(req_3)
        except pyodbc.ProgrammingError as file:
            file_error.write('Старая версия АСПО. Таблица отсутствует. \n')
            file_error.write(str(file))
            pass
        try:
            cursor.execute(req_5)
        except pyodbc.ProgrammingError as file:
            file_error.write('Старая версия АСПО. Таблица отсутствует. \n')
            file_error.write(str(file))
            pass
        try:
            cursor.execute(req_6)
        except pyodbc.ProgrammingError as file:
            file_error.write('Старая версия АСПО. Таблица отсутствует. \n')
            file_error.write(str(file))
            pass
        try:
            cursor.execute(req_7)
        except pyodbc.ProgrammingError as file:
            file_error.write('Старая версия АСПО. Таблица отсутствует. \n')
            file_error.write(str(file))
            pass
        try:
            cursor.execute(req_8)
        except pyodbc.ProgrammingError as file:
            file_error.write('Старая версия АСПО. Таблица отсутствует. \n')
            file_error.write(str(file))
            pass
        try:
            cursor.execute(req_9)
        except pyodbc.ProgrammingError as file:
            file_error.write('Старая версия АСПО. Таблица отсутствует. \n')
            file_error.write(str(file))
            pass
        try:
            cursor.execute(req_10)
        except pyodbc.ProgrammingError as file:
            file_error.write('Старая версия АСПО. Таблица отсутствует. \n')
            file_error.write(str(file))
            pass
        try:
            del_exams()
        except pyodbc.ProgrammingError as file:
            file_error.write('Старая версия АСПО. Таблица отсутствует. \n')
            file_error.write(str(file))
            pass
        try:
            cursor.execute(req_11)
        except pyodbc.ProgrammingError as file:
            file_error.write('Старая версия АСПО. Таблица отсутствует. \n')
            file_error.write(str(file))
            pass
        try:
            cursor.execute(req_12)
        except pyodbc.ProgrammingError as file:
            file_error.write('Старая версия АСПО. Таблица отсутствует. \n')
            file_error.write(str(file))
            pass
        try:
            cursor.execute(req_13)
        except pyodbc.ProgrammingError as file:
            file_error.write('Старая версия АСПО. Таблица отсутствует. \n')
            file_error.write(str(file))
            pass
        try:
            cursor.execute(req_14)
        except pyodbc.ProgrammingError as file:
            file_error.write('Старая версия АСПО. Таблица отсутствует. \n')
            file_error.write(str(file))
            pass
        try:
            cursor.execute(req_15)
        except pyodbc.ProgrammingError as file:
            file_error.write('Старая версия АСПО. Таблица отсутствует. \n')
            file_error.write(str(file))
            pass
        try:
            cursor.execute(req_16)
        except pyodbc.ProgrammingError as file:
            file_error.write('Старая версия АСПО. Таблица отсутствует. \n')
            file_error.write(str(file))
            pass
        try:
            cursor.execute(req_17)
        except pyodbc.ProgrammingError as file:
            file_error.write('Старая версия АСПО. Таблица отсутствует. \n')
            file_error.write(str(file))
            pass
        try:
            cursor.execute(req_18)
        except pyodbc.ProgrammingError as file:
            file_error.write('Старая версия АСПО. Таблица отсутствует. \n')
            file_error.write(str(file))
            pass
        try:
            cursor.execute(req_19)
        except pyodbc.ProgrammingError as file:
            file_error.write('Старая версия АСПО. Таблица отсутствует. \n')
            file_error.write(str(file))
            pass
        try:
            cursor.execute(req_20)
        except pyodbc.ProgrammingError as file:
            file_error.write('Старая версия АСПО. Таблица отсутствует. \n')
            file_error.write(str(file))
            pass
        try:
            cursor.execute(req_21)
        except pyodbc.ProgrammingError as file:
            file_error.write('Старая версия АСПО. Таблица отсутствует. \n')
            file_error.write(str(file))
            pass
        try:
            cursor.execute(req_22)
        except pyodbc.ProgrammingError as file:
            file_error.write('Старая версия АСПО. Таблица отсутствует. \n')
            file_error.write(str(file))
            pass
        try:
            cursor.execute(req_23)
        except pyodbc.ProgrammingError as file:
            file_error.write('Старая версия АСПО. Таблица отсутствует. \n')
            file_error.write(str(file))
            pass
        try:
            cursor.execute(req_24)
        except pyodbc.ProgrammingError as file:
            file_error.write('Старая версия АСПО. Таблица отсутствует. \n')
            file_error.write(str(file))
            pass
        try:
            cursor.execute(req_25)
        except pyodbc.ProgrammingError as file:
            file_error.write('Старая версия АСПО. Таблица отсутствует. \n')
            file_error.write(str(file))
            pass
        try:
            request_log()
        except pyodbc.ProgrammingError as file:
            file_error.write('Старая версия АСПО. Таблица отсутствует. \n')
            file_error.write(str(file))
            pass
        file_error.close()


def sh_sql():
    cursor = sql_return().cursor()
    cursor.execute(Request5)
    time.sleep(1)
    for row in cursor:
        print('row = %r' % (row,))


def request_log():
    cursor = sql_return().cursor()
    cursor.execute(rs_db_tools)
    time.sleep(1)
    cursor.execute('select count(*) from tRequestLog')
    for row in cursor:
        print('Логи запросов = %r' % (row,))


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
                file_error.write(f"{datetime_res()} line:98 (db_tools_connect) Некорректный ввод пароля\n{err}")
                file_error.close()
                n = n + 1
                if n == n_max:
                    print('Вы превысили количество попыток.')
                    with open(os.path.join(get_folder()[0], f'{TODAY}_PassError.txt'), 'w+') as file_error_pass:
                        file_error_pass.write(f"{datetime_res()} Исчерпаны попытки ввода пароля.")
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

