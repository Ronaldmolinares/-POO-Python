from typing import Protocol


class BookProtocol(Protocol):
    def calculate_duration(self) -> str:
        """Metodo para calcular la duración de prestamo de un libro"""
        ...

    def lend_book(self) -> str:
        """Método para prestar un libro"""
        ...
