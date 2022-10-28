import time
from db_tools_request import *
from db_tools_connect import sql_return, bak_search

def bak_sql():
    cursor = sql_return().cursor()
    print('Start...')
    cursor.execute(Request3)
    time.sleep(5)
    cursor.close()
    sql_return().close()
    bak_search()
    if bak_search() is True:
        print('Резервная копия создана.')
    elif bak_search() is False:
        print('Не могу создать резервную копию.')
    else:
        print('Что-то пошло не так.')


bak_sql()
