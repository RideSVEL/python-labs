import pickle

from lab12.car import Car
from lab12.contextManager import file_open
from lab12.excepcitons.ClassException import ClassNotFoundException
from lab12.iterator.iterator import CarAssembler
from lab12.naming import Naming

if __name__ == '__main__':
    try:
        car = Car(8600, 14.7, Naming("Daewoo", "Lanos", 2006))
        number = int(input("Введите необходимое кол-во лет для сборки машины: "))
        cars = car.generate_cars(number)
        print(type(cars))
        print(cars)
        spisok = []
        for i in cars:  # заполняем список с помощью генератора класса
            spisok.append(i)
        car_assembler = CarAssembler(spisok)
        print(car_assembler)
        for i in car_assembler:
            print(i)
        with file_open("car.pkl", "wb") as fp:
            pickle.dump(spisok, fp)
        with file_open("car.pkl", "rb") as fp:
            a = pickle.load(fp)
        print(a)
    except ClassNotFoundException as e:
        print(e)
