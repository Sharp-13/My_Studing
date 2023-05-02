from dataclasses import dataclass
import books_modul

@dataclass
class Author:

    name: str
    country: str
    birthday: str
        # books_list = list()
        # for book in books:
        #     if isinstance(book, books_modul.Book):
        #         books_list.append(book)
        #     else:
        #         raise ValueError('Not valid bookname')
    books: list[books_modul.Book]

    def __repr__(self):
        return f"{self.name} (birthday: {self.birthday}, country: {self.country}, books: {self.books}"

    def __str__(self):
        return f"{self.name} was born {self.birthday} in {self.country}. He wrote books: {self.books}"


# books = ['angels and demons', 'inferno', 'the da vinci cide']
books = [books_modul.angels_and_demons, books_modul.da_vinci_code, books_modul.inferno]
dan_brown = Author('Dan Brown', 'USA', '22.06.1964', books)