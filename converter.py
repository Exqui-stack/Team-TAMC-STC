if __name__ == "__main__":
    text = input("> ")
    words = text.split( " " )
    emojis={
        "grin" : "😁",
        "wink" : "😉",
        "laughing" : "😆",
    }
    result = " "
    for word in words:
        result += emojis.get(word, word) + " "
        print(result)
    

    