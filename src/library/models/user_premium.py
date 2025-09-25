from library.models.book import Book
from library.models.user import User
from library.utils.exceptions import BookCantRented, BookCantReturn


class UserPremium(User):
    def __init__(self, name: str, surname: str, address: str) -> None:
        super().__init__(name=name, surname=surname, address=address)
        self.__rented_books: list[Book] = []

    @property
    def rented_books(self) -> list[Book]:
        return self.__rented_books

    def rent_book(self, book: Book) -> None:
        if book in self.rented_books:
            raise BookCantRented(
                f"You cannot rent this book because you already have {book.name} rented."
            )
        if not book.stock:
            raise BookCantRented(
                "The book cannot be rented because it is out of stock."
            )

        book.decrease_unit()
        self.__rented_books.append(book)

    def return_book(self, book: Book) -> None:
        if book not in self.rented_books:
            raise BookCantReturn(
                f"You can't return the {book.name} book because you don't have it rented."
            )

        book.increase_unit()
        self.__rented_books.remove(book)

    def _get_list_name_rented_books(self) -> list[str]:
        return [book.name for book in self.rented_books]

    def __str__(self) -> None:
        return (
            f"----- User Premium {self.id} -----\n"
            f"User ID: {self.id}\n"
            f"User: {self.complete_name}\n"
            f"User Adress: {self.address}\n"
            f"Books Rented: {self._get_list_name_rented_books()}\n\n"
        )


def main() -> None:
    dracula_book = Book(
        name="Drácula",
        description="Es una novela de fantasía gótica escrita por Bram Stoker, publicada en 1897.",
        author="Bram Stoker",
        units=20,
    )
    la_clase_de_griego_book = Book(
        name="LA CLASE DE GRIEGO",
        description="En Seúl, una mujer asiste a clases de griego antiguo.",
        author="KANG, HAN",
        units=1,
    )
    gravity_falls_book = Book(
        name="Gravity Falls",
        description="Este libro está lleno de datos y confesiones escalofriantes para satisfacer tu curiosidad.",
        author="Alex Hirsch",
        units=5,
    )

    user_premium = UserPremium(
        name="Carlos", surname="Skere", address="Calle False 1234"
    )

    user_premium.rent_book(book=la_clase_de_griego_book)
    user_premium.rent_book(book=gravity_falls_book)
    user_premium.rent_book(book=dracula_book)

    print(user_premium)

    print(dracula_book)
    print(la_clase_de_griego_book)
    print(gravity_falls_book)


if __name__ == "__main__":
    main()
