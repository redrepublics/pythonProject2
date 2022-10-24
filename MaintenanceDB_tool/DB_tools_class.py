import pyodbc


class Request:
    def __init__(self, requestString):
        self.requestString = requestString

    def Get_RequestString(self):
        return self.requestString


def get_connect():
    # database = "SRW_688"
    # server = "192.168.0.116"
    # username = "sa"
    # password = "daorliar"
    driver = 'SQL Server Native Client 11.0'

    # server = 'localhost\sqlexpress'  # для особых случаев
    # server = 'myserver,port'  # для указания альтернативного порта

    server = "192.168.0.116"  # Название сервера SQL, к которому будет выполнено подключение.
    bddata = "SRW_688"  # Имя базы данных SQL
    user = "sa"  # Имя пользователя SQL
    password = "daorliar"  # Пароль пользователя SQL
    connect = pyodbc.connect(
        'DRIVER={' + driver + '};SERVER=' + server + ';DATABASE=' + bddata + ';UID=' + user + ';PWD=' + password + ';')


    return connect


get_connect()
