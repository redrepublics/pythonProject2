import time
import os
from db_tools_request import *
from db_tools_connect import sql_return, bak_search, del_tables, sh_sql, request_log, start_password
from mess_db_tools import *


def bak_sql():
    try:
        cursor = sql_return().cursor()
    except AttributeError as err:
        with open(os.path.join(get_folder()[0], f'{TODAY}_AttributeError.txt'), 'w+') as file_error:
            file_error.write(f"{datetime_res()} line:10 (db.tools) Нет параметра для подключения\n{err}")
            file_error.close()
    else:
        if 1 == int(get_folder()[6]):
            print('Для продолжения работы введите пароль.')
            start_password()
        else:
            pass
        with open(os.path.join(get_folder()[0], f'{TODAY}_db_tools_report.txt'), 'w+') as file_error:
            ff_report = f'{TODAY}_db_tools_report.txt'
            print(mess_db_tools_1)
            file_error.write(f'{datetime_res()}: {mess_db_tools_1}\n')
            print(mess_db_tools_2)
            file_error.write(f'{datetime_res()}: {mess_db_tools_2}\n')
        cursor.execute(Request3)
        time.sleep(5)
        cursor.close()
        sql_return().close()
        bak_search()
        if bak_search() is True:
            with open(os.path.join(get_folder()[0], ff_report), 'a') as file_error:
                print(mess_db_tools_3)
                file_error.write(f'{datetime_res()}: {mess_db_tools_3}\n')
                print(mess_db_tools_4)
                file_error.write(f'{datetime_res()}: {mess_db_tools_4}\n')
                del_tables()
                request_log()
                print(mess_db_tools_5)
                file_error.write(f'{datetime_res()}: {mess_db_tools_5}\n')
                request_log()
                sh_sql()
                print(mess_db_tools_6)
                file_error.write(f'{datetime_res()}: {mess_db_tools_6}\n')
                file_error.close()
        elif bak_search() is False:
            print("Нельзя создать бэкап. Работа остановлена.")
        else:
            print('Что-то пошло не так.')


bak_sql()
