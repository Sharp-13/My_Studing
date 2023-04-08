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

file_path = "titanic_data.csv"

with open("titanic_data.csv", "r") as f:
    rows_list = f.readlines()

splited_list = list()
for e in rows_list:
    e1 = e.split(",")
    b = e1[:1] + e1[2:]
    row = ""
    for item in b:
        row += item +  ","
    splited_list.append(row[:-1])
print(splited_list)

with open("titanic_data_1.csv", "w") as f_1:
    for row in splited_list:
        f_1.write(row)