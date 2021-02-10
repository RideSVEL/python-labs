class Bike:

    def __init__(self, cost, popularity, color, cost_production, naming, count_of_sell_in_month):
        self.cost = cost
        self.popularity = popularity
        self.color = color
        self.cost_production = cost_production
        self.naming = naming  # Композиция
        self.count_of_sell_in_month = count_of_sell_in_month

    def profit_of_production(self):
        """
        Получить прибыль от производства
        :return:
        """
        return int(self.cost - self.cost_production)

    def drive(self):
        """
        Ride a bike
        """
        return "I'm ride a bike with %s color and cost %s some $!" % (self.color, self.cost)

    def count_proceeds_by_month(self):
        return self.profit_of_production() * self.count_of_sell_in_month

    def __getstate__(self) -> dict:  # Как мы будем "сохранять" класс
        state = {"cost": self.cost, "popularity": self.popularity, "color": self.color,
                 "cost_production": self.cost_production, "naming": self.naming}
        return state

    def __setstate__(self, state: dict):  # Как мы будем восстанавливать класс из байтов
        self.cost = state["cost"]
        self.popularity = state["popularity"]
        self.color = state["color"]
        self.cost_production = state["cost_production"]
        self.naming = state["naming"]

    def __repr__(self) -> str:
        return 'Bike({}, {}, {}, {})'.format(self.cost, self.popularity, self.color, self.naming.__repr__())

    def __str__(self) -> str:
        return '({}, {}, {}, {})'.format(self.cost, self.popularity, self.color, self.naming.__str__())
