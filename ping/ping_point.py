import time

from ping_params import *
from ping3 import ping
from ping_del_filese import file_old_del
from ping_conn import db_cursor
import csv


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


def host_name_csv():
    folder_txt()
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
    return hostname


# смотрим ответ по выводу
def ping_point():
    if 1 != get_folder()[7]:
        host_ip = host_name()
    else:
        host_ip = host_name_csv()
    for i in host_ip:
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


# Запуск основной процедуры
ping_point()
# Запуск очистки старых файлов отчета
file_old_del()
