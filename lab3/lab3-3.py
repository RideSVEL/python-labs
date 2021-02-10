def getDoubleWord(sentence):
    splitter = sentence.lower().replace(",", "").replace(".", "").split(" ")
    for i in range(0, len(splitter)):
        temp = splitter[i]
        for j in range(i+1, len(splitter)):
            if temp.__eq__(splitter[j]):
                return temp


if __name__ == '__main__':
    string = "Это тестовое предложение, которое содержит два раза слово это."
    print(getDoubleWord(string))
