from users.user import User


class Teacher(User):
    def __init__(self, name: str, id: str, department: str):
        super().__init__(name, id)
        self.departement = department
        self.book_limit = None

    def __str__(self):
        return (
            f"Docente: {self.name}, Cédula: {self.id}, Departamento: {self.departement}"
        )

    def request_book(self, title: str):
        self.libros_prestados.append(title)
        return f"Prestamo exitoso: Libro {title}, Estudiante {self.name}."
