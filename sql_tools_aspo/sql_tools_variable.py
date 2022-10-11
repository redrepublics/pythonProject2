import pyodbc
import os
import os.path
import configparser
import glob

class Variable:
    def __init__(self, driver, server, database, rel_version, folder, backup, file_ver):
        self.driver = driver
        self.server = server
        self.database = database
        self.rel_version = rel_version
        self.folder = folder
        self.backup = backup
        self.file_ver = file_ver


    def Driver_Variable(self):
        ini_files = "sql_tools.ini"
        config = configparser.ConfigParser()
        config.read(ini_files)
        driver_id_sql = list()
        driver_id_sql.append(config["default"]["Driver"])
        driver = driver_id_sql[0]
        return driver



file_ver = 'ver.sql'
# блок sql_tools.ini
ini_files = "sql_tools.ini"
config = configparser.ConfigParser()
config.read(ini_files)  # читаем конфиг


server_id = list()
database_id = list()
rel_version_id = list()
folder_id = list()
backup_id = list()

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