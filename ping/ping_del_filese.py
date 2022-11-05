import arrow
import os
import glob
import time
import sys
from pathlib import Path
from ping_params import get_folder
from ping_params import current_time, current_time_file

path_fold = 'отчеты'
filesPath = os.path.join(os.getcwd(), path_fold)


def file_old_del():
    old_time = arrow.now().shift(days=-(int(get_folder()[6])))
    for item in Path(filesPath).glob('*.txt'):
        if item.is_file():
            # print(str(item.absolute()))
            item_time = arrow.get(item.stat().st_mtime)
            if item_time < old_time:
                os.remove(str(item.absolute()))
                pass


def csv_dir():
    os.chdir(os.getcwd())
    for file in glob.glob("ping.csv"):
        if file:
            pass
        else:
            with open(os.path.join(os.getcwd(), 'отчеты', f"{current_time_file} Error.txt"), 'a') as file:
                file.write(f'{current_time} Нет SCV.')
                print('Нет SCV или он поврежден.')
                time.sleep(5)
            sys.exit(1)
