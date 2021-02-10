import random

import numpy as np


def findMinInStolbec(spisok):
    indexes = []
    for i in range(0, len(spisok[0])):
        temp = np.array(spisok)
        indexes.append(min(list(temp[:, i])))
    index = indexes.index(min(indexes))
    return index


def findMinPositiveIndex(spisok, exclude):
    indexes = []
    for i in range(0, len(spisok[0])):
        if i == exclude:
            indexes.append(100)
            continue
        temp = np.array(spisok)
        temp_temp = []
        for j in list(temp[:, i]):
            if j > 0:
                temp_temp.append(j)
        indexes.append(min(temp_temp))
    index = indexes.index(min(indexes))
    return index


if __name__ == '__main__':
    print('Input n: ')
    n = int(input())
    print('Input m: ')
    m = int(input())
    my_list = [[random.randint(-10, 10) for i in range(n)] for j in range(m)]
    for row in my_list:
        print(row)
    print("=====================")
    index_stolbec1 = findMinInStolbec(my_list)
    index_stolbec2 = findMinPositiveIndex(my_list, index_stolbec1)
    print("Change stolbec with index {} on stolbec with index {}".format(index_stolbec1, index_stolbec2))
    print("=====================")
    temp = np.array(my_list)
    l1 = list(temp[:, index_stolbec1])
    l2 = list(temp[:, index_stolbec2])
    for i in range(0, len(my_list[0])):
        my_list[i][index_stolbec1] = l2[i]
        my_list[i][index_stolbec2] = l1[i]

    print('Изменённый список :')
    for i in range(0, n):
        print(my_list[i])
