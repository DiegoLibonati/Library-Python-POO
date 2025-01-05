import logging

from src.models.Book import Book


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def test_create_book(book: Book, book_dict: dict[str, str | int]) -> None:
    assert book.name == book_dict["name"]
    assert book.description == book_dict["description"]
    assert book.author == book_dict["author"]
    assert book.units == book_dict["units"]
    assert book.banner_url == book_dict["banner_url"]

def test_banner_url_setter(book: Book) -> None:
    url = "https://google.com"

    assert book.banner_url != url

    book.banner_url = url

    assert book.banner_url == url

def test_decrease_unit_without_units(book_without_units: Book) -> None:
    assert book_without_units.units == 0

    book_without_units.decrease_unit()

    assert book_without_units.units == 0

def test_decrease_unit(book: Book, book_dict: dict[str, str | int]) -> None:
    current_units = book.units

    assert current_units == book_dict["units"]
    
    book.decrease_unit()

    assert book.units == current_units - 1

def test_increase_unit(book: Book, book_dict: dict[str, str | int]) -> None:
    current_units = book.units

    assert current_units == book_dict["units"]

    book.increase_unit()

    assert book.units == current_units + 1