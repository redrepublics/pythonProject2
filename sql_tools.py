# вариант утилиты для сверки данных
# добавить инпуты переменных для подключения к нужной базе данных, а не дефолтной
# попробовать вариант чтения скрипта из файла
# путь из get == добавление необходимых импортов
# найти возможность подгрузки параметров коннекта из файла на пк (сделать ini)


import pyodbc


driver_id = pyodbc.drivers()
print(driver_id)
drever_id_sql = driver_id[1]
server = 'localhost'
database = 'SRW_688'

def connect_sql():
    connectionString = ("Driver={"+drever_id_sql+"};" "Server="+server+";" "Database="+database+";" "Trusted_Connection=yes;")
    connection = pyodbc.connect(connectionString, autocommit=True)
    dbCursor = connection.cursor()
    requestString = ('select top(10)*, LName from tUserDetails order by RecTime DESC')
    requestString2 = ('select @@VERSION')

    while True:
        global request_user
        try:
            request_user = int(input("Запрос в tUserDetails............[1]\nУзнать версию сервера MS SQL.....[2]\n"))
        except ValueError or NameError:
            print('Я так не умею')
            break
        if request_user == 1:
            dbCursor.execute(requestString)
            connection.commit()
            for respond_sql in dbCursor:
                print(respond_sql)
            break
        elif request_user == 2:
            dbCursor.execute(requestString2)
            connection.commit()
            for respond_sql in dbCursor:
                print(respond_sql)
            break
        else:
            print('Что-то пошло не так.')

connect_sql()








