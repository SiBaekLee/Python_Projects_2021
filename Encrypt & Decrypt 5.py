def Exit() :
    while True :
        exit = str(input("Process finished. Press X to exit."))
        if exit == "X" or exit == "x":
            break

def Keyerror() :
    print("=" * 50)
    print("Error occured.\nMake sure that you have written letters or numbers correctly as required.")
    print("=" * 50)

def Encrypt() :    #함수에 인수 넣는 방식으로 // 가독성을 위해
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
        for a in range(0, rangeEnd) :        # for 핵심용도는 c와 좀 다르다. 이렇게 쓰면 절대 안된다. range는 세번째값이 있다. 그것은 간격. 그러면 저렇게 복잡하게 안해도 된다. 파이선에서는 인덱스를 반복문을 통해 접근할 필요가 없다.
                                             # collection 이용하면 된다. 컬렉션 값을 바꾸지 않는 것이 좋다. 절차지향은 가독성이 처음에는 어쩔 수 없음... 절차지향보다는 객체가
                                             # 파이선은 자료형 다루는 데 특화되어 있다. 자료 삭제추가 등등에 특화. 최종적으로 원하는 출력의 자료 형태를 그대로 따라가는 것이 좋음. 무슨말이냐면 마지막부분이
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
    return {value: key for key, value in obj.items()}    #사실 인터넷에서 찾아서 보고 함 // 이것의 존재는 딕셔너리 컴프리헨션, items() 는 키와 값을 묶어서 한번에 보낸다.(쌍을 뽑아낸다)

library = {"0": "dz", "1": "xq", "2": "in", "3": "tp", "4": "ui", "5": "zm", "6": "ke", "7": "px", "8": "qb", "9": "nr",
            "!" : "aw", "@" : "bj", "#" : "cn", "$" : "em", "%" : "fb", "^" : "gv", "&" : "hf", "*" : "jh", "(" : "ml",
            ")" : "sy", "_" : "vu", "+" : "wa", "~" : "ye", "/" : "lc", "-" : "oz", "=" : "rx",
           "a" : "zt", "b" : "kp", "c" : "mn", "d" : "it", "e" : "re", "f" : "ob" }

print("=" * 60)
print("Encrypter and Decrypter. by leeseeback. version 5.0")
print("=" * 60)

selection = ""
notice = 0
while selection != "E" and selection != "e" and selection != "D" and selection != "d" :    #in  a in b-> a가 b 안에 있는지 알아본다. 리스트에 넣어서 리스트에 있는지 확인하는 방법
    if notice > 0 :
        print("Error command. Retry.")
    selection = str(input("choose type (E)ncrypt / (D)ecrypt : "))       # str 굳이 안써도 됨. input로 받는 거는 다 문자열임.
    notice += 1                 #notice 부분은 변수가 딱히 필요가 없다. 사실 c언어에는 do while 함수가 있었음. 실행 후 평가 순서. 파이선에는 이런게 없음.

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

    """
    upper : 모든 글자 대문자
    low : 모든 글자 소문자
    
    입력을 함수로 따로 하여 정형화하는 것이 좋음.
    
    같은 코드를 중복해서 작성하지 않는다. 가독성.
    if에서 else는 안빠지는게 나음. 가독성.
    Exit() 와 같은 거는 코드의 반복이므로 마지막으로 빼도 됨.
    
    while for 반복문은 쓰임이 다르다.
    while : 조건이 참이면 실행
    for : 
    모든 방면에서 최대한 방법을 줄이고 겹치는 것은 싹 다 없애고.
    최대한 짧게 (가독성은 보장하는 내에서)
    더 나아가서 배운다면 코드를 줄이면서 원하는 거를 뽑아내게.
    """