# Task 1
#
# Write a function called oops that explicitly raises an IndexError exception when called.
# Then write another function that calls oops inside a try/except statement to catch the error.
# What happens if you change oops to raise KeyError instead of IndexError?

def oops(example_str):
    example_list = example_str.strip()
    print(example_list[len(example_list)])


def oops1(example_str):
    example_list = example_str.strip()
    example_dict = {item: item.title() for item in example_list}
    print(example_dict['@'])


def try_oops(input_string):
    try:
        oops(input_string)
    except IndexError:
        print('Oops! Something went wrong')


def try_oops1(input_string):
    try:
        oops1(input_string)
    except IndexError:
        print('Oops! Something went wrong. Again(')


some_string = input('Write some string: ')
try_oops(some_string)

# Якщо розкоментувати і викликати наступну функцію - згенерується помилка KeyError
#try_oops1(some_string)

# Task 2
#
# Write a function that takes in two numbers from the user via input(), call the numbers a and b,
# and then returns the value of squared a divided by b, construct a try-except block which
# raises an exception if the two values given by the input function were not numbers,
# and if value b was zero (cannot divide by zero).

def calculating():
    try:
        a = int(input('Please, enter value of "a": '))
        b = int(input('Please, enter value of "b": '))
        print(f'Result is: {a ** 2 / b}')
    except ValueError:
        print('"a" or "b" is not numeric')
    except ZeroDivisionError:
        print('"b" cannot be zero')


calculating()
