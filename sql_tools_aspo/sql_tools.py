#добавить проверку наличия ini
#добавить действие бэкапа базы
#реализовать чтение запроса из файла *.sql
#обрабатывать ошибки при неправильных параметрах в ini
import pyodbc
import os
import configparser
from sql_tools_class import Request
folder = os.getcwd()
file_ver = 'ver.sql'

# блок sql_tools.ini
ini_files = "sql_tools.ini"
config = configparser.ConfigParser()
config.read(ini_files)  # читаем конфиг
driver_id_sql = list()
server_id = list()
database_id = list()
driver_id_sql.append(config["default"]["Driver"])
server_id.append(config["connect"]["Server"])
database_id.append(config["connect"]["Database"])
driver = driver_id_sql[0]
server = server_id[0]
database = database_id[0]
rel_version = 'версия БД 3.1.1.8'


def connect_sql():
    connectionString = ("Driver={" + driver + "};" "Server=" + server + ";" "Database=" + database + ";" "Trusted_Connection=yes;")
    connection = pyodbc.connect(connectionString, autocommit=True)
    dbCursor = connection.cursor()

    while True:
        global request_user
        try:
            request_user = int(input("Запрос в tUserDetails............[1]\nУзнать версию сервера MS SQL.....[2]\nУзнать версию базы АСПО..........[3]\n"))
        except ValueError or NameError:
            print('Я так не умею')
            break
        if request_user == 1:
            dbCursor.execute(Request1.Get_RequestString())
            connection.commit()
            for respond_sql in dbCursor:
                print(respond_sql)
            break
        elif request_user == 2:
            dbCursor.execute(Request2.Get_RequestString())
            connection.commit()
            for respond_sql in dbCursor:
                print(respond_sql)
            break
#выполняем скрипт sql, предварительно читая его из файла
        elif request_user == 3:
            with open(file_ver, 'r', encoding='utf-8') as sql_file:
                result_iterator = dbCursor.execute(sql_file.read())
                for respond_sql in result_iterator:
                    print(respond_sql)
                    if rel_version in respond_sql:
                        print(f"У вас последняя версия {respond_sql}")
                    else:
                        print(f"Версию можно обновить. Последняя версия {rel_version}. Ваша версия: {respond_sql}")
                    continue
                break


            # dbCursor.execute(Request3.Get_RequestString())
            # connection.commit()
            # for respond_sql in dbCursor:
            #     print(respond_sql)
            # break
        else:
            print('Что-то пошло не так.')




#началоблока запросов
Request1 = Request('select top(10)*, LName from tUserDetails order by RecTime DESC')
Request2 = Request('select @@VERSION')
# Request3 = Request()

connect_sql()








