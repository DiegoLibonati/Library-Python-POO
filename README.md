# Library Python POO

## Getting Started

1. Clone the repository
2. Join to the correct path of the clone
3. Execute: `python -m venv venv`
4. Execute in Windows: `venv\Scripts\activate`
5. Execute: `pip install -r requirements.txt`
6. Execute: `pip install -r requirements.test.txt`
7. Use `python -m src.models.Library` -> everything in main of Library.py will be executed.

## Description

Library management system implemented in Python to manage books and users. The system includes classes for normal and premium users, allowing registration, deletion and management of book loans and returns. Each book can have units available, and its inventory status is managed. Custom validations and exceptions are also included to handle common errors, such as invalid or missing users or books.

IMPORTANT: This project was created for practice POO

## Technologies used

1. Python

## Libraries used

#### Requirements.txt

```
No 3rd libraries used.
```

#### Requirements.test.txt

```
pytest
```

## Portfolio Link

[`https://www.diegolibonati.com.ar/#/project/Library-Python-POO`](https://www.diegolibonati.com.ar/#/project/Library-Python-POO)

## Testing

1. Join to the correct path of the clone
2. Execute in Windows: `venv\Scripts\activate`
3. Execute: `pytest --log-cli-level=INFO`
