from typing import Union

from Book import Book
from User import UserNormal
from User import UserPremium 
from exceptions import BookNotFound
from exceptions import BookNotValidError
from exceptions import UserNotFound
from exceptions import UserNotValidError
from exceptions import UserAlreadyExists

class Library:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__books: list[Book] = []
        self.__users: list[Union[UserNormal, UserPremium]] = []

    @property
    def name(self) -> str:
        return self.__name

    @property
    def books(self) -> list[Book]:
        return self.__books
    
    @property
    def users(self) -> list[Union[UserNormal, UserPremium]]:
        return self.__users

    def register_user(self, user: UserNormal | UserPremium) -> None:
        if not user or not isinstance(user, UserNormal | UserPremium): raise UserNotValidError("You must enter a valid user.")
        if user in self.users: raise UserAlreadyExists(f"The user with id {user.id} already exists.")
        self.__users.append(user)

    def remove_user(self, user: UserNormal | UserPremium) -> None:
        if not user or not isinstance(user, UserNormal | UserPremium): raise UserNotValidError("You must enter a valid user.")
        if not user in self.users: raise UserNotFound("This user was not found.")
        
        self.__users.remove(user)

    def remove_user_by_id(self, id_user: str) -> None:
        user = self.__get_user_by_id(id_user=id_user)
        self.__users.remove(user)

    def add_book(self, book: Book) -> None:
        if not book or not isinstance(book, Book): raise BookNotValidError("You must enter a valid book to add.")
        self.__books.append(book)

    def remove_book(self, book: Book) -> None:
        if not book or not isinstance(book, Book): raise BookNotValidError("You must enter a valid book to add.")
        if not book in self.books: raise BookNotFound("This book was not found.")
        self.__books.remove(book)

    def remove_book_by_name_and_author(self, name: str, author: str) -> None:
        book = self.__get_book_by_name_and_author(name=name, author=author)
        self.__books.remove(book)

    def rent_book(self, user: UserNormal | UserPremium, book: Book) -> None:
        if not user or not isinstance(user, UserNormal | UserPremium): raise UserNotValidError("You must enter a valid user.")
        user.rent_book(book=book)

    def return_book(self, user: UserNormal | UserPremium, book: Book = None) -> None:
        if not user or not isinstance(user, UserNormal | UserPremium): raise UserNotValidError("You must enter a valid user.")

        if isinstance(user, UserPremium) and (not book or not isinstance(book, Book)): raise BookNotValidError("You must enter a valid book to return.")

        if isinstance(user, UserPremium):
            user.return_book(book=book)
            return
        
        user.return_book()

    def str_users(self) -> None:
        print(f"----- Library Users {self.name} -----")
        for user in self.users:
            print(user)

    def str_books(self) -> None:
        print(f"----- Library Books {self.name} -----")
        for book in self.books:
            print(book)

    def __str__(self) -> str:
        print(f"----- Library {self.name} -----")
        return (
            f"Library Name: {self.name}\n"
            f"Library Users: {self.users}\n"
            f"Library Banner: {self.books}\n\n"
        )
    
    def __get_user_by_id(self, id_user: str) -> UserNormal | UserPremium:
        for user in self.users:
            if user.id == id_user:
                return user
        
        raise UserNotFound("A user with the given id was not found.")
    
    def __get_book_by_name_and_author(self, name: str, author: str) -> Book:
        for book in self.books:
            if book.name == name and book.author == author:
                return book
        
        raise BookNotFound("A book with the given name and author was not found.")
        

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