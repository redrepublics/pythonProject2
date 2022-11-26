import subprocess
import os
import sys
import configparser
from conv_folder_size import size_fold, count_a, count_d
import datetime
import arrow
from pathlib import Path

folder = os.getcwd()
vid = 'video'
src = os.path.join(folder, vid)
del_files = []
ini_files = "conv_avi_to_mp4.ini"
config = configparser.ConfigParser()
config.read(ini_files)
now = datetime.datetime.now()
current_time = now.strftime("%y.%m.%d %H:%M:%S")
current_time_file = now.strftime("%y_%m_%d_%H_%M_%S")


# Читаем из инишника, удалять или нет файлы
def get_folder():
    ini_list = list()
    ini_list.append(config["result_cod"]["del_avi"])
    return ini_list


# проверяем наличие конвертера
def convert_and_folder_search():
    is_folder_video = os.path.exists(src)
    if is_folder_video:
        is_conv = os.path.exists(os.path.join(folder, 'ffmpeg.exe'))
        if is_conv:
            pass
        else:
            sys.exit(0)
    else:
        sys.exit(0)


# Основная конверсия с записью логов события
def basic_conversion():
    num_one = size_fold()
    convert_and_folder_search()
    report_file()
    for root, dirs, filenames in os.walk(src, topdown=False):
        for filename in filenames:
            if ".avi" in filename:
                count_a()
                input_file = os.path.join(root, filename)
                del_files.append(input_file)
                output_file = os.path.join(src, filename.replace(".avi", ".mp4"))
                subprocess.run(['ffmpeg', '-loglevel', 'quiet', '-y', '-i', input_file, output_file])
            else:
                pass
    if int(get_folder()[0]) == 1:
        for x in del_files:
            count_d()
            os.remove(x)
    num_two = size_fold()
    if int(get_folder()[0]) == 1:
        with open(os.path.join(src, f'{current_time_file}_report.txt'), 'a') as file:
            result = num_one - num_two
            file.write('\nМы уменьшили размер папки на: {0}, Мбайт.'.format(result))
    elif int(get_folder()[0]) == 0:
        with open(os.path.join(src, f'{current_time_file}_report.txt'), 'a') as file:
            result = num_two - num_one
            file.write('\nМы увеличили размер папки на: {0} Мбайт.'.format(result))
            file.write('\nДля удаления сконвертированных avi измените del_avi')
    else:
        with open(os.path.join(src, f'{current_time_file}_report.txt'), 'a') as file:
            file.write('\nНеправильная настройка.')
    with open(os.path.join(src, f'{current_time_file}_report.txt'), 'a') as file:
        file.write(f"\nБыло: {num_one} Мбайт.\nСтало: {num_two} Мбайт. ")
        file.write(f'\nКонвертировали: {count_a() - 1} шт.')
        file.write(f'\nУдалили: {count_d() - 1} шт.')
    file.close()


# Создаем лог
def report_file():
    if not os.path.exists(os.path.join(src, f'{current_time_file}_report.txt')):
        with open(os.path.join(src, f'{current_time_file}_report.txt'), 'w'):
            pass


# Проверяем логи за 10 дней, если есть старые то фиксим
def del_report():
    old_time = arrow.now().shift(days=-10)
    for item in Path(src).glob('*.txt'):
        if item.is_file():
            item_time = arrow.get(item.stat().st_mtime)
            if item_time < old_time:
                os.remove(str(item.absolute()))
                pass


basic_conversion()
del_report()
