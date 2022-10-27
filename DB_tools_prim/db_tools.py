import configparser
import pyodbc
import time
import os
from datetime import datetime
import os.path

ini_files = "db_tools.ini"
config = configparser.ConfigParser()
config.read(ini_files)


def sql_return():
    conn = pyodbc.connect(
        'DRIVER={' + get_folder()[1] + '};SERVER=' + get_folder()[2] + ';DATABASE=' + get_folder()[3] + ';UID=' +
        get_folder()[4] + ';PWD=' + get_folder()[5] + ';', autocommit=True)
    return conn


def get_folder():
    ini_list = list()
    ini_list.append(config["folders"]["fold"])
    ini_list.append(config["connectdb"]['driver'])
    ini_list.append(config["connectdb"]['server'])
    ini_list.append(config["connectdb"]['bddata'])
    ini_list.append(config["connectdb"]['user'])
    ini_list.append(config["connectdb"]['password'])
    return ini_list


now = datetime.now()
TODAY = now.strftime("%y_%m_%d_%H_%M_%S")
file_name_bak = f'{get_folder()[3]}{TODAY}'
bak_res = f'{file_name_bak}.bak'
pars_files_bak = [bak_res]

Request1 = "SELECT @@version;"
Request2 = 'select * from tLocalParams'
Request3 = 'BACKUP DATABASE [' + get_folder()[3] + "] TO DISK = N'" + get_folder()[0] + "/" + get_folder()[
    3] + '-' + bak_res + "'"  # рабочий бэкап
Request5 = 'DBCC SHRINKDATABASE (' + get_folder()[3] + ', 10);'  # рабочий шринк

req_1 = 'delete tRExamComplaints'
req_2 = 'delete tRemoteExams'
req_3 = 'delete tRemoteExamSignature'


def testtest():
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
    testtest()
    if testtest() is True:
        print('Резервная копия создана.')
    elif testtest() is False:
        print('Не могу создать резервную копию.')
    else:
        print('Что-то пошло не так.')


bak_sql()
