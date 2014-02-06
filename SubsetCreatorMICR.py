import EPP
import string

fname = "SubsetsMICR.txt"
EPP.clearFile(fname)
toFile = "These are the test cases to run:\n"
EPP.writeToFile(fname, toFile)

MICRChars = "0123456789ABCD"
endSignal = ""
while endSignal != "0":
    word = ""
    words = []
    while word != 'E':
        word = str(input("Enter Acceptable Word in Subset(Enter E to end):")).upper()
        while not(EPP.checkWordInCharSet(word,MICRChars)) and word != 'E':
            word = str(input("Unacceptable characters please try again(Enter E to end):")).upper()
        if word != "E":
            words.append(word)

    subset = ""
    for word in words:
            for a in word:
                    if a not in subset:
                            subset += a
    toFile = '{"' + subset + '","",' + str(len(subset)) + ",'S',},\n"
    EPP.writeToFile(fname,toFile)
    EPP.readFromFile(fname)

    testWord = ""
    while testWord != "E":
            testWord = str(input("Enter word to test in Subset(Type E to end): ")).upper()
            while ((not(EPP.checkWordInCharSet(testWord,MICRChars))) or (not(EPP.testForOCRStringReqMICR(testWord)))) and testWord != 'E':
                testWord = str(input("Unacceptable characters please try again(Enter E to end):")).upper()
            passing  = True
            if testWord != 'E':
                    template = EPP.generateTemplate(testWord)
                    for a in testWord:
                        if a not in subset:
                                passing = False
                                break
                    if passing:
                            print(testWord + " Passed because its in the subset: " + subset)
                            toFile ='{"' + testWord + '","' + template + '", ' + str(len(testWord)) + ",'D',true},\n"
                            EPP.writeToFile(fname,toFile)
                    else:
                            print(testWord + " Failed")
                            toFile ='{"' + testWord + '","' + template + '", ' + str(len(testWord)) + ",'D',false},\n"
                            EPP.writeToFile(fname,toFile)
    endSignal = str(input("Do you want to end:(if yes type 0)"))
