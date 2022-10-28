import configparser
from datetime import datetime

ini_files = "db_tools.ini"
config = configparser.ConfigParser()
config.read(ini_files)


def get_folder():
    ini_list = list()
    ini_list.append(config["folders"]["fold"])
    ini_list.append(config["connectdb"]['driver'])
    ini_list.append(config["connectdb"]['server'])
    ini_list.append(config["connectdb"]['bddata'])
    ini_list.append(config["connectdb"]['user'])
    ini_list.append(config["connectdb"]['password'])
    return ini_list


now = datetime.now()
TODAY = now.strftime("%y_%m_%d_%H_%M_%S")
file_name_bak = f'{get_folder()[3]}{TODAY}'
bak_res = f'{file_name_bak}.bak'
pars_files_bak = [bak_res]
