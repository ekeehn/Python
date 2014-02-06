import EPP

print("Enter words to be used for password generator:(Type STOP to end)")
inString = str(input())
words = []
while inString != "STOP":
    words.append(inString)
    inString = str(input())
print("Enter numbers to be used for password generator:(Type STOP to end)")
inString = input()
numbers = []
while inString != "STOP":
    numbers.append(inString)
    inString = input()
print("Enter specials to be used for password generator:(Type STOP to end)")
inString = input()
specials = []
while inString != "STOP":
    specials.append(inString)
    inString = input()
print ("The possible passwords are:")
EPP.passwordGenerator(words, numbers, specials)
input("Press enter to end")
