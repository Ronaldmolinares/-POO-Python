from users.base_user import BaseUser


class User(BaseUser):
    def __init__(self, name: str, id: str):
        self.name = name
        self.id = id
        self.libros_prestados: list[str] = []

    def __str__(self):
        return f"Usuario: {self.name}, cédula: {self.id}"

    def request_book(self, title: str):
        return f"Solicitud del libro {title} realizada."

    def return_book(self, title: str) -> str:
        # Buscar el libro sin importar mayúsculas/minúsculas
        libro_encontrado = None
        for libro in self.libros_prestados:
            if libro.lower() == title.lower():
                libro_encontrado = libro
                break

        if libro_encontrado is None:
            return f"Error:\n El libro: {title} no se encuentra en la lista de libros prestados del estudiante {self.name}."
        else:
            self.libros_prestados.remove(libro_encontrado)
            return f"Libro: {title} devuelto."
