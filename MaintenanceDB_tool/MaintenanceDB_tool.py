# import pyodbc
import pypyodbc
import datetime
import os

driver = 'SQL Server Native Client 11.0'
server = "localhost"  # Название сервера SQL, к которому будет выполнено подключение.
bddata = "SRW_688"  # Имя базы данных SQL
user = "sa"  # Имя пользователя SQL
password = "daorliar"  # Пароль пользователя SQL
TODAY = datetime.date.today()
location = os.getcwd()
print(location)

Request1 = "SELECT @@version;"
Request2 = 'select * from tLocalParams'
Request3 = 'BACKUP DATABASE [' + bddata + "] TO DISK = N'" + location + "/" + bddata + '-' + str(
                TODAY) + ".bak'"
query = ("""BACKUP DATABASE SRW_688
            TO DISK = 'E:/test_db.BAK';""")


def connect_sql():
    conn = pypyodbc.connect(
        'DRIVER={' + driver + '};SERVER=' + server + ';DATABASE=' + bddata + ';UID=' + user + ';PWD=' + password + ';',autocommit=True)

    cursor = conn.cursor()
    # cursor.execute(backup)
    cursor.execute(Request3)

    for row in cursor:
        print('Переменная:', row[0], 'параметр:', row[1])
    cursor.close()





connect_sql()






