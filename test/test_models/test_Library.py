import pytest

from src.models.Library import Library
from src.models.Book import Book
from src.models.UserNormal import UserNormal
from src.models.UserPremium import UserPremium
from src.utils.exceptions import UserNotValidError
from src.utils.exceptions import UserAlreadyExists
from src.utils.exceptions import UserNotFound
from src.utils.exceptions import BookNotValidError
from src.utils.exceptions import BookNotFound


def test_create_library(library: Library, library_dict: dict[str, str]) -> None:
    assert not library.books
    assert not library.users
    assert library.name == library_dict["name"]

def test_register_user_invalid_user(library: Library) -> None:
    with pytest.raises(UserNotValidError) as exc_info:
        library.register_user(user="a")

    assert str(exc_info.value) == "You must enter a valid user."

def test_register_user_already_user_exists(library: Library, user_normal: UserNormal) -> None:
    library.register_user(user=user_normal)

    with pytest.raises(UserAlreadyExists) as exc_info:
        library.register_user(user=user_normal)

    assert str(exc_info.value) == f"The user with id {user_normal.id} already exists."

def test_register_user(library: Library, user_normal: UserNormal) -> None:
    assert not library.users

    library.register_user(user=user_normal)

    assert user_normal in library.users

def test_remove_user_invalid_user(library: Library) -> None:
    with pytest.raises(UserNotValidError) as exc_info:
        library.remove_user(user="a")

    assert str(exc_info.value) == "You must enter a valid user."

def test_remove_user_not_user_exists(library: Library, user_normal: UserNormal) -> None:
    with pytest.raises(UserNotFound) as exc_info:
        library.remove_user(user=user_normal)

    assert str(exc_info.value) == "This user was not found."

def test_remove_user(library: Library, user_normal: UserNormal) -> None:
    assert not library.users

    library.register_user(user=user_normal)

    assert user_normal in library.users

    library.remove_user(user=user_normal)

    assert not library.users

def test_remove_user_by_id(library: Library, user_normal: UserNormal) -> None:
    assert not library.users

    library.register_user(user=user_normal)

    assert user_normal in library.users

    library.remove_user_by_id(id_user=user_normal.id)

    assert not library.users

def test_add_book_invalid_book(library: Library) -> None:
    with pytest.raises(BookNotValidError) as exc_info:
        library.add_book(book="a")

    assert str(exc_info.value) == "You must enter a valid book to add."

def test_add_book(library: Library, book: Book) -> None:
    assert not library.books

    library.add_book(book=book)

    assert book in library.books

def test_remove_book_invalid_book(library: Library) -> None:
    with pytest.raises(BookNotValidError) as exc_info:
        library.remove_book(book="a")

    assert str(exc_info.value) == "You must enter a valid book to add."

def test_remove_book_not_book_exists(library: Library, book: Book) -> None:
    with pytest.raises(BookNotFound) as exc_info:
        library.remove_book(book=book)

    assert str(exc_info.value) == "This book was not found."

def test_remove_book(library: Library, book: Book) -> None:
    assert not library.books

    library.add_book(book=book)

    assert book in library.books

    library.remove_book(book=book)

    assert not library.books

def test_remove_book_by_name_and_author(library: Library, book: Book) -> None:
    library.add_book(book=book)

    assert book in library.books

    library.remove_book_by_name_and_author(name=book.name, author=book.author)

    assert not library.books

def test_rent_book_invalid_user(library: Library, book: Book) -> None:
    with pytest.raises(UserNotValidError) as exc_info:
        library.rent_book(user="a", book=book)

    assert str(exc_info.value) == "You must enter a valid user."

def test_rent_book_invalid_book(library: Library, user_normal: UserNormal) -> None:
    with pytest.raises(BookNotValidError) as exc_info:
        library.rent_book(user=user_normal, book="a")

    assert str(exc_info.value) == "You must enter a valid book to add."

def test_rent_book(library: Library, user_normal: UserNormal, book: Book) -> None:
    library.rent_book(user=user_normal, book=book)

    assert user_normal.rented_book == book

def test_return_book_invalid_user(library: Library, book: Book) -> None:
    with pytest.raises(UserNotValidError) as exc_info:
        library.return_book(user="a", book=book)

    assert str(exc_info.value) == "You must enter a valid user."

def test_return_book_invalid_book(library: Library, user_normal: UserNormal) -> None:
    with pytest.raises(BookNotValidError) as exc_info:
        library.return_book(user=user_normal, book="a")

    assert str(exc_info.value) == "You must enter a valid book to add."

def test_return_book_user_normal(library: Library, user_normal: UserNormal, book: Book) -> None:
    library.rent_book(user=user_normal, book=book)

    assert user_normal.rented_book == book

    library.return_book(user=user_normal, book=book)

    assert not user_normal.rented_book

def test_return_book_user_premium(library: Library, user_premium: UserPremium, book: Book) -> None:
    library.rent_book(user=user_premium, book=book)

    assert book in user_premium.rented_books

    library.return_book(user=user_premium, book=book)

    assert not user_premium.rented_books

def test_get_user_by_id_not_found(library: Library) -> None:
    with pytest.raises(UserNotFound) as exc_info:
        library._get_user_by_id(id_user="a")

    assert str(exc_info.value) == "A user with the given id was not found."

def test_get_user_by_id(library: Library, user_normal: UserNormal) -> None:
    library.register_user(user=user_normal)

    user = library._get_user_by_id(id_user=user_normal.id)

    assert user == user_normal

def test_get_book_by_name_and_author_not_found(library: Library) -> None:
    with pytest.raises(BookNotFound) as exc_info:
        library._get_book_by_name_and_author(name="a", author="b")

    assert str(exc_info.value) == "A book with the given name and author was not found."

def test_get_book_by_name_and_author(library: Library, book: Book) -> None:
    library.add_book(book=book)

    book_by_name_and_author = library._get_book_by_name_and_author(name=book.name, author=book.author)

    assert book_by_name_and_author == book

