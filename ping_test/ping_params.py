import configparser
import datetime

# тут забираем параметры из ini и выводим их в список
ini_files = 'ping.ini'
config = configparser.ConfigParser()
config.read(ini_files)
# отлавливаем временную метку для записи в лог
now = datetime.datetime.now()
current_time = now.strftime("%y_%m_%d_%H_%M_%S")
output_t = 1


def get_folder():
    ini_list = list()
    ini_list.append(config["connectdb"]['driver'])
    ini_list.append(config["connectdb"]['server'])
    ini_list.append(config["connectdb"]['bd_data'])
    ini_list.append(config["connectdb"]['user'])
    ini_list.append(config["connectdb"]['password'])
    ini_list.append(config["terminal"]['terminal_output'])
    return ini_list
