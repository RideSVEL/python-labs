import json
from concurrent.futures.thread import ThreadPoolExecutor
from time import sleep

import requests

from lab1314.csv_export import Exporter
from lab1314.html_parse import HtmlParser
from lab1314.jsonparser import JsonParser


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
    while True:
        s = input("Введите вакансию для поиска: ")
        jsObj = json.loads(getPage(s))

        with ThreadPoolExecutor(max_workers=2) as executor:
            future = executor.submit(JsonParser.parse_vacancies_list, jsObj)
            future2 = executor.submit(HtmlParser.parse_hot_vacancy)
            vacancies_list = future.result()
            hot_vacancy = future2.result()
        Exporter.export_csv(vacancies_list)
        print("Первый файл экспортирован")
        Exporter.export_csv(hot_vacancy, 'export2.csv')
        print("Второй файл экспортирован")
        sleep(10)
