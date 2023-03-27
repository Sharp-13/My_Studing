#Task 1

# A simple function.
#
# Create a simple function called favorite_movie, which takes a
# string containing the name of your favorite movie. The function
# should then print “My favorite movie is named {name}”.

def favorite_movie(movie_name):
    print('My favorite movie is named ' + movie_name)


favorite_movie('Taxi')

#Task 2

# Creating a dictionary.
#
# Create a function called make_country, which takes in a country’s
# name and capital as parameters. Then create a dictionary from those two,
# with ‘name’ as a key and ‘capital’ as a parameter. Make the function
# print out the values of the dictionary to make sure that it works as intended.

def make_country(country_name, capital):
    country_dict = {country_name: capital}
    print(country_dict)


make_country('Ukraine', 'Kyiv')

#Task 3

# A simple calculator.
#
# Create a function called make_operation, which takes in a simple arithmetic
# operator as a first parameter (to keep things simple let it only be ‘+’, ‘-’ or ‘*’)
# and an arbitrary number of arguments (only numbers) as the second parameter.
# Then return the sum or product of all the numbers in the arbitrary parameter.
# For example:
#
# the call make_operation(‘+’, 7, 7, 2) should return 16
# the call make_operation(‘-’, 5, 5, -10, -20) should return 30
# the call make_operation(‘*’, 7, 6) should return 42

def sum_numbers(number, sum_result):
     sum_result = sum_result + number
     return sum_result


def mult_numbers(number, mult_result):
    mult_result = mult_result * number
    return mult_result


def sub_numbers(number, sub_result):
    sub_result = sub_result - number
    return sub_result


def make_operation(operation, *numbers):
    operation_dict = {
        '+': sum_numbers,
        '-': sub_numbers,
        '*': mult_numbers
    }
    result = numbers[0]
    for number in numbers[1:]:
        result = operation_dict[operation](number, result)
    print(result)


make_operation('+', 2, 5, 18, 5)
make_operation('-', 25, 5, 10)
make_operation('*', 7, 8, 2)