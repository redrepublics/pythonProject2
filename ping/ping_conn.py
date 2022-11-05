import pyodbc
from ping_params import *
import sys


# Подключаемся к серверу
def db_cursor():
    try:
        conn = pyodbc.connect(
            "DRIVER={" + get_folder()[0] + '};SERVER=' + get_folder()[1] + ';DATABASE=' + get_folder()[
                2] + ';UID=' +
            get_folder()[3] + ';PWD=' + get_folder()[4] + ';', autocommit=True)
    except pyodbc.OperationalError as err:
        err_report_one = 'Error: Ошибка подключения к SQL Server.'
        err_report_two = ('ms-sql Operation Error: {0}'.format(err))
        with open(os.path.join(os.getcwd(), 'отчеты', f'{current_time_file} Ошибка подключения.txt'),
                  'w+') as result:
            result.write(r'' + err_report_one + '\n' + err_report_two + '')
            result.close()
            print(f"Выполнение будет остановлено. {err_report_one},\n{err_report_two}")
            sys.exit(1)
    return conn
