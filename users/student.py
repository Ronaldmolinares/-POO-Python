from exceptions.exception import InvalidTitleError
from users.user import User


class Student(User):
    def __init__(self, name: str, id: str, carrera: str):
        super().__init__(name, id)
        self.carrera = carrera
        self.limite_libros = 3

    def __str__(self):
        return f"Estudiante: {self.name}, Cédula: {self.id}, Carrera: {self.carrera}"

    def request_book(self, title: str):
        if not title:
            raise InvalidTitleError("Titulo no valido.")
        if len(self.libros_prestados) < self.limite_libros:
            self.libros_prestados.append(title)
            return f"Prestamo exitoso: Libro {title}, Estudiante {self.name}."
        else:
            return f"No se pueden prestar mas de {self.limite_libros} libros a un mismo estudiante."

    @classmethod
    def specific_career(cls, name: str, id: str):
        return cls(name, id, carrera="Ingenieria Civil")
