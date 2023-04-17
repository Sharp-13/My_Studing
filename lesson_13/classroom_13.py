# Задача 1: Створити логгер.
#
# Написати декоратор, котрий записує результат кожного виконання функції в пам'ять в форматі:
# 2023-01-01 02:02:32, функція FUNCTION_NAME була виконана з параметрами *ПЕРЕЛІК ПАРАМЕТРІВ*
# і повернула результат *РЕЗУЛЬТАТ*
# Декоратор має приймати параметр, котрий регулює кількість рядків, котрі максимально тримаються
# в пам'яті т назву файлу з логами.
# Коли кількість рядків перевищує дозволену, декоратор має записувати логи в файл

# from datetime import datetime
#
#
# def func():
#     pass
#
#
# log_list = list()
#
#
# def wrap(*args, **kwargs):
#     time = str(datetime.now())
#     string_of_args = " ".join([f"argument {element}" for element in args])
#     string_of_kwargs = " ".join([f"argument {element_key}, {element_value}" \
#                                  for element_key, element_value in kwargs.items()])
#     func_name = func.__name__


# Задача 2. Імплементувати lru_cache
#
# lru_cache - декоратор, що запам'ятовує останні виклики функції й якщо вона ще раз викликається з цими аргументами, то він дістає її значення з кешу замість виконання.
#
# Імплементуйте декоратор, котрий дозволяє зберігати останні виклики функції в якомусь словнику і звертатися до них за потреби.
#
# Для простоти вважаємо, що ми маємо справу з функціями однієї змінної

from functools import wraps

def my_cache(func):
    container = dict()
    @wraps(func)
    def wrapper(arg):
        call = (func, arg)
        if call in container.keys():
            a = container[call]
            return a
        else:
            a = func(arg)
            container[call] = a
            return a
    return wrapper



@my_cache
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)


# Задача 3. Написати декоратор, що повторює виконання функції у випадку провалу
#
# Напишіть декоратор, що повторює виклик функції N разів, якщо до цього він завершився з помилкою.
#
# Якщо помилка повторюється N разів, треба видати повідомлення про помилку, але не рейзити ексепшн.

# Задача 2. Робота з файлами через map.
#
# В директорії titanic_data ви можете знайти файл titanic_data.csv.
#
# Напишіть програму, що видаляє другу колонку з цієї таблиці та зберігає оновлену таблицю
# у файл titanic_data_2.csv.
#
# Бажано використовувати map для якомога більшої долі операцій.
#
# Hint: ви можете зробити за допомогою map все, окрім власне роботи з файлами

from functools import reduce

# file_path = "titanic_data.csv"

with open("titanic_data.csv", "r") as f:
    rows_list = f.readlines()


# splited_list = list()
def new_func(e):
    e1 = e.split(",")
    b = e1[:1] + e1[2:]
    row = reduce(lambda item1, item2: item1 + "," + item2, b)
    return row


splited_list = map(new_func, rows_list)

print(list(splited_list))

with open("titanic_data_1.csv", "w") as f_1:
    for row in list(splited_list):
        f_1.write(row)



