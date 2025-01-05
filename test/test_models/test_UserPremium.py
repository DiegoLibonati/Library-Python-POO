
import pytest

from src.models.Book import Book
from src.models.UserPremium import UserPremium

from src.utils.exceptions import BookCantRented
from src.utils.exceptions import BookCantReturn

def test_create_user_premium(user_premium: UserPremium, user_dict: dict[str, str]) -> None:
    assert user_premium.id
    assert user_premium.complete_name == user_dict["name"] + " " + user_dict["surname"]
    assert user_premium.address == user_dict["address"]
    assert not user_premium.rented_books

def test_rent_book_cant_rented(user_premium: UserPremium, book: Book) -> None:
    assert not user_premium.rented_books

    user_premium.rent_book(book=book)

    with pytest.raises(BookCantRented) as exc_info:
        user_premium.rent_book(book=book)

    assert str(exc_info.value) == f"You cannot rent this book because you already have {book.name} rented."

def test_rent_book_cant_rented_stock(user_premium: UserPremium, book_without_units: Book) -> None:
    assert not user_premium.rented_books

    with pytest.raises(BookCantRented) as exc_info:
        user_premium.rent_book(book=book_without_units)

    assert str(exc_info.value) == "The book cannot be rented because it is out of stock."

def test_rent_book(user_premium: UserPremium, book: Book) -> None:
    assert not user_premium.rented_books

    current_units = book.units

    user_premium.rent_book(book=book)

    assert book.units == current_units - 1
    assert book in user_premium.rented_books

def test_return_book_not_return(user_premium: UserPremium, book: Book) -> None:
    assert not user_premium.rented_books

    with pytest.raises(BookCantReturn) as exc_info:
        user_premium.return_book(book=book)

    assert str(exc_info.value) == f"You can't return the {book.name} book because you don't have it rented."

def test_return_book(user_premium: UserPremium, book: Book) -> None:
    assert not user_premium.rented_books

    current_units = book.units

    user_premium.rent_book(book=book)

    assert book in user_premium.rented_books
    assert book.units == current_units - 1

    user_premium.return_book(book=book)

    assert not user_premium.rented_books
    assert book.units == current_units

def test_get_list_name_rented_books(user_premium: UserPremium, book: Book) -> None:
    book_names = user_premium._get_list_name_rented_books()

    assert not user_premium.rented_books
    assert not book_names

    user_premium.rent_book(book=book)

    book_names = user_premium._get_list_name_rented_books()

    assert book_names == [book.name]