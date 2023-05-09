# Create your own implementation of a built-in function range, named in_range(),
# which takes three parameters: `start`, `end`, and optional step.
# Tips: See the documentation for `range` function

def in_range(start, end, step = 1):
    n = start
    while n <= end:
        yield n
        n += step

for i in in_range(3, 8, 2):
    print(i)