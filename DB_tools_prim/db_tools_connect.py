import os
import os.path
import pyodbc
from db_tools_params import *


def sql_return():
    try:
        conn = pyodbc.connect(
            'DRIVER={' + get_folder()[1] + '};SERVER=' + get_folder()[2] + ';DATABASE=' + get_folder()[3] + ';UID=' +
            get_folder()[4] + ';PWD=' + get_folder()[5] + ';', autocommit=True)
    except pyodbc.Error as err:
        with open(os.path.join(get_folder()[0], f'{TODAY}_pyodbc.txt'), 'w+') as file_error:
            file_error.write(f"line:9 (db_tools_connect) Сервер не запущен, или неправильно указаны параметры "
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
