import os

folder = os.getcwd()
vid = 'video'
src = os.path.join(folder, vid)


# assign folder path

def size_fold():
    size = 0
    # get size
    for path, dirs, files in os.walk(src):
        for f in files:
            fp = os.path.join(path, f)
            size += os.path.getsize(fp)
        return size



