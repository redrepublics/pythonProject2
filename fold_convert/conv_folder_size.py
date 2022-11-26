import os
from pathlib import Path

folder = os.getcwd()
vid = 'video'
src = os.path.join(folder, vid)
count_avi = 0
count_del = 0


# def size_fold():
#     size = 0
#     fp = os.path.join(src)
#     size += os.path.getsize(fp)
#     result = size
#     return result

def size_fold():
    file_size = 0
    for file in Path(src).rglob('*'):
        if os.path.isfile(file):
            file_size += os.path.getsize(file)
            result = round((file_size / 1024 / 1024), 2)
    return result


def count_a():
    global count_avi
    count_avi += 1
    return count_avi


def count_d():
    global count_del
    count_del += 1
    return count_del
