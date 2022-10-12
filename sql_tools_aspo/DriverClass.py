import pyodbc, configparser, os
ini_files = "sql_tools.ini"
# блок sql_tools.ini
config = configparser.ConfigParser()
config.read(ini_files)

#меню по цифрам
def UsSelect():
    num_min, num_max = 1, 5
    user_selection = [i for i in range(num_min, num_max)]
    return user_selection

#автоматом получаем драйвер из системы
def GetDriver():
    driver_id_sql = pyodbc.drivers()
    driver = driver_id_sql[1]
    return driver

#получаем ip или экземпляр
def GetServer():
    server_id = list()
    server_id.append(config["connect"]["Server"])
    server = server_id[0]
    return server

#название базы данных
def GetDataBase():
    database_id = list()
    database_id.append(config["connect"]["Database"])
    database = database_id[0]
    return database

#такая процедура появилась потом что ms sql server тут как валенок, задержка перед тем как рубить коннект
def GetTimeSleep():
    timesleep_id = list()
    timesleep_id.append((config["default"]["TimeSleep"]))
    timesleep = int(timesleep_id[0])
    return timesleep

#куда класть бэкап
def GetMyDir():
    my_dir_id = list()
    my_dir_id.append(config["system"]["MyDir"])
    my_dir = my_dir_id[0]
    return my_dir

#тут узнаем какая версия АСПО последняя
def GetRV():
    rel_version_id = list()
    rel_version_id.append(config["version"]["Version"])
    rel_version = rel_version_id[0]
    return rel_version

#базовая папка, диск etc. лучьше не выбирать C: с его проблеммами доступа
def GetFolder():
    folder_id = list()
    folder_id.append(config["system"]["Folder"])
    folder = folder_id[0]
    return folder

#как зовут бэкап базы
def GetBackUp():
    backup_id = list()
    backup_id.append(config["system"]["Backup"])
    backup = backup_id[0]
    return backup

#проверям создался ли бэкап
def check_backup():
    path = os.path.join(GetFolder(), GetMyDir())
    final_bk = os.path.exists(path)
    if final_bk is True:
        print("► Резервная копия сделана.") #Ожидаем результируюшего файла. Он будет скопирован в папку {my_dir} ")
    else:
        print("► Резервную копию сделать нельзя.")
    return final_bk

#проверяем или создаем папку для хранения бэкапа
def mk_dir_new():
    path = os.path.join(GetFolder(), GetMyDir())
    if not os.path.isdir(path):
        os.mkdir(os.path.join(GetFolder(), GetMyDir()))
        print("► Папка создана.")