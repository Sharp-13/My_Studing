#Task 1

# Write a decorator that prints a function with arguments passed to it.
#
# NOTE! It should print the function, not the result of its execution!
#
# For example:
#
#  "add called with 4, 5"
#
# ```

from functools import wraps

def logger(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        func_name = func.__name__
        func(*args, **kwargs)
        arguments = list()
        arguments.extend(args)
        arguments.extend(kwargs)
        return print(f'{func_name} called with ', str(arguments).strip('[]'))
    return wrap


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

add(3,5)
print(add.__wrapped__(3,5))
square_all(2,3,4,5)
print(square_all.__wrapped__(2,3,4,5))
