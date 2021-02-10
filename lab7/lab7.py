import random
import time
from functools import wraps

registered = []


def decorator(func):
    @wraps(func)
    def register(*args, **kwargs):
        func(*args, **kwargs)
        if hasattr(func, '__wrapped__'):
            registered.append(func.__name__)

    return register


def executes(func):
    @wraps(func)
    def get_time(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        finish = time.time() - start
        print("Time to execute - ", finish)

    return get_time


def success(func):
    @wraps(func)
    def while_not_success(*args, **kwargs):
        while True:
            try:
                print("Попытка выполнить функцию...")
                func(*args, **kwargs)
                break
            except IndexError as e:
                print("Ошибка выполнения, необходимо осуществить повторное выполнение...")
                pass
        print("Успешное выполнение функции!")

    return while_not_success


@decorator
@executes
def random_numbers(number):
    """
    Фнкция печатает рандомные числа в консоль, в количестве указанном в аргументах
    :param number:
    :return:
    """
    for i in range(number):
        time.sleep(0.3)
        print(random.randint(0, 50))


@decorator
def list_random_numbers(number):
    """
    Функция выдает список рандомных чисел, на основе аргумента
    :param number:
    :return:
    """
    spisok = []
    for i in range(number):
        time.sleep(0.3)
        spisok.append(random.randint(0, 50))
    print(spisok)


@decorator
@success
def difference():
    """
    Функция возвращает тру или фолс из определенного результата рандома
    :return:
    """
    temp = random.randint(0, 50)
    if temp > 20:
        print("Функция отработала успешно!")
    else:
        raise IndexError("Не успешное выполнение")


list_random_numbers = executes(list_random_numbers)

if __name__ == '__main__':
    print(random_numbers.__name__)
    num = int(input("Введите нужное количество чисел: "))
    random_numbers(num)
    list_random_numbers(num)
    difference()
    print(registered)
