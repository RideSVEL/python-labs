from lab1011.bike import Bike
from lab1011.car import Car
from lab1011.excepcitons.ClassException import ClassNotFoundException
from lab1011.naming import Naming

if __name__ == '__main__':
    try:
        bike = Bike(500, 4.5, "Green", 400, Naming("Trail", "Cannondale", 2015), 15)
        print(bike)
        print(bike.__repr__())
        print("Profit of production bike -", bike.production())
        print(bike.drive())
        car = Car(8600, 14.7, Naming("Daewoo", "Lanos", 2006))
        print(car)
        print(Car.status())  # static method
        print(Car.get_rent_car())  # class method
        print(Car.count_of_rent_car)  # class variable
        for i in range(0, 10):
            print(Car.get_rent_car())  # class method
        print(Car.count_of_rent_car)  # class variable
        print(car.drive())
        print(car.production())
    except ClassNotFoundException as e:
        print(e)
