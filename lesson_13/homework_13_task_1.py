# Task 1

# Write a Python program to detect the number of local variables declared in a function.

def var_counter(func) -> int:
    return func.__code__.co_nlocals

def some_func():
    a = 0
    b = '1'
    c = [0, 1, 2]

result = var_counter(some_func)
print(result)

