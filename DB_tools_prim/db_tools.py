import time
import os
from db_tools_request import *
from db_tools_connect import sql_return, bak_search, del_tables, sh_sql, request_log, start_password


def bak_sql():
    try:
        cursor = sql_return().cursor()
    except AttributeError as err:
        with open(os.path.join(get_folder()[0], f'{TODAY}_AttributeError.txt'), 'w+') as file_error:
            file_error.write(f"line:9 (db.tools) Нет параметра для подключения\n{err}")
            file_error.close()
    else:
        if 1 == int(get_folder()[6]):
            print('Для продолжения работы введите пароль.')
            start_password()
        else:
            pass
        print('Start...')
        print('Начинаем резервное копирование базы данных.')
        cursor.execute(Request3)
        time.sleep(5)
        cursor.close()
        sql_return().close()
        bak_search()
        if bak_search() is True:
            print('Резервная копия базы данных создана.')
            print('Чистим таблицы.')
            del_tables()
            request_log()
            print('Сжимаем базу данных.')
            request_log()
            sh_sql()
            print('Обслуживание завершено.')
        elif bak_search() is False:
            print("Нельзя создать бэкап. Работа остановлена.")
        else:
            print('Что-то пошло не так.')


bak_sql()
