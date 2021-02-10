import random


def createTwoArray(n, m, first, second, floats):
    randomGenerate = []
    for i in range(0, n):
        temp = []
        if floats:
            for j in range(0, m):
                temp.append(random.uniform(first, second))
        else:
            for j in range(0, m):
                temp.append(random.randint(first, second))
        randomGenerate.append(temp)
    return randomGenerate


def checkFirstIf(inputList):
    indexes = []
    for i in range(1, len(inputList) - 1):
        temp = inputList[i]
        firstCheck = True
        for j in range(0, i):
            if temp < inputList[j]:
                firstCheck = False
        secondCheck = False
        if firstCheck:
            secondCheck = True
            for j in range(i + 1, len(inputList)):
                if temp > inputList[j]:
                    secondCheck = False
        if secondCheck:
            indexes.append(i)
    return indexes


def checkSecondIf(inputList):
    counter = 0
    for i in range(0, len(inputList)):
        indexes = checkFirstIf(inputList[i])
        print(indexes)
        if len(indexes) > 0:
            for j in range(0, len(indexes)):
                temp = indexes[j]
                candidat = inputList[i][temp]
                sumAnotherElement = 0
                for k in range(0, len(inputList)):
                    sumAnotherElement += inputList[k][temp]
                sumAnotherElement -= candidat
                if candidat > sumAnotherElement:
                    counter += 1
    return counter


if __name__ == '__main__':
    nn = int(input('Введите n значений для списка: '))
    mm = int(input('Введите m значений для списка: '))
    randomList = createTwoArray(nn, mm, -10, 11, False)
    tempList = createTwoArray(nn, mm, 0, 20, False)
    print("Сгенерированная матрица а")
    for i in range(0, len(randomList)):
        print(randomList[i])
    print("Сгенерированная матрица б")
    for i in range(0, len(tempList)):
        print(tempList[i])
    tempList = createTwoArray(nn, mm, 0, 20, True)
    print("Сгенерированная матрица в")
    for i in range(0, len(tempList)):
        print(tempList[i])
    print("\n")

    print(checkSecondIf(randomList))
