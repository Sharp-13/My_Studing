# Create your own implementation of a built-in function range, named in_range(),
# which takes three parameters: `start`, `end`, and optional step.
# Tips: See the documentation for `range` function

def in_range(start, end, step = 1):
    n = start
    if step == 0:
        raise ValueError('Step can not be zero')
    elif step > 0:
        while n <= end:
            yield n
            n += step
    else:
        while n >= end:
            yield n
            n += step

for i in in_range(8, 3, -2):
    print(i)

