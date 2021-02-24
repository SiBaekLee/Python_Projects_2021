def Exit() :
    while True :
        exit = str(input("Process finished. Press X to exit."))
        if exit == "X" or exit == "x":
            break

def Keyerror() :
    print("=" * 50)
    print("Error occured.\nMake sure that you have written letters or numbers correctly as required.")
    print("=" * 50)

def Encrypt() :
    try:
        secondList = list(raw)

        z = list()
        for i in secondList:
            z.append(library[i])

        result = "".join(z)
        print(result)

    except KeyError:
        Keyerror()

def Decrypt() :
    try:
        secondList = list(raw)

        z = list()
        b = 0
        semiList = []
        rangeEnd = int(len(secondList) / 2)
        for a in range(0, rangeEnd) :
            if len(secondList) % 2 == 1 :
                print("Some characters not exist.")
                raise Exception
            if b % 2 == 1 :
                b += 1
            sum = secondList[b] + secondList[b + 1]
            semiList.append(sum)
            b += 1

        for i in semiList :
            z.append(library[i])

        result = "".join(z)
        print(result)

    except Exception as a :
        Keyerror()

def invertlibrary(obj):
    return {value: key for key, value in obj.items()}
library = {"0": "dz", "1": "xq", "2": "in", "3": "tp", "4": "ui", "5": "zm", "6": "ke", "7": "px", "8": "qb", "9": "nr",
            "!" : "aw", "@" : "bj", "#" : "cn", "$" : "em", "%" : "fb", "^" : "gv", "&" : "hf", "*" : "jh", "(" : "ml",
            ")" : "sy", "_" : "vu", "+" : "wa", "~" : "ye", "/" : "lc", "-" : "oz", "=" : "rx",
           "a" : "zt", "b" : "kp", "c" : "mn", "d" : "it", "e" : "re", "f" : "ob" }

print("=" * 60)
print("Encrypter and Decrypter. by leeseeback. version 5.0")
print("=" * 60)

selection = ""
notice = 0
while selection != "E" and selection != "e" and selection != "D" and selection != "d" :
    if notice > 0 :
        print("Error command. Retry.")
    selection = str(input("choose type (E)ncrypt / (D)ecrypt : "))
    notice += 1

if selection == "E" or selection == "e" :
    raw = str(input("number and marks (Some Unsupported) \n --> "))
    Encrypt()
    Exit()

elif selection == "D" or selection == "d" :
    library = invertlibrary(library)
    raw = str(input("word"
                    "\n -->"))
    Decrypt()
    Exit()
