from books.digital_book import DigitalBook
from books.physical_book import PhysicalBook
from models.book import Book


class BookFactory:
    @staticmethod
    def create_book(
        book_type: str, title: str, author: str, isbn: str, is_available: bool = True
    ) -> Book:
        if book_type.lower() == "physical":
            return PhysicalBook(title, author, isbn, is_available)
        elif book_type.lower() == "digital":
            return DigitalBook(title, author, isbn, is_available)
        else:
            raise ValueError(f"Tipo de libro '{book_type}' no válido")
