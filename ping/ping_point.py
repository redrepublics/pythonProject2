import sys
import time

from ping_params import *
from ping3 import ping
from ping_del_filese import file_old_del
from ping_conn import db_cursor
import csv
import glob


# проверяем csv
def csv_dir():
    os.chdir(os.getcwd())
    for file in glob.glob("ping.csv"):
        if file is not None:
            with open('ping.csv', newline='') as File:
                reader = csv.reader(File)
        elif file is None:
            with open(os.path.join(os.getcwd(), 'отчеты', f"{current_time_file} Error.txt"), 'a') as file_2:
                file_2.write(f'{current_time} Нет SCV.')
                print('Нет SCV или он поврежден.')
                file_2.close()
                time.sleep(5)
            sys.exit(1)
        return reader


# делаем запрос на IP, создаем список, убираем все лишнее, в том числе и экземпляры
def host_name():
    folder_txt()
    cursor = db_cursor().cursor()
    cursor.execute(req)
    for row in cursor:
        x = ",".join(row)
        hostname.append(x)
        for person in hostname:
            if del_t in person:
                hostname.remove(person)
                with open(os.path.join(os.getcwd(), 'отчеты', f"{current_time_file} Сомнительная запись.txt"),
                          'w+') as file:
                    file.write(f'{current_time} Проверить вручную: {person}\n')
                    file.close()
            else:
                pass
    cursor.close()
    return hostname


# делам запрос из csv + еще одна проверка на наличие файла, удаляем вск кривые записи
def host_name_csv():
    folder_txt()
    csv_dir()
    try:
        with open('ping.csv', newline='') as File:
            reader = csv.reader(File)
            for row in reader:
                x = ",".join(row)
                hostname.append(x)
            for person in hostname:
                if del_t in person:
                    hostname.remove(person)
                    with open(os.path.join(os.getcwd(), 'отчеты', f"{current_time_file} Сомнительная запись.txt"),
                              'w+') as file:
                        file.write(f'{current_time} Проверить вручную: {person}\n')
                        file.close()
                else:
                    pass
    except FileNotFoundError:
        with open(os.path.join(os.getcwd(), 'отчеты', f"{current_time_file} Error.txt"), 'a') as file_2:
            file_2.write(f'{current_time} Нет SCV.')
            print('Нет SCV или он поврежден.')
            sys.exit(1)
    return hostname


# выбираем, откуда будем читать 1 - из базы, 0 из csv, иначе выход с сообщением об ошибке ini - modeon
def ip_list():
    if int(get_folder()[7]) == 1:
        host_ip = host_name()
        if host_ip:
            return host_ip
        else:
            with open(os.path.join(os.getcwd(), 'отчеты', f"{current_time_file} Ошибка АСПО.txt"), 'a') as file:
                file.write(f'{current_time} Нет адресов для работы в базе АСПО.')
                print('Нет адресов для работы в базе АСПО.')
            sys.exit(1)
    elif int(get_folder()[7]) == 0:
        host_ip = host_name_csv()
        if host_ip:
            return host_ip
        else:
            with open(os.path.join(os.getcwd(), 'отчеты', f"{current_time_file} Ошибка CSV.txt"), 'a') as file:
                file.write(f'{current_time} Пустой или некорректный csv.')
                print('Пустой или некорректный csv. Файл должен находиться в той же паке, что и ПО.')
            sys.exit(1)
    else:
        with open(os.path.join(os.getcwd(), 'отчеты', f"{current_time_file} Ошибка.txt"), 'a') as file:
            file.write(f'{current_time} Нет адресов для работы.')
            print('Нет данных для работы')
        sys.exit(1)


# смотрим ответ по выводу из ip_list
def ping_point():
    for i in ip_list():
        i = str(i)
        ping(i)
        if ping(i):
            with open(os.path.join(os.getcwd(), 'отчеты', f"{current_time_file} Доступные_хосты.txt"), 'a') as file:
                file.write(f'{current_time} Доступен: {i}\n')
            if int(get_folder()[5]) == 1:
                print(f'{i} - Успех.')
                time.sleep(1)
            else:
                pass
        else:
            with open(os.path.join(os.getcwd(), 'отчеты', f"{current_time_file} Недоступные_хосты.txt"), 'a') as file:
                file.write(f'{current_time} Недоступен: {i}\n')
            if int(get_folder()[5]) == 1:
                print(f'{i} - Провал.')
                time.sleep(1)
            else:
                pass


file_old_del()
# Запуск основной процедуры
ping_point()
# Запуск очистки старых файлов отчета
file_old_del()

