class Book:  # parent class/superclass
    def __init__(self, ISBNP, AuthorP, TitleP, PriceP):
        self.__ISBN = ISBNP
        self.__Author = AuthorP
        self.__Title = TitleP
        self.__Price = PriceP

    # getters
    def ISBN(self):
        return self.__ISBN

    def Author(self):
        return self.__Title

    def Title(self):
        return self.__Title

    def Price(self):
        return self.__Price

    def Price(self, new_price):
        if new_price >= 0:
            self.__Price = new_price

    def Display_Info(self):
        print(f"ISBN: {self.__ISBN}")
        print(f"Title: {self.__Title}")
        print(f"Author: {self.__Author}")
        print(f"Price: RM{self.__Price}")


class TextBook(Book):  # subclass/child class
    def __init__(self, ISBNP, AuthorP, TitleP, PriceP, EditionP, CDP):
        super().__init__(ISBNP, AuthorP, TitleP, PriceP)
        self.__Edition = EditionP
        self.__CD = CDP

    def Display_Info(self):
        super().Display_Info()  # calling parent's method
        print(f"Edition: {self.__Edition}")  # polymorphism
        print(f"CD: {self.__CD}")  # polymorphism


class Librarian:
    def __init__(self, nameP):
        self.__name = nameP

    def GreetStudents(self):
        print(f"Hi, I am {self.__name}, your Librarian for this Library!")

#Containment↓↓↓

class Library:  
    def __init__(self, librarianP):
        self.books = []
        self.librarian = librarianP

    def add_book(self, bookP):
        self.books.append(bookP)

    def Display_Books(self):
        print("Books in the Library:")
        for book in self.books:
            book.Display_Info()

#containment: objects within objects - books and librarian within library