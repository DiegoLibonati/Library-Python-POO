import pytest

from library import Book, BookCantRented, NotBookToReturn, UserNormal


def test_create_user_normal(user_normal: UserNormal, user_dict: dict[str, str]) -> None:
    assert user_normal.id
    assert user_normal.complete_name == user_dict["name"] + " " + user_dict["surname"]
    assert user_normal.address == user_dict["address"]
    assert not user_normal.rented_book


def test_rent_book_cant_rented(user_normal: UserNormal, book: Book) -> None:
    assert not user_normal.rented_book

    user_normal.rent_book(book=book)

    with pytest.raises(BookCantRented) as exc_info:
        user_normal.rent_book(book=book)

    assert (
        str(exc_info.value)
        == f"You cannot rent another book, you must return {book.name} before renting another one."
    )


def test_rent_book_cant_rented_stock(
    user_normal: UserNormal, book_without_units: Book
) -> None:
    assert not user_normal.rented_book

    with pytest.raises(BookCantRented) as exc_info:
        user_normal.rent_book(book=book_without_units)

    assert (
        str(exc_info.value) == "The book cannot be rented because it is out of stock."
    )


def test_rent_book(user_normal: UserNormal, book: Book) -> None:
    assert not user_normal.rented_book

    current_units = book.units

    user_normal.rent_book(book=book)

    assert book.units == current_units - 1
    assert user_normal.rented_book == book


def test_return_book_not_return(user_normal: UserNormal) -> None:
    assert not user_normal.rented_book

    with pytest.raises(NotBookToReturn) as exc_info:
        user_normal.return_book()

    assert str(exc_info.value) == "You do not have any books to return."


def test_return_book(user_normal: UserNormal, book: Book) -> None:
    assert not user_normal.rented_book

    current_units = book.units

    user_normal.rent_book(book=book)

    assert user_normal.rented_book == book
    assert book.units == current_units - 1

    user_normal.return_book()

    assert not user_normal.rented_book
    assert book.units == current_units
