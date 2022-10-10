import pyodbc
import os
import os.path
import configparser
import glob

class Variable:
    def __init__(self):

    file_ver = 'ver.sql'


# блок sql_tools.ini
ini_files = "sql_tools.ini"
config = configparser.ConfigParser()
config.read(ini_files)  # читаем конфиг

driver_id_sql = list()
server_id = list()
database_id = list()
rel_version_id = list()
folder_id = list()
backup_id = list()
driver_id_sql.append(config["default"]["Driver"])
server_id.append(config["connect"]["Server"])
database_id.append(config["connect"]["Database"])
rel_version_id.append(config["version"]["Version"])
folder_id.append(config["system"]["Folder"])
backup_id.append(config["system"]["Backup"])
driver = driver_id_sql[0]
server = server_id[0]
database = database_id[0]
rel_version = rel_version_id[0]
folder = folder_id[0]
backup = backup_id[0]