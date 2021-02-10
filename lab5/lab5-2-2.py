def prime(number):
    n = number
    counter = 0
    for i in range(1, n + 1):
        if n % i == 0:
            counter += 1
    return True if counter == 2 else False


if __name__ == '__main__':
    a = {i for i in range(8, 103)}
    print(type(a))
    print(a)
    x = set()
    y = set()
    z = set()
    for i in range(len(a)):
        temp = a.pop()
        if 8 <= temp <= 22:
            x.add(temp)
        if prime(temp):
            y.add(temp)
        else:
            z.add(temp)
    print("Множество x -", x)
    print("Множество y -", y)
    print("Множество z -", z)
