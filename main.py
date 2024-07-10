from src.work_with_user import WorkUser
from src.json_work import SaveJson

if __name__ == "__main__":
    vacancies = WorkUser.get_vacancy()  # Отбор всех вакансий

    editing_file = SaveJson()  # Создание экземпляра для работы с файлом

    editing_file.edit_file(vacancies)  # Запись в файл

    vacancies_ex = editing_file.read_file()  # чтение из файла и последующее создание экземпляров

    work_user = WorkUser(vacancies_ex)  # Создание экземпляра и передача списка в класс

    while True:
        select_user = int(input("""Выберите необходимое действие:
1. Вывести список
2. Вывести топ вакансий
3. Поиск по ключевому слову
4. Остановить программу\n"""))
        if select_user == 1:
            work_user.print_vacancies()  # Вывод списка
            continue
        elif select_user == 2:
            work_user.get_top_n_for_salary()  # Вывод топа
            work_user.print_vacancies()
            continue
        elif select_user == 3:
            work_user.filter_name()
            work_user.print_vacancies()
            continue
        elif select_user == 4:
            break
        else:
            print("\nТакого пункта не существует\n")
