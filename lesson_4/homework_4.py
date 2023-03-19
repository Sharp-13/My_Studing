# Task 1
#
# String manipulation
#
# Write a Python program to get a string made of the first 2 and the last 2 chars from a given
# string. If the string length is less than 2, return instead of the empty string.
#
# Sample String: 'helloworld'
#
# Expected Result: 'held'
#
# Sample String: 'my'
#
# ExpectedResult: 'mymy'
#
# Sample String: 'x'
#
# Expected Result: Empty String
#
# Tips:
#
# Use built - in function len() on an input string
# Use positive indexing to get the first characters of a string and negative indexing
# to get the last characters

string = input('Write string: ')
if len(string) < 2:
    print('Empty string')
else:
    print(string[:2] + string[-2:])

# Task 2
#
# The valid phone number program.
#
# Make a program that checks if a string is in the right format
# for a phone number.The program should check that the string contains only numerical
# characters and is only 10 characters long.Print a suitable message depending on the
# outcome of the string evaluation.

phone_number = input('Введіть номер телефону: ')

if phone_number.isdigit() and len(phone_number) <=10:
    print('Номер валідний')
else:
    print('Номер не валідний')

# Task 3
#
# The math quiz program.
#
# Write a program that asks the answer for a mathematical expression,
# checks whether the user is right or wrong, and then responds with a message accordingly.

first_number = input('Введіть перше число: ')
second_number = input('Введіть друге число: ')
while True:
    operation = input('''Виберіть операцію:
                         1. Додавання
                         2. Віднімання
                         3. Множення
                         4. Ділення
                         5. Піднесення до ступіня: ''')

    if operation in '12345':
        if operation == '1':
            result = int(first_number) + int(second_number)
        elif operation == '2':
            result = int(first_number) - int(second_number)
        elif operation == '3':
            result = int(first_number) * int(second_number)
        elif operation == '4':
            result = int(first_number) / int(second_number)
        elif operation == '5':
            result = int(first_number) ** int(second_number)
        predicted_result = input('Який результат Ви очікуєте? - ')
        print('Вірно!') if predicted_result == str(result) else print('Не вірно! Правильний результат:', str(result))
        break
    else:
        print('Немає такої операції')

# Task 4
#
# The name check.
#
# Write a program that has a variable with your name stored ( in lowercase) and then
# asks for your name as input.The program should check if your input is equal to the
# stored name even if the given name has another case, e.g., if your input is “Anton”
# and the stored name is “anton”, it should return True.

stored_name = 'serhii'

user_name = input("Введіть ім'я: ")

if user_name.lower() == stored_name:
    print("Ім'я вірне")
else:
    print("Ім'я невірне")