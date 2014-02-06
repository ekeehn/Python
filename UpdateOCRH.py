import os, shutil

filename = "OCR.h"
rootDir = os.path.dirname(__file__)
srcFilePath = os.path.join(rootDir, filename)
print(rootDir)
for rootFolder , subFolders, files in os.walk(rootDir):
    for cFolder in subFolders:
        pathName = os.path.join(rootFolder, cFolder)
        dstFilePath = os.path.join(pathName, filename)
        if(os.path.exists(dstFilePath)):
           shutil.copyfile(srcFilePath,dstFilePath)
           print ("Copied File from " + srcFilePath + " to " + dstFilePath)

input("All Updates Complete Press enter to close")
