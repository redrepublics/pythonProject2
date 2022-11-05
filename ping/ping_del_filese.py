import arrow
import os
import glob
import time
import sys
import csv
from pathlib import Path
from ping_params import get_folder
from ping_params import current_time, current_time_file

path_fold = 'отчеты'
filesPath = os.path.join(os.getcwd(), path_fold)


# удаление файлов старше (смотрим в ini параметр del_old)
def file_old_del():
    count = 0
    old_time = arrow.now().shift(days=-(int(get_folder()[6])))
    for item in Path(filesPath).glob('*.txt'):
        if item.is_file():
            item_time = arrow.get(item.stat().st_mtime)
            if item_time < old_time:
                count += 1
                os.remove(str(item.absolute()))
                pass
        if count == 0:
            pass
        else:
            print(f'Всего удалено старых отчетов: {count}')
            time.sleep(1)



# смотрим присутствие csv
def csv_dir():
    os.chdir(os.getcwd())
    for file in glob.glob("ping.csv"):
        if isinstance(file, str):
            with open('ping.csv', newline='') as File:
                reader = csv.reader(File)
        else:
            with open(os.path.join(os.getcwd(), 'отчеты', f"{current_time_file} Error.txt"), 'a') as file_2:
                file_2.write(f'{current_time} Нет SCV.')
                print('Нет SCV или он поврежден.')
                file_2.close()
                time.sleep(5)
                sys.exit(1)
        return reader
