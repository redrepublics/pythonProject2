
import os
import sys
import glob
folder = os.getcwd()
def folder_dir():
    for filename in os.listdir(folder):
        infilename = os.path.join(folder,filename)
        if not os.path.isfile(infilename):
            continue
        else:
            oldbase = os.path.splitext(filename)
            newname = infilename.replace('.txt', '.xml')
            output = os.rename(infilename, newname)


folder_dir()
