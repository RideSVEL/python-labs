from lab1314.vacancy import Vacancy


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
