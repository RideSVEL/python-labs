class Vacancy:

    def __init__(self, name, salary, description, company, area):
        self.name = name
        self.salary = salary
        self.description = description
        self.company = company
        self.area = area

    def __str__(self) -> str:
        return "Name - {}\n" \
               "Salary - {}\n" \
               "Description - {}\n" \
               "Company - {}\n" \
               "Area - {}\n".format(self.name, self.salary, self.description, self.company, self.area)

    def __repr__(self) -> str:
        return "\nVacancy(Name - {}\n" \
               "Salary - {}\n" \
               "Description - {}\n" \
               "Company - {}\n" \
               "Area - {})\n".format(self.name, self.salary, self.description, self.company, self.area)
