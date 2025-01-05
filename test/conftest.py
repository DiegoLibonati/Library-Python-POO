import pytest

from src.models.Book import Book
from src.models.UserNormal import UserNormal
from src.models.UserPremium import UserPremium
from src.models.Library import Library

from test.constants import MOCK_BOOK
from test.constants import MOCK_BOOK_WITHOUT_UNITS
from test.constants import MOCK_USER
from test.constants import MOCK_LIBRARY

@pytest.fixture
def book(book_dict: dict[str, str | int]) -> Book:
    name = book_dict["name"]
    description = book_dict["description"]
    author = book_dict["author"]
    units = book_dict["units"]
    banner_url = book_dict["banner_url"]

    return Book(
        name=name, 
        description=description, 
        author=author, 
        units=units,
        banner_url=banner_url
    )

@pytest.fixture
def book_without_units(book_without_units_dict: dict[str, str | int]) -> Book:
    name = book_without_units_dict["name"]
    description = book_without_units_dict["description"]
    author = book_without_units_dict["author"]
    units = book_without_units_dict["units"]
    banner_url = book_without_units_dict["banner_url"]

    return Book(
        name=name, 
        description=description, 
        author=author, 
        units=units,
        banner_url=banner_url
    )

@pytest.fixture
def user_normal(user_dict: dict[str, str]) -> UserNormal:
    name = user_dict["name"]
    surname = user_dict["surname"]
    address = user_dict["address"]

    return UserNormal(
        name=name,
        surname=surname,
        address=address
    )

@pytest.fixture
def user_premium(user_dict: dict[str, str]) -> UserPremium:
    name = user_dict["name"]
    surname = user_dict["surname"]
    address = user_dict["address"]

    return UserPremium(
        name=name,
        surname=surname,
        address=address
    )

@pytest.fixture
def library(library_dict: dict[str, str]) -> Library:
    name = library_dict["name"]

    return Library(
        name=name,
    )

# Mocks
@pytest.fixture
def book_dict() -> dict[str, str | int]:
    return MOCK_BOOK

@pytest.fixture
def book_without_units_dict() -> dict[str, str | int]:
    return MOCK_BOOK_WITHOUT_UNITS

@pytest.fixture
def user_dict() -> dict[str, str]:
    return MOCK_USER

@pytest.fixture
def library_dict() -> dict[str, str]:
    return MOCK_LIBRARY