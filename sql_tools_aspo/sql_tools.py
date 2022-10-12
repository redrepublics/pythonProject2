#обрабатывать ошибки при неправильных параметрах в ini
#проработка закрытия открытых файлов
import pyodbc, os, os.path, configparser, shutil, time
from sql_tools_class import Request


ini_files = "sql_tools.ini"
file_ver = 'ver.sql'
# блок sql_tools.ini
config = configparser.ConfigParser()
config.read(ini_files)  # читаем конфиг


def GetDriver():
    driver_id_sql = pyodbc.drivers()
    driver = driver_id_sql[1]
    return driver
def GetServer():
    server_id = list()
    server_id.append(config["connect"]["Server"])
    server = server_id[0]
    return server
def GetDataBase():
    database_id = list()
    database_id.append(config["connect"]["Database"])
    database = database_id[0]
    return database

def GetTimeSleep():
    timesleep_id = list()
    timesleep_id.append((config["default"]["TimeSleep"]))
    timesleep = int(timesleep_id[0])
    return timesleep
def GetMyDir():
    my_dir_id = list()
    my_dir_id.append(config["system"]["MyDir"])
    my_dir = my_dir_id[0]
    return my_dir

def GetRV():
    rel_version_id = list()
    rel_version_id.append(config["version"]["Version"])
    rel_version = rel_version_id[0]
    return rel_version

def GetFolder():
    folder_id = list()
    folder_id.append(config["system"]["Folder"])
    folder = folder_id[0]
    return folder

def GetBackUp():
    backup_id = list()
    backup_id.append(config["system"]["Backup"])
    backup = backup_id[0]
    return backup



def connect_sql():
    connectionString = ("Driver={" + GetDriver() + "};" "Server=" + GetServer() + ";" "Database=" + GetDataBase() + ";" "Trusted_Connection=yes;")
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
                sql_file.close()
                for respond_sql in result_iterator:
                    if GetRV() in respond_sql:
                        print(f"У вас последняя {respond_sql}")
                    else:
                        print(f"Версию можно обновить.\nПоследняя {GetRV()} ► Ваша: {respond_sql}")
                        print('█'*35)
                        print("Делаем резервную копию базы данных")
                        dbCursor.execute(Request3.Get_RequestString())
                        connection.commit()
                        connection.autocommit = True
                        time.sleep(GetTimeSleep())
                        mk_dir_new()
                        dbCursor.close()#закрываем работу с запросм, после выполнения.
                        print("Идет копирование бэкапа.")
                        shutil.move(os.path.join(GetFolder(), GetBackUp()), os.path.join(GetFolder(), GetMyDir(), GetBackUp()))
                        result_bk = check_backup()
                        if result_bk is True:
                            print("Запускаем обновление!")
                            break
                        else:
                            print("Обновление невозможно, сначала сделайте резервную копию")
                            break

                    break
                break
        else:
            print('Что-то пошло не так.')

def check_backup():
    path = os.path.join(GetFolder(), GetMyDir())
    final_bk = os.path.exists(path)
    if final_bk is True:
        print("Резервная копия сделана.") #Ожидаем результируюшего файла. Он будет скопирован в папку {my_dir} ")
    else:
        print("Резервную копию сделать нельзя.")
    return final_bk


def mk_dir_new():
    path = os.path.join(GetFolder(), GetMyDir())
    if not os.path.isdir(path):
        os.mkdir(os.path.join(GetFolder(), GetMyDir()))
        print("Папка создана")






#начало блока запросов
Request1 = Request('select top(10)*, LName from tUserDetails order by RecTime DESC')
Request2 = Request('select @@VERSION')
Request3 = Request(r"BACKUP DATABASE [" + GetDataBase() + "] TO  DISK = N'" + GetFolder() + "" + GetBackUp() + "'")


connect_sql()








