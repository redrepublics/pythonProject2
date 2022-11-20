import os

folder = os.getcwd()
vid = 'video'
src = os.path.join(folder, vid)


def size_fold():
    size = 0
    for path, dirs, files in os.walk(src):
        for f in files:
            fp = os.path.join(path, f)
            size += os.path.getsize(fp)
        return size





print(size_fold())
print(type(size_fold()))
def res_res():
    x = round((size_fold()/1024/1024), 4)
    return x
print(res_res())