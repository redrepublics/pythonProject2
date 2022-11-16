import subprocess
import os
import sys

"""Используем декодер ffmpeg
Все делаем из корня АСПО, папка VIDEO должна присутствовать"""

folder = os.getcwd()
vid = 'video'
src = os.path.join(folder, vid)


def converty_avi_to_mpg():
    is_folder_video = os.path.exists(src)
    if is_folder_video:
        print('folder video - ok')
        is_conv = os.path.exists(os.path.join(folder, 'ffmpeg.exe'))
        if is_conv:
            print('converter - ok')
            pass
        else:
            sys.exit(0)
    else:
        sys.exit(0)


converty_avi_to_mpg()
for root, dirs, filenames in os.walk(src, topdown=False):
    for filename in filenames:
        if ".avi" in filename:
            inputfile = os.path.join(root, filename)
            print(inputfile)
            outputfile = os.path.join(src, filename.replace(".avi", ".mp4"))
            subprocess.run(['ffmpeg', '-loglevel', 'quiet', '-y' '-i', inputfile, outputfile])
        else:
            pass

for rootdir, dirs, files in os.walk(src):
    for file in files:
        if ((file.split('.')[-1]) == 'avi'):
            print(os.path.join(rootdir, file))
