import os, sys, shutil

dirName = ""

if (sys.platform == 'linux'):
    dirName = "./"
else if (sys.platform == 'win32'):
    dirName = "C:\Program Files"
    
for currentFolder, subFolders, files in os.walk(dirName):
    if (currentFolder == "DesMume"):
