import random


def firstCheck(dictionary):
    for i in range(0, len(dictionary)):
        get = dictionary[i].get(1)
        if get is not None and get < 25:
            return True
    return False


def secondCheck(lists):
    counter = 0
    for i in range(0, len(lists)):
        if lists[i] > 2:
            counter += 1
    return counter


def thirdCheck(lists):
    counter = 0
    summa = 0
    for i in range(0, len(lists)):
        summa += lists[i]
    average = summa / len(lists)
    for i in range(0, len(lists)):
        if average < lists[i]:
            counter += 1
    return counter


def fourthsCheck(lists, keys):
    summa = 0
    summa2 = 0
    for i in range(0, len(keys)):
        summa2 += keys[i]
        summa += lists[i]
    average = summa / summa2
    for i in range(len(keys)):
        if abs(lists[i] / keys[i] - average) <= 0.5:
            return i


def generateElement():
    return {random.randint(1, 20): int(random.randint(1, 50) * 1.5)}


if __name__ == '__main__':
    number = 10
    dicts = []
    for i in range(0, number):
        dicts.append(generateElement())
    print(dicts)
    items = []
    for i in range(0, len(dicts)):
        items.append(list(dicts[i].values())[0])
    print("Вес багажа: ", items)
    list1 = []
    for i in range(0, len(dicts)):
        list1.append(list(dicts[i].keys())[0])
    print("Количество багажа: ", list1)
    list2 = list1
    list2.sort()
    print("Отсортированное количество багажа: ", list2)
    print("Чи є хоч один пасажир, багаж якого складається з однієї речі вагою менше 25 кг - ", firstCheck(dicts))
    print("Кількість пасажирів, які мають більше двох речей -", secondCheck(list1))
    print("Число пасажирів, кількість речей яких перевершуєсереднє число речей всіх пасажирів -", thirdCheck(list1))
    print("Номер багажу, в якому середня вагаод нієї речі відрізняється від загальної середньої ваги однієї речі не "
          "більше ніжна 0,5 кг", fourthsCheck(items, list1))
