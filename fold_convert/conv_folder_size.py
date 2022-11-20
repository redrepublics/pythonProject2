import os

folder = os.getcwd()
vid = 'video'
src = os.path.join(folder, vid)
count_avi = 0
count_del = 0


def size_fold():
    size = 0
    for path, dirs, files in os.walk(src):
        for f in files:
            fp = os.path.join(path, f)
            size += os.path.getsize(fp)
            result = round((size / 1024 / 1024), 4)
            return result


def count_a():
    global count_avi
    count_avi += 1
    return count_avi


def count_d():
    global count_del
    count_del += 1
    return count_del
