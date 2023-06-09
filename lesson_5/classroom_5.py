# Задача 1: створити модуль, в котрому буде зберігатися математична константа Пі i e
# За допомогою цих констант зробити програму, котра рахує:
# 1. Площу круга довільного радіусу
# 2. Довжину круга довільного радіусу
# 3. Перевіряє тотожність Ейлера (e^(i*pi) = -1)

# i = корінь з -1, нижче буде показано, як його знайти в Python

import constants

i = complex(0, 1)

is_input_valid = False
while not is_input_valid:
    rad = input('Write radius:')
    is_input_valid = rad.isdigit()
square = round(constants.PI*int(rad)**2, 2)
print('Square is', str(square))
circle_lenght = round(constants.PI*2*int(rad), 2)
print('Lenght of circle is', str(circle_lenght))

print(constants.EXP**(i*constants.PI))

# Задача 2: створити модуль, котрий:
# 1. Виводить на екран повідомлення виду "це модуль для перетворення рядків у uppercase і lowercase"
# 2. Тримає в собі дві функції: upper і lower, котрі приймають в себе рядок і видають рядок  у відповідному кейсі
# 3. Якщо він викликаний незалежно (а не в імпорті), він виводить ваше ім'я в lowercase і uppercase.


# Приклад оголошення функцій буде надано нижче. Треба буде виключно створити їхню імплементацію.
# Можна використовувати вбудовані функції, але краще використати таблицю ASCII :)
# В рамках задачі можемо обмежитися словами з символами виключно з латинського алфавіту.

def lower(string):
    """Функція, котра переводить рядок string у lowercase"""
    #Here goes your implementation
    return result

def upper(string):
    """Функція, котра переводить рядок string у uppercase"""
    #here goes your implementation
    return result

# Задача 3: генерація випадкових дат.
#
# В Python існує безліч зручних вбудованих модулей. Наразі, нас цікавлять два: random і datetime.
#
# datetime - модуль, що дозволяє працювати з datetime-об'єктами, використовуючи доволі простий інтерфейс (приклади нижче в коді)
#
# Напишіть програму, котра:
#   Бере сьогоднішню дату
#     Бере випадкове ціле число від 1 до 100
#     Віднімає цю кількість років від поточного року
#     Генерує дату між отриманим на попередньому кроці роком і сьогоднішнім днем
#     Виводить її
#     Виводить різницю між сьогоднішнім днем і випадковою датою.
# Врахуйте, що в різних місяцях різна кількість днів. Якщо, наприклад, ваш код видає щось на кшталт 30 лютого, повторіть випадковий вибір до валідного результату.

# Високосні роки враховуються!


from datetime import datetime, timedelta

today = datetime.today()
print(f"Сьогодні в нас: {today.date()}")
one_day_delta = timedelta(days=1)
yesterday = today - one_day_delta
print(f"Вчора було: {yesterday.date()}")
print(f"Різниця між цими датами: {today - yesterday}")
print(f"Тип об'єкту сьогоднішньої дати: {type(today)}")
print(f"Тип різниці між датами: {type(today - yesterday)}")