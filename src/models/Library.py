from typing import Union
from typing import ValuesView

from src.models.Book import Book
from src.models.UserNormal import UserNormal
from src.models.UserPremium import UserPremium 
from src.utils.exceptions import BookNotFound
from src.utils.exceptions import BookNotValidError
from src.utils.exceptions import UserNotFound
from src.utils.exceptions import UserNotValidError
from src.utils.exceptions import UserAlreadyExists

class Library:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__books: dict[str, Book] = {}
        self.__users: dict[str, Union[UserNormal, UserPremium]] = {}

    @property
    def name(self) -> str:
        return self.__name

    @property
    def books(self) -> dict[str, Book]:
        return self.__books
    
    @property
    def users(self) -> dict[str, Union[UserNormal, UserPremium]]:
        return self.__users
    
    @property
    def books_values(self) -> ValuesView[Book]:
        return self.__books.values()
    
    @property
    def users_values(self) -> ValuesView[Union[UserNormal, UserPremium]]:
        return self.__users.values()


    def register_user(self, user: UserNormal | UserPremium) -> None:
        if not user or not isinstance(user, UserNormal | UserPremium): raise UserNotValidError("You must enter a valid user.")
        if user in self.users_values: raise UserAlreadyExists(f"The user with id {user.id} already exists.")
        self.__users[user.id] = user

    def remove_user(self, user: UserNormal | UserPremium) -> None:
        if not user or not isinstance(user, UserNormal | UserPremium): raise UserNotValidError("You must enter a valid user.")
        if not user in self.users_values: raise UserNotFound("This user was not found.")
        
        del self.__users[user.id]

    def add_book(self, book: Book) -> None:
        if not book or not isinstance(book, Book): raise BookNotValidError("You must enter a valid book to add.")
        self.__books[book.id] = book

    def remove_book(self, book: Book) -> None:
        if not book or not isinstance(book, Book): raise BookNotValidError("You must enter a valid book to add.")
        if not book in self.books_values: raise BookNotFound("This book was not found.")
        
        del self.__books[book.id]

    def rent_book(self, user: UserNormal | UserPremium, book: Book) -> None:
        if not user or not isinstance(user, UserNormal | UserPremium): raise UserNotValidError("You must enter a valid user.")
        if not book or not isinstance(book, Book): raise BookNotValidError("You must enter a valid book to add.")

        user.rent_book(book=book)

    def return_book(self, user: UserNormal | UserPremium, book: Book = None) -> None:
        if not user or not isinstance(user, UserNormal | UserPremium): raise UserNotValidError("You must enter a valid user.")
        if book and not isinstance(book, Book): raise BookNotValidError("You must enter a valid book to add.")

        if isinstance(user, UserPremium):
            user.return_book(book=book)
            return
        
        user.return_book()
        
    def str_users(self) -> None:
        print(f"----- Library Users {self.name} -----")
        for user in self.users_values:
            print(user)

    def str_books(self) -> None:
        print(f"----- Library Books {self.name} -----")
        for book in self.books_values:
            print(book)

    def __str__(self) -> str:
        return (
            f"----- Library {self.name} -----\n"
            f"Library Name: {self.name}\n"
            f"Library Users: {self.users_values}\n"
            f"Library Books: {self.books_values}\n\n"
        )

def main() -> None:
    # Library
    library = Library(name="Libreria LaRosca")

    # Books
    dracula_book = Book(name="Drácula", description="Es una novela de fantasía gótica escrita por Bram Stoker, publicada en 1897.", author="Bram Stoker", units=20)
    la_clase_de_griego_book = Book(name="LA CLASE DE GRIEGO", description="En Seúl, una mujer asiste a clases de griego antiguo.", author="KANG, HAN", units=1)
    gravity_falls_book = Book(name="Gravity Falls", description="Este libro está lleno de datos y confesiones escalofriantes para satisfacer tu curiosidad.", author="Alex Hirsch", units=5)

    # Users
    user_normal = UserNormal(name="Pepe", surname="Alcachofaz", address="Calle False 123")
    user_normal_2 = UserNormal(name="Sergio", surname="Sorg", address="Calle False 12345")
    user_premium = UserPremium(name="Carlos", surname="Skere", address="Calle False 1234")

    library.register_user(user=user_normal)
    library.register_user(user=user_normal_2)
    library.register_user(user=user_premium)

    library.add_book(dracula_book)
    library.add_book(la_clase_de_griego_book)
    library.add_book(gravity_falls_book)

    library.rent_book(user=user_normal, book=dracula_book)
    library.rent_book(user=user_premium, book=dracula_book)
    library.rent_book(user=user_premium, book=la_clase_de_griego_book)
    library.rent_book(user=user_premium, book=gravity_falls_book)

    library.return_book(user=user_normal)
    library.return_book(user=user_premium, book=dracula_book)

    print(library)
    library.str_users()
    library.str_books()

if __name__ == "__main__":
    main()