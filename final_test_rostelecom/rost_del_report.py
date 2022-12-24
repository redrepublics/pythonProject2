import glob
import os.path


def del_old_report():
    filelist = glob.glob(os.path.join(os.getcwd(), "*.png"))
    for f in filelist:
        os.remove(f)

