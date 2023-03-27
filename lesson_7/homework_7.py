# Task 1
#
# Make a program that has some sentence (a string) on input and returns
# a dict containing all unique words as keys and the number of
# occurrences as values.

sentence = 'Some sentence with some words'

sentence_list = sentence.lower().split()

result_dict = dict()

for item in list(set(sentence_list)):
    count = 0
    for word in sentence_list:
        if word == item:
            count += 1
    result_dict[item] = count

print(result_dict)

# Task 2
#
# Input data:

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Compute the total price of the stock where the total price
# is the sum of the price of an item multiplied by the quantity
# of this exact item.

total_price = 0

for food, quant in stock.items():
    total_price = total_price + prices[food] * quant

print(f'Total price of the stock is {total_price}')

# Task 3
#
# List comprehension exercise
#
# Use a list comprehension to make a list containing tuples (i, j)
# where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.

list_tuples = [(i, i**2) for i in range(1, 11)]

print(list_tuples)
print(type(list_tuples[1]))

# Task 4
#
# Створити лист із днями тижня.
# В один рядок (ну або як завжди) створити словник виду: {1: “Monday”, 2:...
# Також в один рядок або як вдасться створити зворотний словник {“Monday”: 1,

week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

week_dict = dict([(i+1, week_days[i]) for i in range(len(week_days))])
week_dict_reverse = dict([(week_days[i], i+1) for i in range(len(week_days))])

print(week_dict)
print(week_dict_reverse)
