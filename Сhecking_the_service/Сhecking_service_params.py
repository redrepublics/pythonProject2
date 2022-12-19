import configparser


ini_files = 'Сhecking_service.ini'
config = configparser.ConfigParser()
config.read(ini_files)


def get_folder():
    ini_list = list()
    ini_list.append(config["default"]['count_max'])
    ini_list.append(config["default"]['time_sleep'])
    ini_list.append(config["default"]['ser_name'])
    return ini_list


count_m = int(get_folder()[0])
s_time = int(get_folder()[1])
serv = get_folder()[2]
