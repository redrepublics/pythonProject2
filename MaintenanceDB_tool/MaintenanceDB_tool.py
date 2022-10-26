import pyodbc
import datetime
import time
import os
import os.path

driver = 'SQL Server Native Client 11.0'
server = "localhost"  # Название сервера SQL, к которому будет выполнено подключение.
bddata = "SRW_688"  # Имя базы данных SQL
user = "sa"  # Имя пользователя SQL
password = "daorliar"  # Пароль пользователя SQL
TODAY = datetime.date.today()
# location = os.getcwd()
folder = os.path.join('E:\\', 'TEST')
# print(folder)
# location = 'E:\TEST'


Request1 = "SELECT @@version;"
Request2 = 'select * from tLocalParams'
Request3 = 'BACKUP DATABASE [' + bddata + "] TO DISK = N'" + folder + "/" + bddata + '-' + str(
                TODAY) + ".bak'"
query = ("""BACKUP DATABASE SRW_688
            TO DISK = 'E:/test_db.BAK';""")


def connect_sql():
    conn = pyodbc.connect(
        'DRIVER={' + driver + '};SERVER=' + server + ';DATABASE=' + bddata + ';UID=' + user + ';PWD=' + password + ';', autocommit=True)
    cursor = conn.cursor()
    cursor.execute(Request3)
    time.sleep(1)
    # print(type(cursor.nextset()))
    if cursor.nextset() is True:
        print("Бэкап готов")
    else:
        print("Неудача")
    conn.close()


    # row = cursor.fetchone()
    # while row:
    #     print(row[0])
    #     row = cursor.fetchone()


connect_sql()






