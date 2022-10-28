import os
import pyodbc
from db_tools_params import *


def sql_return():
    conn = pyodbc.connect(
        'DRIVER={' + get_folder()[1] + '};SERVER=' + get_folder()[2] + ';DATABASE=' + get_folder()[3] + ';UID=' +
        get_folder()[4] + ';PWD=' + get_folder()[5] + ';', autocommit=True)
    return conn


def bak_search():
    path = os.path.join(get_folder()[0], f'SRW_688-{pars_files_bak[-1]}')
    if os.path.isfile(path) is True:
        return True
    else:
        return False
