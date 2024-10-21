# Django REST API - Authors and Books

## Overview

This project is a simple Django REST API for managing authors and their books. It provides endpoints for creating, retrieving, updating, and deleting authors and books, with JSON Web Token (JWT) authentication to secure the API.

## Features

- **CRUD Operations** for Authors and Books
- JWT Authentication for secure access
- Easy to extend and modify
- Built with Django and Django REST Framework

## Technologies Used

- Django
- Django REST Framework
- Django REST Framework Simple JWT

## Getting Started

### Prerequisites

Make sure you have the following installed on your machine:

- Python 3.x
- Django
- Django REST Framework
- djangorestframework-simplejwt

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/authors-books-api.git
    ```
2. **Navigate to the project directory**:
    ```bash
    cd authors-books-api
    ```
3. **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```
4. **Activate the virtual environment**:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```
5. **Install the requirements**:
    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```
2. **Create a superuser** (optional, for accessing the Django admin):
    ```bash
    python manage.py createsuperuser
    ```
3. **Run the server**:
    ```bash
    python manage.py runserver
    ```

### API Endpoints

- **Authors**
    - `GET /authors/`: List all authors
    - `POST /authors/`: Create a new author
    - `GET /authors/{id}/`: Retrieve an author by ID
    - `PUT /authors/{id}/`: Update an author by ID
    - `DELETE /authors/{id}/`: Delete an author by ID

- **Books**
    - `GET /books/`: List all books
    - `POST /books/`: Create a new book
    - `GET /books/{id}/`: Retrieve a book by ID
    - `PUT /books/{id}/`: Update a book by ID
    - `DELETE /books/{id}/`: Delete a book by ID

### Authentication

To access the API endpoints, you'll need to obtain a JWT token. You can do this by sending a POST request to your authentication endpoint (assuming you have set up JWT authentication properly). Include your credentials in the body of the request.

## Running Tests

To run tests for this project, you can create test cases using Django's built-in testing framework. This project currently does not include any test cases, but you can add them to ensure the API works as expected.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. Suggestions and improvements are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to the Django and Django REST Framework communities for their resources and support.
