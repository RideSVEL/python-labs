def check(string, ch):
    if not string:
        return 0
    elif string[0] == ch:
        return 1 + check(string[1:], ch)
    else:
        return check(string[1:], ch)


if __name__ == '__main__':
    sentence = "Тестовое предложение, которое содержит какие то интересные слова."
    splitter = sentence.lower().replace(",", "").replace(".", "").replace(" ", "")
    print(splitter)
    for i in range(0, len(splitter)):
        if check(sentence, splitter[i]) == 1:
            print(splitter[i])
