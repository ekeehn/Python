##import EPP
import string

f = open('Subsets.txt','w')
toFile = "These are the test cases to run:\n"
f.write(toFile)
f.close()

endSignal = ""

while endSignal != "0":
    f = open('Subsets.txt','a')
    word = ""
    words = []
    while word != '0':
        word = str(input("Enter Acceptable Word in Subset(Enter 0 to end):")).upper()
        if word != "0":
            words.append(word)

    subset = ""
    for word in words:
        for a in word:
            if a not in subset:
                subset += a
    toFile = '{"' + subset + '","",' + str(len(subset)) + ",'S',},\n"
    f.write(toFile)
    f.close()
    
    f = open('Subsets.txt','r')
    print(f.read())
    f.close()

    f = open('Subsets.txt', 'a')
    testWord = ""
    while testWord != "0":
        testWord = str(input("Enter word to test in Subset(Type 0 to end): ")).upper()
        passing  = True
        if testWord != '0':
            template = ""
            for a in testWord:
                if a in string.ascii_letters:
                    template += 'A'
                elif a in string.digits:
                    template += '9'
                else:
                    if a == '+':
                        template += '"+"'
                    else:
                        template += '+' + a + '+'
            for a in testWord:
                if a not in subset:
                    passing = False
                    break
            if passing:
                print(testWord + " Passed because its in the subset: " + subset)
                toFile ='{"' + testWord + '","' + template + '", ' + str(len(testWord)) + ",'D',true},\n"
                f.write(toFile)
            else:
                print(testWord + " Failed")
                toFile ='{"' + testWord + '","' + template + '", ' + str(len(testWord)) + ",'D',false},\n"
                f.write(toFile)
    f.close()
    endSignal = str(input("Do you want to end:(if yes type 0)"))
    
