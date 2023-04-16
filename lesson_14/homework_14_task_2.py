#ask 2

# Write a decorator that takes a list of stop words and replaces them with * inside the decorated function
#

from functools import wraps
from typing import Callable
def stop_words(words: list):
    def decor(func: Callable):
        @wraps(func)
        def wrap(*args, **kwargs):
            result_string = func(*args, **kwargs)
            for word in words:
                result_string = result_string.replace(word, "*")
            return result_string
        return wrap
    return decor

@stop_words(['pepsi', 'BMW'])
def create_slogan(name = "Steve"):
    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan('Serhii'))
assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
