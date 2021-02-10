import math


def countFunction(alpha):
    return math.cos(alpha) + math.cos(2 * alpha) + math.cos(6 * alpha) + math.cos(7 * alpha)


def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


def lcm(a, b):
    m = a * b
    return m // gcd(a, b)


if __name__ == '__main__':
    number = int(input('Введите значение для расчета функции: '))
    print("Получившийся результат: {}".format(countFunction(countFunction(number))))
    first = int(input('Введите первое значение для расчета НОД: '))
    second = int(input('Введите второе значение для расчета НОД: '))
    print("Получившийся результат для НОК: {}".format(gcd(first, second)))
    print("Получившийся результат для НОД: {}".format(lcm(first, second)))
