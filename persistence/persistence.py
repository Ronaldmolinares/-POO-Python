import json
from datetime import datetime

from models.book import Book
from models.library import Library
from users.student import Student
from users.teacher import Teacher


class Persistence:
    def __init__(self, file="library.json") -> None:
        self.file = file

    def save_data(self, library):
        data = {
            "name": library.name,
            "books": [
                {
                    "title": book.title,
                    "author": book.author,
                    "isbn": book.isbn,
                    "is_available": book.is_available,
                    "loan_date": book.loan_date.isoformat() if book.loan_date else None,
                }
                for book in library.books
            ],
            "users": [
                {
                    "name": user.name,
                    "id": user.id,
                    "libros_prestados": user.libros_prestados,
                    "tipo": "estudiante" if isinstance(user, Student) else "docente",
                    "carrera": user.carrera if isinstance(user, Student) else None,
                    "departamento": user.departement
                    if isinstance(user, Teacher)
                    else None,
                }
                for user in library.users
            ],
            "saving_date": datetime.now().isoformat(),
        }
        with open(self.file, "w", encoding="utf_8") as file_write:
            json.dump(data, file_write, indent=4, ensure_ascii=False)

    def load_data(self):
        with open(self.file, "r", encoding="utf_8") as file_read:
            data = json.load(file_read)

        library = Library(data["name"])
        for data_book in data["books"]:
            book = Book(
                title=data_book["title"],
                author=data_book["author"],
                isbn=data_book["isbn"],
                is_available=data_book["is_available"],
            )
            # Restaurar loan_date si existe
            if data_book.get("loan_date"):
                book.loan_date = datetime.fromisoformat(data_book["loan_date"])
            library.books.append(book)

        for data_user in data["users"]:
            if data_user["tipo"] == "estudiante":
                user = Student(data_user["name"], data_user["id"], data_user["carrera"])
            else:
                user = Teacher(
                    data_user["name"], data_user["id"], data_user["departamento"]
                )

            user.libros_prestados = data_user["libros_prestados"]
            library.users.append(user)

        return library
