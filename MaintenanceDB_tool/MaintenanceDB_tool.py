import time
import os
from DB_tools_params import *
from DB_tools_class import sql_return





def bak_sql():
    cursor = sql_return().cursor()
    cursor.execute(Request3)
    time.sleep(5)
    cursor.close()
    sql_return().close()
    # path = os.path.join(get_folder()[0], bak_res)
    path = os.path.join('E:', 'TEST', 'SRW_68813_15.bak')
    print(os.path.isfile(path))



bak_sql()
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

# def sh_sql():
#     cursor = sql_return().cursor()
#     cursor.execute(Request1)
#     time.sleep(1)
#     for row in cursor:
#         print('row = %r' % (row,))
#     # row = cursor.fetchone()
#     #
#     # if row:
#     #     while row:
#     #         print(row[0])
#     #         row = cursor.fetchone()
#     # # if cursor.nextset() is True:
#     # #     print("Реиндекс готов")
#     #
#     # else:
#     #     print('Неудача')
#     sql_return().close()
#     cursor.close()
# sh_sql()

