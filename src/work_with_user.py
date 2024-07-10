from src.parser import HH


class WorkUser:
    def __init__(self, vacancies):
        self.vacancies = vacancies

    @staticmethod
    def get_vacancy():
        search_query = input("Введите поисковый запрос: ")
        key_hh = HH(search_query)
        return key_hh.load_vacancies()

    def get_top_n_for_salary(self):
        """Вывод топ вакансий"""
        top_n = int(input("Введите количество вакансий для вывода в топ N: "))
        sort_by_salary = sorted(self.vacancies, reverse=True)
        self.vacancies = sort_by_salary[:top_n]


    def print_vacancies(self):
        """Перечисление списка вакансий"""
        for vacancy in self.vacancies:
            print(vacancy)
            print('-' * 50)

    def filter_name(self):
        """Отбор по ключевому слову"""
        value = input("Введите ключевое слово для поиска: ")
        self.vacancies = [vacancy for vacancy in self.vacancies if value in vacancy.name]