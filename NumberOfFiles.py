import os
import sys

numberOfFiles = 0
print(os.path.dirname(__file__))
numberOfFiles +=  len([name for name in os.listdir(os.path.dirname(__file__)) if os.path.isfile(name)])
print("The number of files in this directory are: " + str(numberOfFiles))

