import books_modul

class Author:
    def __init__(self, name, country, birthday, books):
        self.name = name
        self.country = country
        self.birthday = birthday
        books_list = list()
        for book in books:
            if isinstance(book, books_modul.Book):
                books_list.append(book)
            else:
                raise ValueError('Not valid bookname')
        self.books = books_list

    def __repr__(self):
        return f"{self.name} (birthday: {self.birthday}, country: {self.country}, books: {self.books}"

    def __str__(self):
        return f"{self.name} was born {self.birthday} in {self.country}. He wrote books: {self.books}"


books = [books_modul.angels_and_demons, books_modul.da_vinci_code, books_modul.inferno]
dan_brown = Author('Dan Brown', 'USA', '22.06.1964', books)