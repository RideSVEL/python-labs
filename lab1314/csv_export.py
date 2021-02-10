import csv
import pandas as pd


class Exporter:
    @staticmethod
    def export_csv(vacancies, filename='export.csv'):
        with open(filename, mode="w", encoding="utf-8") as csvfile:
            names = ["Name", "Salary", "Description", "Company", "Area"]
            vacancy = csv.writer(csvfile, dialect='excel')
            vacancy.writerow(names)
            for i in vacancies:
                vacancy.writerow(
                    [i.name, i.salary, i.description, i.company,
                     i.area])
            csvfile.close()
