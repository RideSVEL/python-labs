def findCentury(year=2021):
    """Метод для опрдеделения столетия по входящему году путем деление на 100"""
    temp = year / 100
    if temp // 1 == temp:
        return int(temp)
    else:
        return int((temp + 1) // 1)


if __name__ == '__main__':
    """Точка входа в программу.
    Получает с консоли год и выдает столетие, к которому оно относится"""
    input_year = int(input("Введите год для определения столетия: "))
    century = findCentury(input_year)
    if century > 0:
        print("Введенный год соответствует {} столетию".format(century))
    else:
        print("Введенный год соответствует {} столетию до нашей эры".format(century * -1))
