# Task 1
#
# The greatest number
#
# Write a Python program to get the largest number from a list of random
# numbers with the length of 10
#
# Constraints: use only while loop and random module to generate numbers

import random

base_list = list()
i = 0

while i < 10:
    base_list.append(random.randint(0, 100))
    i += 1
print('List: ', base_list)

base_list.sort()

print('The largest number is: ', base_list[-1])

# Task 2
#
# Exclusive common numbers.
#
# Generate 2 lists with the length of 10 with random integers from 1 to 10,
# and make a third list containing the common integers between the 2 initial
# lists without any duplicates.
#
# Constraints: use only while loop and random module to generate numbers

first_list = list()
second_list = list()
i = 0

while i < 10:
    first_list.append(random.randint(1, 10))
    second_list.append(random.randint(1, 10))
    i += 1

print('First list: ', first_list)
print('Second list: ', second_list)

first_set = set(first_list)
second_set = set(second_list)

# print(first_set)
# print(second_set)

common_numbers = list(first_set.intersection(second_set))
print('Exclusive common numbers: ', common_numbers)

# Task 3
#
# Extracting numbers.
#
# Make a list that contains all integers from 1 to 100, then find all integers
# from the list that are divisible by 7 but not a multiple of 5, and store them
# in a separate list. Finally, print the list.
#
# Constraint: use only while loop for iteration

range_list = list()
result_list = list()
i = 1

while i <= 100:
    range_list.append(i)
    i += 1

i = 0
while i < len(range_list):
    if range_list[i] % 7 == 0 and range_list[i] % 5 != 0:
        result_list.append(range_list[i])
    i += 1

print('Numbers that are divisible by 7 but not a multiple of 5: ', result_list)
