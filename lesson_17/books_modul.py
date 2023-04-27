import authors

class Book:

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author

    def __repr__(self):
        return f'Book (name: {self.name}, year: {self.year}, author: {self.author})'

    def __str__(self):
        return f'{self.name} was written by {self.author} in {self.year}'


angels_and_demons = Book('Angels and Demons', 2000, dan_brown)
da_vinci_code = Book('The Da Vinci Code', 2003, dan_brown)
inferno = Book('Inferno', 2013, dan_brown)
