# Task 2
#
# Extend Phonebook application
#
# Functionality of Phonebook application:
#
# Add new entries
# Search by first name
# Search by last name
# Search by full name
# Search by telephone number
# Search by city or state
# Delete a record for a given telephone number
# Update a record for a given telephone number
# An option to exit the program
#
#
# The first argument to the application should be the name of the phonebook.
# Application should load JSON data, if it is present in the folder with application, else raise an error.
# After the user exits, all data should be saved to loaded JSON.

# import json

from crud_functions import *

GREATING_TEXT = 'Доброго дня! Вітаємо Вас у телефонній книзі Beetroot!'
CHOICE_OPERATION_TEXT = '''Будь ласка, виберіть команду:
- якщо Ви бажаєте додати новий номер до телефонної книги - натисніть "1";
- якщо Ви бажаєте знайти номер у телефонній книзі - натисніть "2";
- якщо Ви бажаєте змінити дані за номером - натисніть "3";
- якщо Ви бажаєте видалити номер з телефонної книги - натисніть "4";
- якщо Ви бажаєте завершити виконання програми - натисніть "0".
'''

print(GREATING_TEXT)

operation_dict = {
    '1': create_number,
    '2': search_number,
    '3': update_number,
    '4': delete_number
}

while True:
    selected_operation = input(CHOICE_OPERATION_TEXT)
    if int(selected_operation) in range(1, 5):
        operation_dict[selected_operation]()
    elif int(selected_operation) == 0:
        break
    else:
        print('Такої команди не існує. Будь ласка, виберіть команду ще раз')


