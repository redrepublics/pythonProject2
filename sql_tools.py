import pyodbc
import configparser


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



def connect_sql():
    connectionString = ("Driver={" + driver + "};" "Server=" + server + ";" "Database=" + database + ";" "Trusted_Connection=yes;")
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








