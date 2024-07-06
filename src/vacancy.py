class Vacancy:
    """Класс для описания вакансии"""
    name: str  # Название
    area: str  # Город
    salary: int  # Зарплата
    url: str  # Ссылка

    def __init__(self, name, description, salary, url):
        self.name = name
        self.description = description
        self.salary = salary
        self.url = url

    def __str__(self):
        return (f"{self.name}\n"
                f"Город: {self.area}\n"
                f"Зарплата: {self.salary if self.salary else 'Зарплата не указана'}\n"
                f"Ссылка: {self.url}")

    @classmethod
    def new_vacancy(cls, vacancy):
        name = vacancy.get("name")
        area = vacancy.get("area").get("name")
        if vacancy.get("salary"):
            if vacancy.get("salary").get("from"):
                salary = int(vacancy.get("salary").get("from"))
            else:
                salary = 0
        else:
            salary = "Не указана"
        url = vacancy.get("url")
        return cls(name, area, salary, url)

