# Task 2
#
# Write a Python program to access a function inside a function
# (Tips: use function, which returns another function)

def external_func(some_var: int):
    def internal_func(degree: int) -> int:
        return some_var**degree

    return internal_func

result = external_func(4)
print(result(3))
print(external_func(2)(8))