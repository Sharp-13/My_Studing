# Task 2
#
# Doggy age
#
# Create a class Dog with class attribute `age_factor` equals to 7. Make __init__()
# which takes values for a dog’s age. Then create a method `human_age` which returns
# the dog’s age in human equivalent.

class Dog:
    age_factor = 7
    def __init__(self, name, dog_age):
        self.name = name
        self.dog_age = dog_age

    def human_age(self):
        return self.dog_age * Dog.age_factor

rex = Dog("Rex", 12)
print(f'Human age of {rex.name} is {rex.human_age()}')