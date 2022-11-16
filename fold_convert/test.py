import subprocess
import os

folder = os.getcwd()
vid = 'video'
src = os.path.join(folder, vid)

for root, dirs, filenames in os.walk(src, topdown=False):
    for filename in filenames:
        if ".avi" in filename:
            inputfile = os.path.join(root, filename)
            outputfile = os.path.join(src, filename.replace(".avi", ".mp4"))
            subprocess.run(['ffmpeg', '-loglevel', 'quiet', '-y', '-i', inputfile, outputfile])
