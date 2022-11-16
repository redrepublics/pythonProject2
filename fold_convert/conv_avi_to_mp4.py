import subprocess
import os
import sys


folder = os.getcwd()
vid = 'video'
src = os.path.join(folder, vid)
del_files = []


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
    convert_and_folder_search()
    for root, dirs, filenames in os.walk(src, topdown=False):
        for filename in filenames:
            if ".avi" in filename:
                input_file = os.path.join(root, filename)
                del_files.append(input_file)
                output_file = os.path.join(src, filename.replace(".avi", ".mp4"))
                subprocess.run(['ffmpeg', '-loglevel', 'quiet', '-y', '-i', input_file, output_file])
            else:
                pass
        for x in del_files:
            os.remove(x)


basic_conversion()