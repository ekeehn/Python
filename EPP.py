import string
import os
import shutil

## Write a string text to a file given by the name fname
def writeToFile(fname, text):
    f = open(fname, 'a')
    f.write(str(text))
    f.close()

## Read data from a file called fname starting from the byte given by seekTo	
def readFromFile(fname,seekTo=0):
    f = open(fname, 'r')
    print(f.read(seekTo))
    f.close()

## Create an OCR template from the parameter "text"
def generateTemplate(text):
    template = ""
    for a in text:
        if a in string.ascii_letters:
            template += 'A'
        elif a in string.digits:
            template += '9'
        else:
            if a == '+':
                template += '"+"'
            else:
                template += '+' + a + '+'
    return template
	
def checkWordInCharSet(word, charSet):
    passing = True
    for a in word:
        if a not in charSet:
            passing = False
            break
    return passing

def clearFile (fname):
    f = open(fname,'w')
    f.close()

def testForOCRStringReq(word):
    passing = True
    oneSpecial = False
    numSpecials = 0
    b = ''
    for a in word:
        if a not in string.ascii_letters and a not in string.digits and oneSpecial:
            passing = False
            numSpecials += 1
            print("Word Fails Requirements Due to multiple concequtive")
            break
        elif a not in string.ascii_letters and a not in string.digits:
            oneSpecial = True
            numSpecials += 1
        else:
            oneSpecial = False

    if (numSpecials / len(word)) >= 0.25:
        passing = False
        print("Word failed Requirements Due to more the 25% of word is special characters")

    return passing

def testForOCRStringReqMICR(word):
    passing = True
    oneSpecial = False
    numSpecials = 0
    b = ''

    if len(word) < 5: print("Warning: Test word is less than 5 characters")
    for a in word:
        if a not in string.digits and oneSpecial:
            passing = False
            numSpecials += 1
            print("Word Fails Requirements Due to multiple concequtive")
            break
        elif a not in string.digits:
            oneSpecial = True
            numSpecials += 1
        else:
            oneSpecial = False

    if (numSpecials / len(word)) >= 0.25:
        passing = False
        print("Word failed Requirements Due to more the 25% of word is special characters")

    return passing

## Prints the number of files in the passed in directory
def numberOfFilesInDir(path):
    numberOfFiles = 0
    numberOfFiles +=  len([name for name in os.listdir(os.path.dirname(__file__)) if os.path.isfile(name)])
    print("The number of files in " + path +" are: " + str(numberOfFiles))


## Updates all copies of the file given by fileName in all Subfolders of the rootPath
def recursiveUpdate(rootPath, fileName):
    filename = fileName
    rootDir = rootPath
    srcFilePath = os.path.join(rootDir, filename)
    for rootFolder , subFolders, files in os.walk(rootDir):
        for cFolder in subFolders:
            pathName = os.path.join(rootFolder, cFolder)
            dstFilePath = os.path.join(pathName, filename)
            if(os.path.exists(dstFilePath)):
               shutil.copyfile(srcFilePath,dstFilePath)
               print ("Copied File from " + srcFilePath + " to " + dstFilePath)

    input("All Updates Complete Press enter to close")

## Generate Passwords that include specific words, numbers, and special characters
def passwordGenerator (words, numbers, specials):
    for word in words:
        ## First print the word itself
        pword = word
        print (pword)
        ## Then print the word + all the numbers in the list
        for num in numbers:
            pword += num
            print (pword)
        ## Then print the word + each induvidual number in the list of numbers
        pword = word
        for num in numbers:
            print (pword + num)
        for num in numbers:
            for num2 in numbers:
                pword += num
            print(pword)
            pword = word
            for spec in specials:
                print (pword + num + spec)
            pword = word
        for spec in specials:
            pword += spec
            print (pword)
            for num in numbers:
                print (pword + num)
            pword = word
        for word2 in words:
            if (word != word2):
                pword += word2
            for num in numbers:
                pword += num
            for spec in specials:
                pword += spec
            print(pword)
            pword = word

## Generate Passwords that include specific words, numbers, and special characters
def passwordGenerator2 (words, numbers, specials, filename):
    f = open(filename, 'a')
    for current in words:
        pwrds = []
        print(current)
        f.write(current + "\n")
        pword = current
        for word in words:
            if word != current:
                pword += word
                pwrds.append(pword)
                print (pword)        
                f.write(pword + "\n")
        pword = ""
        for word in pwrds[:]:
            for num in numbers:
                word += num
                print (word)
                f.write(word + "\n")
        for word in pwrds[:]:
            for spec in specials:
                word += spec
                print (word)
                f.write(word + "\n")
    f.close()

def fileSaver (filename):
	rootDir = os.path.dirname(__file__)
	srcFilePath = os.path.join(rootDir, filename)
	print(rootDir)
	for subFolders, files in os.walk(rootDir):
		for cFolder in subFolders:
			pathName = os.path.join(rootFolder, cFolder)
			dstFilePath = os.path.join(pathName, filename)
			if(os.path.exists(dstFilePath)):
			   shutil.copyfile(srcFilePath,dstFilePath)
			   print ("Copied File from " + srcFilePath + " to " + dstFilePath)

	input("All Updates Complete Press enter to close")
            
            
            

        



