import random


def quicksort(nums):
    """
    Модернизированная быстрая сортировка Хоара
    :param nums:
    :return:
    """
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
    l_nums = [n for n in nums if n < q]

    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]
    return quicksort(l_nums) + e_nums + quicksort(b_nums)


def findElement(nums, ch):
    """
    Поиск определенного элемента в списке
    :param nums:
    :param ch:
    :return:
    """
    return ch in nums


def findNumberMinElements(nums, num):
    """
    Ищет минимальное элементы в опеределенном кол-ве
    :param nums:
    :param num:
    :return:
    """
    temp = quicksort(nums)
    result = []
    for i in range(0, num):
        result.append(temp[i])
    return result


def findNumberMaxElements(nums, num):
    """
    Ищет максимальные элементы в опеределенном кол-ве
    :param nums:
    :param num:
    :return:
    """
    temp = quicksort(nums)
    temp.reverse()
    result = []
    for i in range(0, num):
        result.append(temp[i])
    return result


def average(nums):
    """
    Расчитывает среднее значение
    :param nums:
    :return: float average
    """
    return float(sum(nums)) / max(len(nums), 1)


def unique_elements(nums):
    """
    Преобразовыввает список в список уникальных элементов
    :param nums: список без уникальных элементом
    :return: уникальный список
    """
    return list(set(nums))


if __name__ == '__main__':
    spisok = []
    for i in range(random.randint(10, 20)):
        spisok.append(random.randint(0, 50))
    print("Сгенерированный список:", spisok)
    print("Быстрая сортировка:", quicksort(spisok))
    print("Поиск элемента @36@:", findElement(spisok, 36))
    print("Поиск 5 первых минимальных элементов:", findNumberMinElements(spisok, 5))
    print("Поиск 5 первых максимальных элементов:", findNumberMaxElements(spisok, 5))
    print("Среднее значение:", average(spisok))
    print("Список состоящий только из уникальных элементов:", unique_elements(spisok))
