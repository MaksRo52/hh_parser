from src.parser import HH


class WorkUser:
    def __init__(self):
        self.vacancy = []

    @staticmethod
    def get_vacancy():
        search_query = input("Введите поисковый запрос: ")
        key_hh = HH(search_query)
        return key_hh.load_vacancies()

    def get_top_n_for_salary(self):
        top_n = int(input("Введите количество вакансий для вывода в топ N: "))
        sort_by_salary = sorted(self.vacancy, key=lambda x: x.salary, reverse=True)
        return sort_by_salary[:top_n]
