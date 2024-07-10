class Vacancy:
    """Класс для описания вакансии"""
    name: str  # Название
    area: str  # Город
    salary: int  # Зарплата
    url: str  # Ссылка
    salary_currency: str

    def __init__(self, name, area, salary, url):
        self.name = name
        self.area = area
        self.__validate_salary(salary)
        self.url = url
        self.rename_currency()

    def __validate_salary(self, salary):
        """Формирование информации по зарплате"""
        if salary is None:
            self.salary_from = 0
            self.salary_to = 0
            self.salary_currency = "Нет валюты"
        else:
            self.salary_from = salary["from"] if salary["from"] else 0
            self.salary_to = salary["to"] if salary["to"] else 0
            self.salary_currency = salary['currency']

    def rename_currency(self):
        if self.salary_currency == "RUR":
            self.salary_currency = "Рублей"
        if self.salary_currency == "BYR":
            self.salary_currency = "Белорусских Рублей"
        if self.salary_currency == "KZT":
            self.salary_currency = "Тенге"

    def __lt__(self, other):
        return self.salary_from < other.salary_from

    def __str__(self):
        return (f"{self.name}\n"
                f"Город: {self.area['name']}\n"
                f"Зарплата от {self.salary_from} до {self.salary_to} {self.salary_currency}\n"
                f"Ссылка: {self.url}")
