import subprocess
import os
import sys
import configparser
from conv_folder_size import size_fold, count_a, count_d

# from origin import origin_def

folder = os.getcwd()
vid = 'video'
src = os.path.join(folder, vid)
del_files = []
ini_files = "conv_avi_to_mp4.ini"
config = configparser.ConfigParser()
config.read(ini_files)


def get_folder():
    ini_list = list()
    ini_list.append(config["result_cod"]["del_avi"])
    return ini_list


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


def basic_conversion():
    num_one = size_fold()
    convert_and_folder_search()
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
        print('Мы уменьшили размер папки на:', num_one - num_two, 'Мбайт.')
    print(f'Было: {num_one} Мбайт.\nСтало: {num_two} Мбайт. ')
    print(f'Конвертировали: {count_a() - 1} шт.')
    print(f'Удалили: {count_d() - 1} шт.')


basic_conversion()
