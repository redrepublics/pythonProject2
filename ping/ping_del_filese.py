import arrow
import os
from pathlib import Path
from ping_params import get_folder


path_fold = 'отчеты'
filesPath = os.path.join(os.getcwd(), path_fold)


def file_old_del():
    old_time = arrow.now().shift(days=-(int(get_folder()[6])))
    print(old_time)
    for item in Path(filesPath).glob('*.txt'):
        if item.is_file():
            # print(str(item.absolute()))
            item_time = arrow.get(item.stat().st_mtime)
            if item_time < old_time:
                os.remove(str(item.absolute()))
                pass
