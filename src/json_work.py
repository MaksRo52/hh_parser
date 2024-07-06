from abc import ABC, abstractmethod
import os.path
import json
from src.vacancy import Vacancy


class WorkWithFile(ABC):
    @abstractmethod
    def edit_file(self, data):
        pass

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def delete_file(self):
        pass


class SaveJson(WorkWithFile):
    """Класс для работы с json"""
    def __init__(self, abs_path="vacancies.json"):
        self.abs_path = f"data/{abs_path}"

    def edit_file(self, data):
        with open(self.abs_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def read_file(self):
        with open(self.abs_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        vacancies = []
        for vacancy in data:
            vacancies.append(Vacancy(
                name=vacancy['name'],
                area=vacancy['area'],
                salary=vacancy['salary'],
                url=vacancy['url']))
        return vacancies

    def delete_file(self):
        pass