import time
from DB_tools_params import *
from DB_tools_class import sql_return




# def bak_sql():
#     cursor = sql_return().cursor()
#     cursor.execute(Request3)
#     time.sleep(1)
#     if cursor.nextset() is True:
#         print("Бэкап готов")
#         # cursor.execute(Request5)
#         # for row in cursor:
#         #     print(row)
#     else:
#         print("Неудача")
#     sql_return().close()

    # row = cursor.fetchone()
    # while row:
    #     print(row[0])
    #     row = cursor.fetchone()

def sh_sql():
    cursor = sql_return().cursor()
    cursor.execute(Request5)
    time.sleep(1)
    for row in cursor:
        print('row = %r' % (row,))
    # row = cursor.fetchone()
    #
    # if row:
    #     while row:
    #         print(row[0])
    #         row = cursor.fetchone()
    # # if cursor.nextset() is True:
    # #     print("Реиндекс готов")
    #
    # else:
    #     print('Неудача')
    sql_return().close()
    cursor.close()

sh_sql()