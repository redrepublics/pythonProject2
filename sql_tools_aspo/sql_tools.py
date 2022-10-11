#добавить проверку наличия ini
#добавить действие бэкапа базы
#реализовать чтение запроса из файла *.sql
#обрабатывать ошибки при неправильных параметрах в ini
#проработка закрытия открытых файлов
import pyodbc
import os
import os.path
import configparser
from sql_tools_class import Request
from pathlib import Path
import shutil
import time

ini_files = "sql_tools.ini"
file_ver = 'ver.sql'
# блок sql_tools.ini
config = configparser.ConfigParser()
config.read(ini_files)  # читаем конфиг

#подготовка переменных
# file_ver_id = list()


timesleep_id = list()
my_dir_id = list()
driver_id_sql = pyodbc.drivers()
server_id = list()
database_id = list()
rel_version_id = list()
folder_id = list()
backup_id = list()

#запрос переменных
server_id.append(config["connect"]["Server"])
database_id.append(config["connect"]["Database"])
rel_version_id.append(config["version"]["Version"])
folder_id.append(config["system"]["Folder"])
backup_id.append(config["system"]["Backup"])
my_dir_id.append(config["system"]["MyDir"])
timesleep_id.append((config["default"]["TimeSleep"]))
#получение переменных из ini
# file_ver = file_ver_id[0]
driver = driver_id_sql[1]
server = server_id[0]
database = database_id[0]
rel_version = rel_version_id[0]
folder = folder_id[0]
backup = backup_id[0]
my_dir = my_dir_id[0]
timesleep = int(timesleep_id[0])

def connect_sql():
    connectionString = ("Driver={" + driver + "};" "Server=" + server + ";" "Database=" + database + ";" "Trusted_Connection=yes;")
    connection = pyodbc.connect(connectionString, autocommit=True)
    dbCursor = connection.cursor()

    while True:
        global request_user
        try:
            request_user = int(input("""Запрос в tUserDetails............[1]
Узнать версию сервера MS SQL.....[2]
Узнать версию базы АСПО..........[3]\n"""))
        except ValueError or NameError:
            print('Я так не умею')
            continue
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
                        print(f"У вас последняя {respond_sql}")
                    else:
                        print(f"Версию можно обновить.\nПоследняя {rel_version} ► Ваша: {respond_sql}")
                        print('█'*30)
                        print("Делаем резервную копию базы данных")
                        dbCursor.execute(Request3.Get_RequestString())
                        connection.commit()
                        connection.autocommit = True
                        time.sleep(timesleep)
                        mk_dir_new()
                        dbCursor.close()#закрываем работу с запросм, после выполнения.
                        print("Идет копирование бэкапа.")
                        shutil.move(os.path.join(folder, backup), os.path.join(folder, my_dir, backup))
                        result_bk = check_backup()
                        if result_bk is True:
                            print("Запускаем обновление")
                            break
                        else:
                            print("Обновление невозможно, сначала сделайте резервную копию")
                            break

                    break
                break
        else:
            print('Что-то пошло не так.')

def check_backup():
    path = os.path.join(folder, my_dir)
    final_bk = os.path.exists(path)
    if final_bk is True:
        print("Резервная копия сделана.") #Ожидаем результируюшего файла. Он будет скопирован в папку {my_dir} ")
    else:
        print("Резервную копию сделать нельзя.")
    return final_bk


def mk_dir_new():
    path = os.path.join(folder, my_dir)
    if not os.path.isdir(path):
        os.mkdir(os.path.join(folder, my_dir))
        print("Папка создана")






#началоблока запросов
Request1 = Request('select top(10)*, LName from tUserDetails order by RecTime DESC')
Request2 = Request('select @@VERSION')
# bac = r"BACKUP DATABASE [" + database + "] TO  DISK = N'" + folder + "" + backup + ";'"
Request3 = Request(r"BACKUP DATABASE [" + database + "] TO  DISK = N'" + folder + "" + backup + "'")


connect_sql()








