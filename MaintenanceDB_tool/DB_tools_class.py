import configparser

ini_files = "db_tools.ini"
config = configparser.ConfigParser()
config.read(ini_files)

def getfolder():
    ini_list = list()
    ini_list.append(config["folders"]["fold"])
    ini_list.append(config["connectdb"]['driver'])
    ini_list.append(config["connectdb"]['server'])
    ini_list.append(config["connectdb"]['bddata'])
    ini_list.append(config["connectdb"]['user'])
    ini_list.append(config["connectdb"]['password'])
    return ini_list




