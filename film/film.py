# Створити консольний застосунок для збереження інформації про фільми.

# Застосунок має мати можливість робити наступне:
#
# 1. Створювати новий фільм в базі
# 2. Переглядати інформацію про фільм
# 3. Шукати фільм в базі
# 4. Оновлювати фільм в базі
# 5. Видаляти фільм з бази
#
# 1 крок: базові сутності, їхня структура та формат. Базова сутність - фільм.
# Атрибути:
#
# 1. Назва
# 2. Жанр (опціонально)
# 3. Рік випуску
# 4. Режисер
# 5. Рейтинг IMDB
# 6. Склад акторів (опціонально)
# 7. Вікові обмеження (опціонально)
# 8. Тривалість (опціонально)
# 9. Компанія-виробник
# 10. Мова (опціонально)
#
# 2 крок: дії, котрі треба робити з базовою сутністю
# Стандартний набір дій (CRUD)
#
# 3. Аналіз базових сутностей, типів даних і їх обмежень
# Назва: str
# Жанр (опціонально): List[str], max = 3
# Рік випуску: int > 0
# Режисер: str, only alphabet chars
# Рейтинг IMDB: float >= 0, round(2,1)
# Склад акторів (опціонально): List[str]
# Вікові обмеження (опціонально): str
# Тривалість (опціонально): int
# Мова (опціонально): str
#
# 4. Приклад реалізації базової сутності на Python
# example_film_dict = {
#     "id": 2,
#     "name": "Аватар: Шлях води",
#     "genres": ["Action"],
#     "year": 2022,
#     "director": "James Cameron",
#     "imdb": 7.8,
# }
#
# example_film_dict_2 = {
#     "id": 3,
#     "name": "Аватар: Шлях води 3",
#     "genres": ["Action"],
#     "year": 2022,
#     "director": "James Cameron",
#     "imdb": 7.8,
# }
# 5. Загальний сценарій використання
# - Користувач обирає команду щоб виконати
# - Система вирішує, що зробити з базою фільмів згідно команди
# - Система запитує в користувача додаткові дані за потреби
# - Система видає якийсь очікуваний результат (дані про фільм, повідомлення про успішне створення фільму, повідомлення про успішне видалення фільму ітд)
# 6. Імплементація

# import re

films_container = dict()

# Створимо головний фрагмент програми, де буде виконуватися логіка взаємодії з користувачем
# def read_command_from_user():
#     GREETING_TEXT = """Вітаю в системі для збереження даних про фільми."""
#
#
#     commands_container = [command.lower() for command in ["create", "update", "read", "delete"]]
#
#     print(GREETING_TEXT)
#     print("Print help for help")
#
#     while True:
#         command = input("Введіть команду: ").lower()
#         if command == "help":
#             print("""Вам доступні наступні команди:""")
#             for number, command in enumerate(commands_container):
#                 print(f"{number + 1}. {command}")
#         elif command in commands_container:
#             break
#         else:
#             print("Введена невалідна команда. Введіть, будь ласка, команду ще раз")
#     return command

# Валідатори полів

from validators import *


films_container = {
    1: {
        "name": "Аватар",
        "year": 2009,
        "director": "James Cameron",
        "imdb": 7.9,
    },
    2: {
        "name": "Аватар: Шлях води",
        "year": 2022,
        "director": "James Cameron",
        "imdb": 7.8,
    },
    }





# Наступний код треба для перевірки
# Безкінечний цикл використав, щоб додати декілька записів
while True:
    create_film()
    print(films_container)


#
# def update_film(films_container):
#     way_to_update = input("Choose the way to update film\n"
#                           "1. if by ID -> input id\n"
#                           "2. if by the full combination of values -> combination \n"
#                           "method: ").lower().strip()
#     if way_to_update == "id":
#         inputted_id = int(input("Provide the id: "))
#         film_ids = [key for key in films_container.keys()]
#         if inputted_id in film_ids:
#             chosen_film = films_container[inputted_id]
#             print(chosen_film)
#             value_to_change = input("What do you want to change\n"
#                                      "1. Name\n"
#                                      "2. Year\n"
#                                      "3. Director\n"
#                                      "4. IMDB\n"
#                                      "your choice: ").lower().strip()
#             new_value = input("Input new value: ")
#             if value_to_change in ['name', 'year', 'director', 'imdb']:
#                 if value_to_change == "name":
#                     is_format_valid = False
#                     iteration = 1
#                     while not is_format_valid:
#                         if iteration == 1:
#                             if validate_name(new_value):
#                                 chosen_film["name"] = new_value
#                                 is_format_valid = True
#                             else:
#                                 print("Wrong format")
#                                 iteration += 1
#                         else:
#                             new_value = input("New name: ")
#                             if validate_name(new_value):
#                                 chosen_film["name"] = new_value
#                                 is_format_valid = True
#                             else:
#                                 print("Wrong format")
#                 elif value_to_change == "year":
#                     is_format_valid = False
#                     iteration = 1
#                     while not is_format_valid:
#                         if iteration == 1:
#                             if validate_year(new_value):
#                                 chosen_film["year"] = int(new_value)
#                                 is_format_valid = True
#                             else:
#                                 print("Wrong format")
#                                 iteration += 1
#                         else:
#                             new_value = input("New name: ")
#                             if validate_name(new_value):
#                                 chosen_film["year"] = new_value
#                                 is_format_valid = True
#                             else:
#                                 print("Wrong format")
#                 elif value_to_change == "director":
#                     is_format_valid = False
#                     iteration = 1
#                     while not is_format_valid:
#                         if iteration == 1:
#                             if validate_director(new_value):
#                                 chosen_film["director"] = new_value
#                                 is_format_valid = True
#                             else:
#                                 print("Wrong format")
#                                 iteration += 1
#                         else:
#                             new_value = input("New name: ")
#                             if validate_director(new_value):
#                                 chosen_film["director"] = new_value
#                                 is_format_valid = True
#                             else:
#                                 print("Wrong format")
#                 elif value_to_change == "imdb":
#                     is_format_valid = False
#                     iteration = 1
#                     while not is_format_valid:
#                         if iteration == 1:
#                             if validate_rank(new_value):
#                                 new_value = float(new_value)
#                                 chosen_film["imdb"] = new_value
#                                 is_format_valid = True
#                             else:
#                                 print("Wrong format")
#                                 iteration += 1
#                         else:
#                             new_value = input("New name: ")
#                             if validate_rank(new_value):
#                                 new_value = float(new_value)
#                                 chosen_film["imdb"] = new_value
#                                 is_format_valid = True
#                             else:
#                                 print("Wrong format")
#     elif way_to_update == "combination":
#         is_name_valid = False
#         while not is_name_valid:
#             name = input("Name: ").title()
#             if validate_name(name):
#                 is_name_valid = True
#             else:
#                 print("wrong format")
#         is_year_valid = False
#         while not is_year_valid:
#             year = input("Year: ")
#             if validate_year(year):
#                 is_year_valid = True
#                 year = int(year)
#             else:
#                 print("wrong format")
#         is_director_valid = False
#         while not is_director_valid:
#             director = input("Director: ").title()
#             if validate_director(director):
#                 is_director_valid = True
#             else:
#                 print("wrong format")
#         is_rank_valid = False
#         while not is_rank_valid:
#             imdb = input("IMDB: ")
#             if validate_rank(imdb):
#                 is_rank_valid = True
#                 imdb = float(imdb)
#             else:
#                 print("wrong format")
#         films_list = [film for film in films_container.values()]
#
#         for film in films_list:
#             is_name_found = film["name"] == name
#             is_year_found = film["year"] == year
#             is_director_found = film["director"] == director
#             is_imdb_found = film["imdb"] == imdb
#             if is_name_found and is_year_found and is_director_found and is_imdb_found:
#                 print(film)
#
# # def delete_film() -> None:
# #     """Ця функція дозволяє видаляти фільм з бази.
# #     1. Функція запитує ID фільму або ПОВНУ КОМБІНАЦІЮ полів, котрі відрізняють один фільм від іншого.
# #     2. Функція валідує значення цього поля
# #     4. Якщо фільм з подібною комбінацією полів існує, функція видаляє його із бази.
# #
# #     Hint: погугліть про del чи pop"""
# #     pass
# import val_module as val
#
# films_container = {
#     1: {
#     "name": "Interstellar",
#     "year": 2014,
#     "director": "Christopher Nolan",
#     "imdb": 8.6
#     },
#     2: {
#     "name": "The Menu",
#     "year": 2022,
#     "director": "Mark Mylod",
#     "imdb": 7.2
#     },
#     3: {
#     "name": "La grande bellezza",
#     "year": 2013,
#     "director": "Paolo Sorrentino",
#     "imdb": 7.7
#     },
#     4: {
#     "name": "Interstellar",
#     "year": 2040,
#     "director": "Christopher",
#     "imdb": 8.9
#     },
# }
#
#
# def delete_full_combination():
#     name_inp = input("Введіть назву фільму: ")
#     year_inp = input("Введіть рік фільму: ")
#     director_inp = input("Введіть режисера фільму: ")
#     imdb_inp = input("Введіть рейтинг imdb: ")
#     valid_name = val.validate_name(name_inp)
#     valid_year = val.validate_year(year_inp)
#     valid_director = val.validate_director(director_inp)
#     valid_imdb = val.validate_rank(imdb_inp)
#     if valid_name and valid_year and valid_director and valid_imdb:
#         for key, value in films_container.items():
#             delete_key = key
#             if value['name'] == name_inp and value['year'] == int(year_inp) and \
#                 value['director'] == director_inp and value['imdb'] == float(imdb_inp):
#                 del films_container[delete_key]
#                 print(f"Фільм з ID №{delete_key} видалений.")
#                 break
#             elif value['name'] != name_inp and value['year'] != int(year_inp) and \
#                 value['director'] != director_inp and value['imdb'] != float(imdb_inp):
#                 continue
#             else:
#                 print("Такого фільму не існує. Введіть, будь ласка, дані ще раз.")
#                 delete_full_combination()
#
#
# def delete_id(id_input):
#     if id_input in films_container:
#         films_container.pop(id_input)
#         print(f"Фільм з ID №{id_input} видалений.")
#     else:
#         print("Цього фільму немає")
#
#
# # def delete_separate():
# #     print("За яким полем бажаєте видалити фільм?", "За назвою команда 1", "За роком команда 2",
# #           "За режисером команда 3", "За рейтингом imdb команда 4", sep='\n')
# #     command = int(input("Введіть команду: "))
# #     name_inp = input("Введіть назву фільму: ")
# #     valid_name = val.validate_name(name_inp)
# #     if command == 1:
# #         key_list = list()
# #         for key, value in films_container.items():
# #             if value['name'] == valid_name:
# #                 key_list.append(key)
# #                 print(f"Фільми за назвою {name_inp} видалені.")
# #         for key in key_list:
# #             del films_container[key]
# #
# #
# #     # elif command == 2:
# #     # elif command == 3:
# #     # elif command == 4:
#
#
# def read_command_from_user():
#     GREETING_TEXT = """Вітаю в системі для видаленя даних про фільми."""
#     print(GREETING_TEXT)
#     print("Як бажаєте видалити фільм?", "За ID введіть команду 1", "За комбінацією полів введіть команду 2",
#           "За окремим полем введіть команду 3", sep = '\n')
#     command = int(input("Введіть команду: "))
#     if command == 1:
#         id_input = int(input("Введіть ID фільму: "))
#         delete_id(id_input)
#     elif command == 2:
#         delete_full_combination()
#     elif command == 3:
#         delete_separate()
#     else:
#         print("Введена невалідна команда. Введіть, будь ласка, команду ще раз.")
#         read_command_from_user()


# def read_film() -> None:
#     print('''It's function to search film by some fields:
#      Here are the fields:
#      -- ID
#      -- Name
#      -- Year
#      -- Director
#      -- IMDB
#              ''')
#     while True:
#         field_name = input("Enter the name of the field to search (or 'id'): ")
#         if field_name == "id" or field_name in films_container[1]:
#             break
#         else:
#             print("Please enter a valid field name.")
#
#     search_value = input(f"Enter the value for {field_name}: ")
#     found_films = list()
#
#     if field_name == "id":
#         if int(search_value) in films_container:
#             found_films.append({search_value: films_container[int(search_value)]})
#     else:
#         for film_id, film in films_container.items():
#             if field_name in film and search_value == str(film[field_name]):
#                 found_films.append({film_id: film})
#
#     if found_films:
#         print("Found films:")
#         for film in found_films:
#             film_id = list(film.keys())[0]
#             info = film[film_id]
#             print(f"Film ID: {film_id}")
#             print(f"Name: {info['name']}")
#             print(f"Year: {info['year']}")
#             print(f"Director: {info['director']}")
#             print(f"IMDB rating: {info['imdb']}")
#     else:
#         print("No films found.")
#
# read_film()