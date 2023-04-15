#ask 2

# Write a decorator that takes a list of stop words and replaces them with * inside the decorated function
#

from functools import wraps

def stop_words(words: list):
    def decor(func):
        @wraps(func)
        def wrap(some_string: str):
            func_string = func(some_string)
            list_of_words = func_string.split()
            for word in words:
                i = 0
                while i < len(list_of_words):
                    if list_of_words[i] == word:
                        list_of_words[i] = "*"
                    i += 1
            result_string = ' '.join(list_of_words)
            return(result_string)
        return wrap
    return decor



@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW"

# print(create_slogan('Serhii'))
assert create_slogan("Steve") == "Steve drinks * in his brand new *"
