import random


def firstCheck(dictionary):
    get = dictionary.get(1)
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
    print(average)
    return counter


def fourthsCheck(dictionary):
    summa = 0
    summa2 = 0
    lists = list(dictionary.values())
    keys = list(dictionary.keys())
    for i in range(0, len(keys)):
        summa2 += keys[i]
    for i in range(0, len(lists)):
        summa += lists[i]
    average = summa / summa2

    for i in range(len(keys)):
        if abs(dictionary.get(keys[i]) / keys[i] - average) <= 0.5:
            return dictionary.get(keys[i])


if __name__ == '__main__':
    number = 10
    dicts = {}
    for i in range(0, number):
        dicts[random.randint(1, 20)] = int(random.randint(1, 50) * 1.5)
    print(dicts)
    items = dicts.values()
    print(items)
    list1 = list(dicts.keys())
    list1.sort()
    print("Чи є хоч один пасажир, багаж якого складається з однієї речі вагою менше 25 кг - ", firstCheck(dicts))
    print("Кількість пасажирів, які мають більше двох речей -", secondCheck(list1))
    print("Число пасажирів, кількість речей яких перевершуєсереднє число речей всіх пасажирів -", thirdCheck(list1))
    print("Номер багажу, в якому середня вагаод нієї речі відрізняється від загальної середньої ваги однієї речі не "
          "більше ніжна 0,5 кг", fourthsCheck(dicts))
