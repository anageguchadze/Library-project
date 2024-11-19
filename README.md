# Django REST API - Authors and Books

# Django Book and Author API

A simple RESTful API built with Django and Django REST Framework (DRF) to manage books and authors, with token-based authentication using Django Simple JWT.

## Features
- **Authors**: Create and list authors with their name and nationality.
- **Books**: Create and list books associated with authors.
- **Authentication**: Protected endpoints for books, requiring JWT authentication.

## Requirements
- Python 3.x
- Django 4.x
- Django REST Framework
- Django Simple JWT

## Installation

Clone the repository:
https://github.com/anageguchadze/Library-project.git

Install dependencies:
pip install -r requirements.txt

Run migrations:
python manage.py migrate

Start the development server:
python manage.py runserver
Endpoints
Authors
GET /authors/: List all authors.
POST /authors/: Create a new author. Requires name and nationality fields.
Books
GET /books/: List all books (requires authentication).
POST /books/: Create a new book (requires authentication). Requires title and author fields.
Running Tests

Run the test suite using:
python manage.py test
Admin Panel
Access the admin panel at /admin/ to manage authors and books directly.

License
This project is licensed under the MIT License.


