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

import re

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

DEFAULT_NAME_LEN_THRESHOLD = 200
LOW_YEAR_THRESHOLD = 1895


def validate_name(value, len_threshold=DEFAULT_NAME_LEN_THRESHOLD):
    # Перевіряємо довжину назви фільма, порожність назви фільма і щоб не було тільки пробілів і табуляцій
    len_value = len(value)
    is_len_appropriate = len_value < len_threshold
    is_only_spaces_or_tabs = value.count(" ") + value.count("\t") == len_value
    return is_len_appropriate and not is_only_spaces_or_tabs


def validate_year(value):
    is_numeric = value.isnumeric()
    is_year_sane = int(value) >= 1895
    return is_numeric and is_year_sane


def validate_director(value):
    # Alphabet chars, spaces, dots, hyphens are allowed
    is_dir_valid = value.replace(" ", "").replace("-", "").replace(".", "").isalpha()
    # Another way of doing it via regex:
    pattern = "[\w -]*$"
    try:
        is_dir_valid_re = re.match(pattern, value).string == value
    except AttributeError:
        is_dir_valid_re = None
    return is_dir_valid


def validate_rank(value):
    pattern_for_floats = "^([0-9]+\.[0-9]+)|\d$"
    try:
        is_rank_valid_re = re.match(pattern_for_floats, value).string == value
    except AttributeError:
        is_rank_valid_re = None
    return is_rank_valid_re


films_container = {
    1: {
        "name": "Аватар: Шлях води",
        "year": 2022,
        "director": "James Cameron",
        "imdb": 7.8,
    },
    2: {
        "name": "Аватар: Шлях води 3",
        "year": 2022,
        "director": "James Cameron",
        "imdb": 7.8,
    },
    }


def create_film():
    """Ця функція створює dict з даними про фільм за наступним принципом:
    1. Дивиться у набір обов'язкових полів
    2. Запитує у користувача значення для цього поля
    3. Валідує це поле згідно оговорених правил
    4. Якщо поле не валідно, повторити запит допоки не введено правильне значення
    5. Створити dict з цих полів
    6. Якщо фільма з таким самим набором полів не існує в films_container - зберегти його в цю змінну
    Інакше - видати повідомлення (не робити raise exception)

    Hint 1: При збереженні в films_container треба створити унікальний ID у вигляді ключа, не забудьте про це

    Hint 2: зробіть валідатори для полів окремими функціями."""

    mandatory_fields_dict = {
        "name": validate_name,
        "year": validate_year,
        "director": validate_director,
        "imdb": validate_rank
    }

    mandatory_fields_types_dict = {
        "name": str,
        "year": int,
        "director": str,
        "imdb": float
    }

    mandatory_fields_final_dict = dict()

    for field_name, field_validator in mandatory_fields_dict.items():
        is_field_valid = False
        while not is_field_valid:
            field_value = input(f"Введить значення для поля {field_name} ")
            is_field_valid = field_validator(field_value)
            if not is_field_valid:
                print("Це поле не є валідним!")
        mandatory_fields_final_dict[field_name] = mandatory_fields_types_dict[field_name](field_value)

    # Наступна частина перевіряє, чи є в базі фільм з введеними даними
    # Тут я виходжу з того, що дані про фільм зберігаються у вигляді словника, де ключі - це айдішки фільмів,
    # а значення - вкладений словник з даними. Тобто наш films_container виглядає наступним чином:

    is_film_in_container = False

    for film in films_container.values():   # Перебираємо films_container, беручи по черзі словники з даними про окремий фільм
        for film_field_name, film_field_value in film.items():  # Перебираємо поля даних про фільм у films_container і порівнюємо їх з полями нашого mandatory_fields_final_dict
            if mandatory_fields_final_dict[film_field_name] != film_field_value:    # Якщо значення у якомусь з полів не співпадають - виходимо з циклу, далі нема сенсу перевіряти
                break
        else:   # Якщо не було викликано break, значить всі значення співпали - піднімаємо прапорець, що такий фільм вже є у базі
            is_film_in_container = True

    if not is_film_in_container:    # Власне, якщо is_film_in_container = False - додаємо фільм до бази
        films_container[len(films_container)+1] = mandatory_fields_final_dict
    else:
        print('Такий фільм вже є у базі')


# Наступний код треба для перевірки
# Безкінечний цикл використав, щоб додати декілька записів
while True:
    create_film()
    print(films_container)