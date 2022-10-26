import pyodbc
import datetime
import time
from DB_tools_class import getfolder


TODAY = datetime.date.today()
Request1 = "SELECT @@version;"
Request2 = 'select * from tLocalParams'
Request3 = 'BACKUP DATABASE [' + getfolder()[3] + "] TO DISK = N'" + getfolder()[0] + "/" + getfolder()[3] + '-' + str(
                TODAY) + ".bak'"



def connect_sql():
    conn = pyodbc.connect(
        'DRIVER={' + getfolder()[1] + '};SERVER=' + getfolder()[2] + ';DATABASE=' + getfolder()[3] + ';UID=' + getfolder()[4] + ';PWD=' + getfolder()[5] + ';', autocommit=True)
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






