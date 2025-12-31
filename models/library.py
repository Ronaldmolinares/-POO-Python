from exceptions.exception import (
    BookNotAvailableError,
    ExceptionLibrary,
    UserNotFoundError,
)
from models.book import Book
from users.user import User


class Library:
    def __init__(self, name: str) -> None:
        self.name = name
        self.books: list[Book] = []
        self.users: list[User] = []

    def books_available(self):
        if not self.books:
            return "No hay libros disponibles."
        return "\n".join(f"- {book.title}" for book in self.books if book.is_available)

    def library_users(self):
        return "\n".join(
            f"{u}, Libros Prestados: {u.libros_prestados}" for u in self.users
        )

    def search_user(self, value: str):
        for user in self.users:
            if user.id == value or user.name.lower() == value.lower():
                return user
        raise UserNotFoundError(f"Usuario con cédula : {value} no registrado.")

    def search_book(self, title: str):
        for book in self.books:
            if title.lower() == book.title.lower() and book.is_available:
                return book
        raise BookNotAvailableError(f"Libro: {title} no disponible o inexistente.")

    @staticmethod
    def validate_isbn(isbn: str):
        if len(isbn) < 13:
            raise ExceptionLibrary("ISBN invalido por longitud de caracteres")
        return True
