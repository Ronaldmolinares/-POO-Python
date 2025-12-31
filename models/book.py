from datetime import datetime

from exceptions.exception import BookNotAvailableError


class Book:
    borrowed_books: list["Book"] = []

    def __init__(self, title: str, author: str, isbn: str, is_available: bool = True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available
        self.__popularity_counter: int = 0
        self.loan_date: datetime | None = None  # Fecha de préstamo

    def __str__(self):
        return f"Libro: {self.title} escrito por: {self.author} (ISBN: {self.isbn}) Disponibilidad: {self.is_available}"

    def lend_book(self) -> str:
        if not self.is_available:
            raise BookNotAvailableError(f"Libro: '{self.title}' no dispobible.")

        if self.is_available:
            self.is_available = False
            self.loan_date = datetime.now()  # Registrar fecha de préstamo
            self.book_popular()
            return f"El libro {self.title} ha sido prestado el {self.loan_date.strftime('%Y-%m-%d %H:%M')}."

    def return_book(self) -> str:
        if not self.is_available:
            self.is_available = True
            duracion_msg = ""
            if self.loan_date:
                dias = (datetime.now() - self.loan_date).days
                horas = ((datetime.now() - self.loan_date).seconds) // 3600
                duracion_msg = f" Duración del préstamo: {dias} días, {horas} horas."
                self.loan_date = None  # Limpiar fecha de préstamo
            return f"El libro {self.title} ha sido devuelto.{duracion_msg}"
        return "No se puede devolver un libro que no ha sido prestado."

    # def es_popular(self):
    #     return self.__popularity_counter > 5

    def book_popular(self) -> bool:
        self.__popularity_counter += 1
        if self.__popularity_counter >= 5 and self not in Book.borrowed_books:
            Book.borrowed_books.append(self)
            return True
        return False

    @property
    def popularity_counter(self):
        return self.__popularity_counter

    @popularity_counter.setter
    def popularity_counter(self, popularity_counter):
        if popularity_counter > 0:
            self.__popularity_counter = popularity_counter
        raise "El valor del contador de popularidad no puede ser menor que 0."

    @classmethod
    def create_book_not_available(cls, title: str, author: str, isbn: str):
        return cls(title, author, isbn, is_available=False)
