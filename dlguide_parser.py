import os
import sys
from downloader import Downloader

root_path = os.getcwd()
f = open(sys.argv[1], "r")
subfolder_path = ''
subsubfolder_path = ''

def reset_loc():
    os.chdir(root_path)

def setdir(folder_name):
    os.mkdir(folder_name)
    os.chdir(folder_name)

for line in f:
    if line[0] == '#':
        reset_loc()
        setdir(line[1:-1])
        subfolder_path = os.getcwd()
    elif line[0] == ';':
        os.chdir(subfolder_path)
        setdir(line[1:-1])
        subsubfolder_path = os.getcwd()
    else:
        d = Downloader(line)
        d.download_vid()
        print('File downloaded :-)')

f.close()
print('All files downloaded :-D')