import pyodbc
from db_tools_params import *


def sql_return():
    conn = pyodbc.connect(
        'DRIVER={' + get_folder()[1] + '};SERVER=' + get_folder()[2] + ';DATABASE=' + get_folder()[3] + ';UID=' +
        get_folder()[4] + ';PWD=' + get_folder()[5] + ';', autocommit=True)
    return conn
