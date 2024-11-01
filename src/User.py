from abc import ABC
from abc import abstractmethod
from uuid import uuid4

from Book import Book
from exceptions import NotBookToReturn
from exceptions import BookCantRented
from exceptions import BookNotValidError
from exceptions import BookCantReturn


class User(ABC):
    def __init__(
        self, name: str, surname: str,
        address: str
    ) -> None:
        self.__id = str(uuid4())
        self.__name = name
        self.__surname = surname
        self.__address = address

    @property
    def id(self) -> str:
        return self.__id

    @property
    def complete_name(self) -> str:
        return self.__name + " " + self.__surname

    @property
    def address(self) -> str:
        return self.__address

    def __str__(self) -> None:
        print(f"----- User {self.id} -----")
        return (
            f"User ID: {self.id}\n"
            f"User: {self.complete_name}\n"
            f"User Adress: {self.address}\n\n"
        )

    @abstractmethod
    def rent_book(self) -> None:
        pass

    @abstractmethod
    def return_book(self) -> None:
        pass
        

class UserNormal(User):
    def __init__(self, name: str, surname: str, address: str) -> None:
        super().__init__(name=name, surname=surname, address=address)
        self.__rented_book: Book = None

    @property
    def rented_book(self) -> Book:
        return self.__rented_book
    
    def rent_book(self, book: Book) -> None:
        if self.rented_book: raise BookCantRented(f"You cannot rent another book, you must return {self.rented_book.name} before renting another one.")
        if not book.stock: raise BookCantRented("The book cannot be rented because it is out of stock.")

        book.decrease_unit()
        self.__rented_book = book

    def return_book(self) -> None:
       if not self.rented_book: raise NotBookToReturn("You do not have any books to return.")
       
       self.rented_book.increase_unit()
       self.__rented_book = None

    def __str__(self) -> None:
        print(f"----- User Normal {self.id} -----")
        return (
            f"User ID: {self.id}\n"
            f"User: {self.complete_name}\n"
            f"User Adress: {self.address}\n"
            f"Book Rented: {self.rented_book.name if self.rented_book else None}\n\n"
        )


class UserPremium(User):
    def __init__(self, name: str, surname: str, address: str) -> None:
        super().__init__(name=name, surname=surname, address=address)
        self.__rented_books: list[Book] = []

    @property
    def rented_books(self) -> list[Book]:
        return self.__rented_books
    
    def rent_book(self, book: Book) -> None:
        self.__is_valid_book(book=book)

        if book in self.rented_books: raise BookCantRented(f"You cannot rent this book because you already have {book.name} rented.")
        if not book.stock: raise BookCantRented("The book cannot be rented because it is out of stock.")
      
        book.decrease_unit()
        self.__rented_books.append(book)

    def return_book(self, book: Book) -> None:
       self.__is_valid_book(book=book)

       if not book in self.rented_books: raise BookCantReturn(f"You can't return the {book.name} book because you don't have it rented.")
       
       book.increase_unit()
       self.__rented_books.remove(book)

    def __str__(self) -> None:
        print(f"----- User Premium {self.id} -----")
        return (
            f"User ID: {self.id}\n"
            f"User: {self.complete_name}\n"
            f"User Adress: {self.address}\n"
            f"Books Rented: {self.__get_list_name_rented_books()}\n\n"
        )
    
    def __is_valid_book(self, book: Book) -> None:
        if not book or not isinstance(book, Book): raise BookNotValidError("You must enter a valid book to return.")

    def __get_list_name_rented_books(self) -> list[str]:
        return [book.name for book in self.rented_books]

def main() -> None:
    dracula_book = Book(name="Drácula", description="Es una novela de fantasía gótica escrita por Bram Stoker, publicada en 1897.", author="Bram Stoker", units=20)
    la_clase_de_griego_book = Book(name="LA CLASE DE GRIEGO", description="En Seúl, una mujer asiste a clases de griego antiguo.", author="KANG, HAN", units=1)
    gravity_falls_book = Book(name="Gravity Falls", description="Este libro está lleno de datos y confesiones escalofriantes para satisfacer tu curiosidad.", author="Alex Hirsch", units=5)

    user_normal = UserNormal(name="Pepe", surname="Alcachofaz", address="Calle False 123")
    user_normal_2 = UserNormal(name="Sergio", surname="Sorg", address="Calle False 12345")
    user_premium = UserPremium(name="Carlos", surname="Skere", address="Calle False 1234")

    user_normal.rent_book(book=dracula_book)
    
    user_premium.rent_book(book=la_clase_de_griego_book)
    user_premium.rent_book(book=gravity_falls_book)
    user_premium.rent_book(book=dracula_book)

    print(user_normal)
    print(user_normal_2)
    print(user_premium)

    print(dracula_book)
    print(la_clase_de_griego_book)
    print(gravity_falls_book)

if __name__ == "__main__":
    main()