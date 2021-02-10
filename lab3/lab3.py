import random


def insertion_sort(array):
    length = len(array)
    for i in range(1, length):
        key = array[i]
        j = i
        while (j - 1 >= 0) and (array[j - 1] > key):
            array[j - 1], array[j] = array[j], array[j - 1]
            j = j - 1
        array[j] = key


if __name__ == '__main__':
    number = int(input('Введите количество значений для списка: '))
    randomListA = []
    randomListB = []
    for i in range(0, number):
        randomListA.append(random.randint(-60, 60))
        randomListB.append(random.randint(0, 50))
    print('Список А - ', randomListA)
    print('Список Б - ', randomListB)
    insertion_sort(randomListA)
    print('Отсортированый список А - ', randomListA)
