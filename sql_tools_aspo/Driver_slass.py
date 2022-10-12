import pyodbc, configparser, os
ini_files = "sql_tools.ini"
# блок sql_tools.ini
config = configparser.ConfigParser()
config.read(ini_files)

def UsSelect():
    num_min, num_max = 1, 5
    user_selection = [i for i in range(num_min, num_max)]
    return user_selection

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

def check_backup():
    path = os.path.join(GetFolder(), GetMyDir())
    final_bk = os.path.exists(path)
    if final_bk is True:
        print("► Резервная копия сделана.") #Ожидаем результируюшего файла. Он будет скопирован в папку {my_dir} ")
    else:
        print("► Резервную копию сделать нельзя.")
    return final_bk


def mk_dir_new():
    path = os.path.join(GetFolder(), GetMyDir())
    if not os.path.isdir(path):
        os.mkdir(os.path.join(GetFolder(), GetMyDir()))
        print("► Папка создана.")