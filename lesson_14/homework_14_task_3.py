#Task 3

# Write a decorator `arg_rules` that validates arguments passed to the function.
#
# A decorator should take 3 arguments:
#
# max_length: 15
#
# type_: str
#
# contains: [] - list of symbols that an argument should contain
#
# If some of the rules' checks returns False, the function should return False and print the reason it failed; otherwise, return the result.
#
# ```

def arg_rules(type_: type, max_length: int, contains: list):
    def decor(func):
        def wrap(some_string: str):
            is_contains_in_string = True
            for item in contains:
                if item not in some_string:
                    is_contains_in_string = False
                    break
            if len(some_string) > max_length:
                print('argument is longer then max_lenght')
                return False
            elif type(some_string) != str:
                print('argument is not string')
                return False
            elif is_contains_in_string == False:
                print("argument doesn't contain mandatory symbols")
                return False
            else:
                return func(some_string)
        return wrap
    return decor


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe0@gmail') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
