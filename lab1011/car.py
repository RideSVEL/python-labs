import random
from abc import ABC

from lab1011.abstract.vehicle import Vehicle


class Car(Vehicle, ABC):
    count_of_rent_car = 0

    def __init__(self, cost, fuel, naming) -> None:
        super().__init__()
        self.cost = cost
        self.fuel = fuel
        self.naming = naming

    def __str__(self) -> str:
        return '({}, {}, {})'.format(self.cost, self.fuel, self.naming.__str__())

    def __repr__(self) -> str:
        return 'Car({}, {}, {})'.format(self.cost, self.fuel, self.naming.__repr__())

    @classmethod
    def get_rent_car(cls):
        cls.count_of_rent_car += 1
        return "You get a rent car for 1 day"

    @staticmethod
    def status():
        statuses = ["The car is cool", "Prosto pushka", "Edem daleko and nadolgo", "Pobeda vmesto obeda"]
        return statuses[random.randint(0, len(statuses))]

    def drive(self):
        return "I'm drive a car with %s fuel on 100km!" % self.fuel

    def production(self):
        pass
