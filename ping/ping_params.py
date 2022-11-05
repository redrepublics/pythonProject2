import configparser
import datetime
import os

ini_files = 'ping.ini'
config = configparser.ConfigParser()
config.read(ini_files)
# отлавливаем временную метку для записи в лог
now = datetime.datetime.now()
current_time = now.strftime("%y.%m.%d %H:%M:%S")
current_time_file = now.strftime("%y_%m_%d_%H_%M_%S")
output_t = 1
del_t = '\\'
hostname = []
req = 'select IPAddress from tNodesDetails'


# тут забираем параметры из ini и выводим их в список
def get_folder():
    ini_list = list()
    ini_list.append(config["connectdb"]['driver'])
    ini_list.append(config["connectdb"]['server'])
    ini_list.append(config["connectdb"]['bd_data'])
    ini_list.append(config["connectdb"]['user'])
    ini_list.append(config["connectdb"]['password'])
    ini_list.append(config["terminal"]['terminal_output'])
    ini_list.append(config["terminal"]['del_old_f'])
    ini_list.append(config["aspo"]['modeon'])
    return ini_list


# Создаем папку для хранения отчетов, если уже есть - pass
def folder_txt():
    if not os.path.exists(os.path.join(os.getcwd(), 'отчеты')):
        os.makedirs(os.path.join(os.getcwd(), 'отчеты'))
    else:
        pass
