
import os
import sys
import glob
folder = 'E:'
for filename in os.listdir(folder):
       infilename = os.path.join(folder,filename)
       if not os.path.isfile(infilename):
           continue
       oldbase = os.path.splitext(filename)
       newname = infilename.replace('.xml', '.txt')
       output = os.rename(infilename, newname)

for f in glob.glob("E:\*.txt"):
    os.system("cat " + f + " >> OutFile.txt")