import json
import sys
from concurrent.futures.thread import ThreadPoolExecutor
from time import sleep

import requests

import csv
import pandas as pd

import requests as req
from bs4 import BeautifulSoup


class HtmlParser:
    @staticmethod
    def parse_hot_vacancy():
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
        }
        resp = req.get("https://jobs.ua/vacancy/hot", headers=headers)
        soup = BeautifulSoup(resp.text, 'lxml')
        spisok = []
        find_all = soup.find_all("li", class_="is_choose_me")
        for i in find_all:
            name = i.find("a", class_="b-vacancy__top__title").text
            salary = i.find("span", class_="b-vacancy__top__pay").text.replace(" ", "").replace(" ", "").replace("грн.",
                                                                                                                 "")
            company = i.find("span", class_="link__hidden").text
            area = i.find("a", class_="link__hidden").text
            description = i.find("p").text
            vacancy = Vacancy(name, salary, description, company, area)
            spisok.append(vacancy)
            # print(vacancy)
        return spisok


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


class JsonParser:

    @staticmethod
    def get_vacancy_from_json_object(vacancy):
        try:
            salary = vacancy["salary"]["from"]
        except TypeError as e:
            salary = "Не указана"
        name = vacancy["name"]
        responsibility = vacancy["snippet"]["responsibility"]
        company = vacancy["employer"]["name"]
        area = vacancy["area"]["name"]
        return Vacancy(name, salary, responsibility, company, area)

    @staticmethod
    def parse_vacancies_list(json):
        get = json.get('items')
        vacancyList = []
        for vacancy in get:
            vacancyList.append(JsonParser.get_vacancy_from_json_object(vacancy))
        return vacancyList


def getPage(search, page=0):
    # Справочник для параметров GET-запроса
    params = {
        'text': 'NAME:' + search,
        'page': page,  # Индекс страницы поиска на HH / ПАГИНАЦИЯ
        'per_page': 50  # Кол-во вакансий на 1 странице
    }
    req = requests.get('https://api.hh.ru/vacancies/', params)  # Посылаем запрос к API
    data = req.content.decode()  # Декодируем его ответ, чтобы Кириллица отображалась корректно
    req.close()
    return data


if __name__ == '__main__':
        jsObj = json.loads(getPage(sys.argv[1]))

        with ThreadPoolExecutor(max_workers=2) as executor:
            future = executor.submit(JsonParser.parse_vacancies_list, jsObj)
            future2 = executor.submit(HtmlParser.parse_hot_vacancy)
            vacancies_list = future.result()
            hot_vacancy = future2.result()
        Exporter.export_csv(vacancies_list)
        print("Первый файл экспортирован")
        Exporter.export_csv(hot_vacancy, 'export2.csv')
        print("Второй файл экспортирован")
