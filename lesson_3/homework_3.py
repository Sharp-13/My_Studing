# 1 The greeting program.
# Make a program that has your name and the current day of the week stored as
# separate variables and then prints a message like this:
# "Good day <name>! <day> is a perfect day to learn some python."

name = 'Serhii'
current_day = 'friday'
print('Good day', name + '!', current_day.title(), 'is a perfect day to learn some python.')

# 2 Manipulate strings.
# Save your first and last name as separate variables,
# then use string concatenation to add them together with a white space in between and print a greeting.

first_name = 'Serhii'
last_name = 'Mazura'

full_name = first_name + ' ' + last_name
print('Good day', full_name + '!', current_day.title(), 'is a perfect day to learn some python.')

# 3 Using python as a calculator.
#
# Make a program with 2 numbers saved in separate variables a and b, then print the result for each of the following:
#
# Addition
# Subtraction
# Division
# Multiplication
# Exponent (Power)
# Modulus
# Floor division

a = 45
b = 22

print('Результат додавання', str(a), 'і', str(b), 'дорівнює', str(a+b))
print('Результат віднімання', str(b), 'від', str(a), 'дорівнює', str(a-b))
print('Результат ділення', str(a), 'на', str(b), 'дорівнює', str(a/b))
print('Результат множення', str(a), 'і', str(b), 'дорівнює', str(a*b))
print('Результат піднесення', str(a), 'до ступеня', str(b), 'дорівнює', str(a**b))
print('Залишок від ділення', str(a), 'на', str(b), 'дорівнює', str(a%b))
print('Ціла частина від ділення', str(a), 'на', str(b), 'дорівнює', str(a//b))