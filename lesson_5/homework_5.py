#Task 1

# The Guessing Game.
#
# Write a program that generates a random number between 1 and 10 and
# lets the user guess what number was generated. The result should be
# sent back to the user via a print statement.

import random

random_number = random.randint(1, 11)

user_number = input('Введіть очікуване число: ')

if int(user_number) == random_number:
    print("Вітаємо! Ви вгадали.")
else:
    print(f"На жаль, Ви не вгадали. Правильне число: {random_number}")

# Task 2
#
# The birthday greeting program.
#
# Write a program that takes your name as input, and then your age as input and greets you with the following:
#
# “Hello <name>, on your next birthday you’ll be <age+1> years”

user_name = input("Введіть своє ім'я: ")
user_age = input('Введіть свій вік: ')

print(f"Hello {user_name.title()}, on your next birthday you'll be {int(user_age)+1} years")

# Task 3
#
# Words combination
#
# Create a program that reads an input string and then creates and prints 5 random
# strings from characters of the input string.
#
# For example, the program obtained the word ‘hello’, so it should print 5 random
# strings(words) that combine characters
#
# 'h', 'e', 'l', 'l', 'o' -> 'hlelo', 'olelh', 'loleh' …
# Tips: Use random module to get random char from string)

# Не роблю import random, тому що це вже є на початку файлу

base_string = input('Введіть базову строку: ')

for i in range(1, 6):
    result_string = ''
    indexes = ''
    while True:
        random_index = random.randint(0, len(base_string) - 1)
        if str(random_index) not in indexes:
            indexes = indexes + str(random_index)
            result_string = result_string + base_string[random_index]
        if len(indexes) == len(base_string):
            break

    print(result_string)