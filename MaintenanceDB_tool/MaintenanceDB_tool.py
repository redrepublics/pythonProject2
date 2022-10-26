import time
from DB_tools_params import *
from DB_tools_class import sql_return


def connect_sql():
    cursor = sql_return().cursor()
    cursor.execute(Request3)
    time.sleep(1)
    if cursor.nextset() is True:
        print("Бэкап готов")
    else:
        print("Неудача")
    sql_return().close()

    # row = cursor.fetchone()
    # while row:
    #     print(row[0])
    #     row = cursor.fetchone()


connect_sql()
