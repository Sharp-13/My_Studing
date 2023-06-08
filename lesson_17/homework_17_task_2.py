# Task 2

# Library
# Write a class structure that implements a library. Classes:
# 1) Library - name, books = [], authors = []
# 2) Book - name, year, author (author must be an instance of Author class)
# 3) Author - name, country, birthday, books = []
#
# Library class
# Methods:
# - new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the
# book to the books list for the current library.
# - group_by_author(author: Author) - returns a list of all books grouped by the specified author
# - group_by_year(year: int) - returns a list of all the books grouped by the specified year

# All 3 classes must have a readable __repr__ and __str__ methods.
# Also, the book class should have a class variable which holds the amount of all existing books
#

from dataclasses import dataclass


@dataclass
class Author:

    name: str
    country: str
    birthday: str
    books: list[str]

    def __repr__(self):
        return f"{self.name} (birthday: {self.birthday}, country: {self.country}, books: {self.books}"

    def __str__(self):
        return f"{self.name} was born {self.birthday} in {self.country}. He wrote books: {self.books}"


class Book:

    def __init__(self, name: str, year: int, author: Author):
        self.name = name
        self.year = year
        if isinstance(author, Author):
            self.author = author
        else:
            raise ValueError('Author is not valid')

    def __repr__(self):
        return f'Book (name: {self.name}, year: {self.year}, author: {self.author.name})'

    def __str__(self):
        return f'{self.name} was written by {self.author.name} in {self.year}'


@dataclass
class Library:

    def __init__(self, name: str, books: list[Book], authors: list[Author]):
        self.name = name
        self.books = books
        self.authors = list()
        for author in authors:
            if isinstance(author, Author):
                self.authors.append(author)
            else:
                raise ValueError('Author is not valid')

    def new_book(self, name: str, year: int, author: Author):
        self.books.append(Book(name, year, author))
        author.books.append(name)
        if author not in self.authors:
            self.authors.append(author)
        return Book(name, year, author)

    def group_by_author(self, author: Author):
        return author.books

    def group_by_year(self, year: int):
        books_by_year = list()
        for book in self.books:
            if book.year == year:
                books_by_year.append(book)
        return books_by_year


dan_brown = Author('Dan Brown', 'USA', '22.06.1964', ['Angels and Demons', 'The Da Vinci Code'])
victor_hugo = Author('Victor Hugo', 'France', '26.02.1802', ['Les Miserables', 'The Hunchback of Notre Dame'])
dumas = Author('Alexandre Dumas', 'France', '24.07.1802', ['The Count of Monte Cristo'])

angels_and_demons = Book('Angels and Demons', 2000, dan_brown)
da_vinci_code = Book('The Da Vinci Code', 2003, dan_brown)
inferno = Book('Inferno', 2013, dan_brown)
les_miserables = Book('Les Miserables', 1862, victor_hugo)
notre_dame = Book('The Hunchback of Notre Dame', 1831, victor_hugo)
my_lib = Library('My library', [angels_and_demons, da_vinci_code, inferno, les_miserables, \
                                notre_dame], [dan_brown, victor_hugo])
quatrevingt_treize = my_lib.new_book('Quatrevingt-treize', 1874, victor_hugo)
musketeers = my_lib.new_book('The Three Musketeers', 1844, dumas)
my_hugo_books = my_lib.group_by_author(victor_hugo)
books_2000 = my_lib.group_by_year(2000)


print(musketeers.__repr__())
print(quatrevingt_treize.__str__())
print(inferno.__repr__())
print(victor_hugo.__repr__())
print(dan_brown.__str__())
print(dumas.__str__())
print(my_lib.books)
print(my_lib.authors)
print(my_hugo_books)
print(books_2000)

