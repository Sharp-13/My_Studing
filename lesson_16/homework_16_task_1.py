# Task 1
#
# School
#
# Make a class structure in python representing people at school.
# Make a base class called Person, a class called Student, and another one called Teacher.
# Try to find as many methods and attributes as you can which belong to different classes,
# and keep in mind which are common and which are not. For example, the name should be a Person attribute,
# while salary should only be available to the teacher.

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self):
        pass

    def write(self):
        pass

class Student(Person):
    def __init__(self, group):
        self.group = group

    def speak(self):
        return "Answer the teacher's questions"

    def study(self):
        return 'Studies subjects according to the curriculum'

    def write(self):
        return 'Writes some lecture notes'

class Teacher(Person):
    def __init__(self, subject, salary):
        self.subject = subject
        self.salary = salary

    def teach(self):
        return f'Teaches students the {self.subject}'

    def speak(self):
        return 'Gives lectures'

