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

import books_modul
import authors

class Library:
    pass

# class Book:
#
#     def __init__(self, name, year, author):
#         self.name = name
#         self.year = year
#         self.author = author
#
#     def __repr__(self):
#         return f'Book (name: {self.name}, year: {self.year}, author: {self.author})'
#
#     def __str__(self):
#         return f'{self.name} was written by {self.author} in {self.year}'


# class Author:
#     def __init__(self, name, country, birthday, books):
#         self.name = name
#         self.country = country
#         self.birthday = birthday
#         books_list = list()
#         for book in books:
#             if isinstance(book, Book):
#                 books_list.append(book)
#             else:
#                 raise ValueError('Not valid bookname')
#         self.books = books_list
#
#     def __repr__(self):
#         return f"{self.name} (birthday: {self.birthday}, country: {self.country}, books: {self.books}"
#
#     def __str__(self):
#         return f"{self.name} was born {self.birthday} in {self.country}. He wrote books: {self.books}"



# books = ['Angels and Demons', 'The Da Vinci Code', 'Inferno']
# dan_brown = Author('Dan Brown', 'USA', '22.06.1964', books)
# angels_and_demons = Book('Angels and Demons', 2000, dan_brown)
# da_vinci_code = Book('The Da Vinci Code', 2003, dan_brown)
# inferno = Book('Inferno', 2013, dan_brown)
print(authors.dan_brown.__repr__())
print(authors.dan_brown.__str__())
