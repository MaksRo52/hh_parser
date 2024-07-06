from abc import ABC, abstractmethod
import os.path
import json


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
    def __init__(self):
        self.abs_path = os.path.abspath("data/vacancies.json")

    def edit_file(self, data):
        with open(self.abs_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def read_file(self):
        with open(self.abs_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def delete_file(self):
        os.remove("data/vacancies.json")
