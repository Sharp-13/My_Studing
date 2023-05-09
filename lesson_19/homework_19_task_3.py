# Create your own implementation of an iterable, which could be used inside for-in loop.
# Also, add logic for retrieving elements using square brackets syntax.

class MyIterator:

    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.iterable):
            self.index += 1
            return self.iterable[self.index-1]
        else:
            raise StopIteration


test_list = ['sfv', 'afv', 'ety', 'qwe']
for i in MyIterator(test_list):
    print(i)

iterator = MyIterator(test_list)
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
