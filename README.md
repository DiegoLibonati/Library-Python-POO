# Library Python POO

## Educational Purpose

This project was created primarily for **educational and learning purposes**.
While it is well-structured and could technically be used in production, it is **not intended for commercialization**.
The main goal is to explore and demonstrate best practices, patterns, and technologies in software development.

## Getting Started

1. Clone the repository
2. Join to the correct path of the clone
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment (Windows): `venv\Scripts\activate`
5. Install dependencies: `pip install -r requirements.txt`
6. Install test dependencies: `pip install -r requirements.test.txt`
7. Install the package in editable mode: `pip install -e .`
8. Run the project: 
    1. From CLI: `library`
    2. Or import as a library in Python: `from library import Library, Book`

### Pre-Commit for Development

1. Once you're inside the virtual environment, let's install the hooks specified in the pre-commit. Execute: `pre-commit install`
2. Now every time you try to commit, the pre-commit lint will run. If you want to do it manually, you can run the command: `pre-commit run --all-files`

## Description

Library management system implemented in Python to manage books and users. The system includes classes for normal and premium users, allowing registration, deletion and management of book loans and returns. Each book can have units available, and its inventory status is managed. Custom validations and exceptions are also included to handle common errors, such as invalid or missing users or books.

IMPORTANT: This project was created for practice POO

## Technologies used

1. Python >= 3.11

## Libraries used

#### Requirements.txt

```
pre-commit==4.3.0
```

#### Requirements.test.txt

```
pytest==8.4.2
```

## Portfolio Link

[`https://www.diegolibonati.com.ar/#/project/Library-Python-POO`](https://www.diegolibonati.com.ar/#/project/Library-Python-POO)

## Testing

1. Join to the correct path of the clone
2. Activate the virtual environment: `venv\Scripts\activate`
3. Make sure the package is installed in editable mode: `pip install -e .`
4. Execute: `pytest --log-cli-level=INFO`

## Known Issues