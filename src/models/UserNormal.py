from src.models.Book import Book
from src.models.User import User

from src.utils.exceptions import BookCantRented
from src.utils.exceptions import NotBookToReturn


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
        return (
            f"----- User Normal {self.id} -----\n"
            f"User ID: {self.id}\n"
            f"User: {self.complete_name}\n"
            f"User Adress: {self.address}\n"
            f"Book Rented: {self.rented_book.name if self.rented_book else None}\n\n"
        )

def main() -> None:
    dracula_book = Book(name="Drácula", description="Es una novela de fantasía gótica escrita por Bram Stoker, publicada en 1897.", author="Bram Stoker", units=20)
    la_clase_de_griego_book = Book(name="LA CLASE DE GRIEGO", description="En Seúl, una mujer asiste a clases de griego antiguo.", author="KANG, HAN", units=1)
    gravity_falls_book = Book(name="Gravity Falls", description="Este libro está lleno de datos y confesiones escalofriantes para satisfacer tu curiosidad.", author="Alex Hirsch", units=5)

    user_normal = UserNormal(name="Pepe", surname="Alcachofaz", address="Calle False 123")
    user_normal_2 = UserNormal(name="Sergio", surname="Sorg", address="Calle False 12345")

    user_normal.rent_book(book=dracula_book)
    
    print(user_normal)
    print(user_normal_2)

    print(dracula_book)
    print(la_clase_de_griego_book)
    print(gravity_falls_book)


if __name__ == "__main__":
    main()