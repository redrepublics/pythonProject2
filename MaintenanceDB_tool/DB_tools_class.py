import configparser
import pyodbc
ini_files = "db_tools.ini"
config = configparser.ConfigParser()
config.read(ini_files)

def sql_return():
    conn = pyodbc.connect(
        'DRIVER={' + get_folder()[1] + '};SERVER=' + get_folder()[2] + ';DATABASE=' + get_folder()[3] + ';UID=' +
        get_folder()[4] + ';PWD=' + get_folder()[5] + ';', autocommit=True)
    return conn

def get_folder():
    ini_list = list()
    ini_list.append(config["folders"]["fold"])
    ini_list.append(config["connectdb"]['driver'])
    ini_list.append(config["connectdb"]['server'])
    ini_list.append(config["connectdb"]['bddata'])
    ini_list.append(config["connectdb"]['user'])
    ini_list.append(config["connectdb"]['password'])
    return ini_list
