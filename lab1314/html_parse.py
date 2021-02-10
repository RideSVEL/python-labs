import requests as req
from bs4 import BeautifulSoup

from lab1314.vacancy import Vacancy


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
