class Naming:

    def __init__(self, model, mark, year):
        self.model = model
        self.mark = mark
        self.year = year

    def __str__(self) -> str:
        return "({}, {}, {})".format(self.model, self.mark, self.year)

    def __repr__(self) -> str:
        return "Naming({}, {}, {})".format(self.model, self.mark, self.year)
