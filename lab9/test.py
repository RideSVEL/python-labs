import pickle

from lab9.bike import Bike
from lab9.naming import Naming

if __name__ == '__main__':
    bike = Bike(500, 4.5, "Green", 400, Naming("Trail", "Cannondale", 2015), 15)
    print(bike)
    print(bike.__repr__())
    print("Profit of production bike -", bike.profit_of_production())
    print("Profit of production bike -", bike.count_proceeds_by_month())
    print(bike.drive())
    try:
        with open("bike.pkl", "wb") as fp:
            pickle.dump(bike, fp)
        with open("bike.pkl", "rb") as fp:
            a = pickle.load(fp)
    except FileExistsError as e:
        print(e)
    print(a)
