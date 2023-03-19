# Задача 2: для даних ПІБ і серії-номера паспорту зробити наступне:
# 1. ПІБ очистити від небажаних символів і привести в офіційний формат
# 2. Серію паспорта привести в належний формат (тільки великі літери, ніяких інших символів).
# 3. Вивести серію-номер паспорта в зворотньому порядку.
# 4. Вивести суму цифр в номері паспорта.
# 5. Перевірити, чи є рядок "great poet" в рядку статуса громадянина
# Для цілей задачі вважаємо, що серія може бути довільної довжини, номер - 6 символів.
# Також, нагадую, що якщо ви не знаєте, як шукати специфічні для типу методи (як-то "abc".lower()),
# ви можете завжди викликати вбудовану функцію dir() з переданим у неї конструктором типу.

corrupted_name_1 = "    $%taras shevchenko& "
id_number = "greattalentgr123eatresponsibility-240891"
corrupted_status = "jfsnljnlsfgnjfsgnjlsgfnlngfslnsdglnlsdgnljgsdnlnln great poet 'akk;ldnflkjsabg;kbouht024h0pijngadknsn"

#1
correct_name = ''

for i in corrupted_name_1:
    if i.isalpha() or i == ' ':
        correct_name += i

print(correct_name.strip().title())

#2
id_series = id_number[:-6]
correct_id_series = ''

for i in id_series:
    if i.isalpha() or i.isdigit():
        correct_id_series += i

correct_id_series = correct_id_series.upper()
print(correct_id_series)

#3
print(id_number[-6:], correct_id_series, sep='')

#4
result_sum = 0

for i in id_number[-6:]:
    result_sum += int(i)

print(result_sum)

#5
if 'great poet' in corrupted_status:
    print('У статусі вказано "великий поет"')
else:
    print('У статусі не вказано "великий поет"')