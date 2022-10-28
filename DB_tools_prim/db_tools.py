import time
import os
import os.path
from db_tools_request import *
from db_tools_connect import sql_return


def bak_search():
    path = os.path.join(get_folder()[0], f'SRW_688-{pars_files_bak[-1]}')
    if os.path.isfile(path) is True:
        return True
    else:
        return False


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
