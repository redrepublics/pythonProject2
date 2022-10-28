import time
import os
from db_tools_request import *
from db_tools_connect import sql_return, bak_search, del_tables, sh_sql, request_log


def bak_sql():
    try:
        cursor = sql_return().cursor()
    except AttributeError as err:
        with open(os.path.join(get_folder()[0], f'{TODAY}_AttributeError.txt'), 'w+') as file_error:
            file_error.write(f"line:9 (db.tools) Нет параметра для подключения\n{err}")
            file_error.close()
    else:
        print('Start...')
        cursor.execute(Request3)
        time.sleep(5)
        cursor.close()
        sql_return().close()
        bak_search()
        if bak_search() is True:
            print('A backup copy has been created.')
            print('We start cleaning the tables.')
            del_tables()
            request_log()
            print('Compressing the database.')
            request_log()
            sh_sql()
            print('Service is over.')
        elif bak_search() is False:
            print("I can't create a backup.")
        else:
            print('Something went wrong.')


bak_sql()
