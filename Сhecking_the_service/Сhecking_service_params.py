import configparser

""" Тут читаем данные из ini
count_max - сколько попыток (шт)
time_sleep - сколько ждем до следующей попытки (секунды)
ser_name - название службы которую ищем и контролируем"""


ini_files = 'Сhecking_service.ini'
config = configparser.ConfigParser()
config.read(ini_files)


def get_ini():
    ini_list = list()
    ini_list.append(config["default"]['count_max'])
    ini_list.append(config["default"]['time_sleep'])
    ini_list.append(config["default"]['ser_name'])
    return ini_list


count_m = int(get_ini()[0])
s_time = int(get_ini()[1])
serv = get_ini()[2]
