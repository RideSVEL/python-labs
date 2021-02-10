import random

if __name__ == '__main__':
    a = {random.randint(10, 30) for i in range(random.randint(10, 20))}
    symbol = int(input("Введите символ Х - "))
    print("Первое множество А -", a)
    b = a
    if b.__contains__(symbol):
        b.remove(symbol)
    else:
        b.add(symbol)
    print("Множество B -", b)
