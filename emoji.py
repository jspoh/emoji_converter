# emoji converter with dictionary somewhat like what discord does(probably)

emoji_list= {
    ":)": "🙂",
    ":D": "😀",
    ":(": "🙁",
    "-_-": "😑",
    "._.": "😐"
}

running = True
while running:
    emoji_msg = ""
    msg = input("Input message: ").split()
    for i in msg:
        emoji_msg += emoji_list.get(i, i) + " "
    print(emoji_msg)
