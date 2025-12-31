from books.digital_book import DigitalBook
from books.physical_book import PhysicalBook
from users.student import Student
from users.teacher import Teacher

# Crear 25 libros (15 físicos y 10 digitales)
books = [
    # Libros físicos
    PhysicalBook("Cien años de soledad", "Gabriel García Márquez", "978-0307474728"),
    PhysicalBook("Don Quijote de la Mancha", "Miguel de Cervantes", "978-8491050407"),
    PhysicalBook("1984", "George Orwell", "978-0451524935"),
    PhysicalBook("El principito", "Antoine de Saint-Exupéry", "978-0156012195"),
    PhysicalBook("Crimen y castigo", "Fiódor Dostoyevski", "978-0143058144"),
    PhysicalBook("El gran Gatsby", "F. Scott Fitzgerald", "978-0743273565"),
    PhysicalBook("Orgullo y prejuicio", "Jane Austen", "978-0141439518"),
    PhysicalBook("La Odisea", "Homero", "978-0140268867"),
    PhysicalBook("Moby Dick", "Herman Melville", "978-0142437247"),
    PhysicalBook(
        "El amor en los tiempos del cólera", "Gabriel García Márquez", "978-0307389732"
    ),
    PhysicalBook("Los miserables", "Victor Hugo", "978-0451419439"),
    PhysicalBook("Anna Karenina", "León Tolstói", "978-0143035008"),
    PhysicalBook("El guardián entre el centeno", "J.D. Salinger", "978-0316769174"),
    PhysicalBook("Fahrenheit 451", "Ray Bradbury", "978-1451673319"),
    PhysicalBook("Matar un ruiseñor", "Harper Lee", "978-0061120084"),
    # Libros digitales
    DigitalBook("Clean Code", "Robert C. Martin", "978-0132350884"),
    DigitalBook("Python Crash Course", "Eric Matthes", "978-1593279288"),
    DigitalBook("The Pragmatic Programmer", "Andrew Hunt", "978-0135957059"),
    DigitalBook("Design Patterns", "Gang of Four", "978-0201633610"),
    DigitalBook("Introduction to Algorithms", "Thomas H. Cormen", "978-0262033844"),
    DigitalBook(
        "Artificial Intelligence: A Modern Approach", "Stuart Russell", "978-0136042594"
    ),
    DigitalBook("Deep Learning", "Ian Goodfellow", "978-0262035613"),
    DigitalBook("You Don't Know JS", "Kyle Simpson", "978-1491904244"),
    DigitalBook("JavaScript: The Good Parts", "Douglas Crockford", "978-0596517748"),
    DigitalBook("Head First Design Patterns", "Eric Freeman", "978-0596007126"),
]


# Crear 10 estudiantes
students = [
    Student("Juan Pérez", "1234567890", "Ingeniería de Sistemas"),
    Student("María González", "2345678901", "Medicina"),
    Student("Carlos Rodríguez", "3456789012", "Derecho"),
    Student("Ana Martínez", "4567890123", "Arquitectura"),
    Student("Luis Hernández", "5678901234", "Ingeniería Civil"),
    Student("Laura López", "6789012345", "Psicología"),
    Student("Pedro Sánchez", "7890123456", "Administración de Empresas"),
    Student("Carmen Díaz", "8901234567", "Biología"),
    Student("Jorge Torres", "9012345678", "Física"),
    Student("Isabel Ramírez", "0123456789", "Química"),
]


# Crear 5 docentes
teachers = [
    Teacher("Dr. Roberto Gómez", "T1001", "Departamento de Ciencias de la Computación"),
    Teacher("Dra. Patricia Fernández", "T1002", "Departamento de Matemáticas"),
    Teacher("Dr. Miguel Ángel Ruiz", "T1003", "Departamento de Física"),
    Teacher("Dra. Elena Castro", "T1004", "Departamento de Literatura"),
    Teacher("Dr. Fernando Morales", "T1005", "Departamento de Ingeniería"),
]
