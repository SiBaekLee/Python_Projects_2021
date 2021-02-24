def community() :
    import webbrowser as wb
    print("=" * 50)
    try:
        recentpage = open("RECENT SEARCH by Athena.txt", 'r')
    except FileNotFoundError:
        recentpage = open("RECENT SEARCH by Athena.txt", 'x')
        recentpage.close()

    recentpage = open("RECENT SEARCH by Athena.txt", 'r')
    contents = recentpage.read()
    print("###RECENT SEARCH : ", contents)
    recentpage.close()

    query = input("Enter query : ")

    while True:
        selectpage = input("Select webpage(s) [using number, no spaces or marks] : \n"
                       " 1. google\n 2. youtube\n 3. naver\n 4. duckduckgo\n -->")

        if selectpage == "" :
            print("None key. Cannot process searching.")
            break
        else:
            inputlist = list(selectpage)

            webpagematch = {"1": "https://www.google.com/search?ei=ZhkdYNGQKonm-AbjkpKoBg&q=",
                            "2": "https://www.youtube.com/results?search_query=",
                            "3": "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=",
                            "4" : "https://duckduckgo.com/?q="}
            try:
                for i in inputlist:
                    keyerrorTester = webpagematch[i]
            except KeyError:
                print("Not key in list. Cannot process searching.")
                break

            for i in inputlist:
                wb.open_new(webpagematch[i] + query)

            recentpage = open("RECENT SEARCH by Athena.txt", 'a')
            recentpage.write("\n" + query)
            recentpage.close()

            print("Process finished.")
            break


print("=" * 50)
print("Athena assistant. by leeseeback. version 3.4")

while True:
    print("=" * 50)
    print("### Welcome to Web assistant Athena.\n### Select you want to do\n")
    print("1. Search in multiple websites\n2. NOT YET\n3. Exit")

    commandCommunity = ["1", "Web", "web", "WEB", "internet", "Internet"]
    commandExit = ["3", "X", "x", "exit", "Exit", "EXIT", "goodbye", "bye"]
    commandFull = commandCommunity + commandExit

    command = input("-->")
    while command not in commandFull:
        command = input("This option is not include your input.\n-->")

    if command in commandCommunity:
        community()
    if command in commandExit :
        break