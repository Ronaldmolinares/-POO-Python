from factories.book_factory import BookFactory
from models.book import Book
from models.library import Library

# from persistence import data
from persistence.persistence import Persistence
from users.student import Student
from users.teacher import Teacher

# library = Library(" ***** BIBLIOTECA DUITAMA COMFABOY ***** ")

# library.books = data.books
# library.users.extend(data.teachers)
# library.users.extend(data.students)

# persistencia = Persistence()
# persistencia.save_data(library)

# Variables globales para mantener el estado
library = None
users_dict = {}  # Diccionario para guardar usuarios por ID
books_dict = {}  # Diccionario para guardar libros por ISBN
persistence = Persistence()  # Instancia de persistencia


def show_menu():
    """Muestra el menú principal"""
    print("\n" + "=" * 50)
    print("SISTEMA DE GESTIÓN DE BIBLIOTECA")
    print("=" * 50)
    print("1. Crear Biblioteca")
    print("2. Crear Libro")
    print("3. Crear Usuario (Estudiante/Docente)")
    print("4. Prestar Libro")
    print("5. Devolver Libro")
    print("6. Ver Libros Populares")
    print("7. Ver Libros Disponibles")
    print("8. Ver Usuarios de la Biblioteca")
    print("9. Guardar Datos")
    print("10. Cargar Datos")
    print("0. Salir")
    print("=" * 50)


def crear_biblioteca():
    """Crea una nueva biblioteca"""
    global library
    nombre = input("Ingrese el nombre de la biblioteca: ")
    library = Library(nombre)
    print(f"✓ Biblioteca '{nombre}' creada exitosamente.")


def crear_libro():
    """Crea un nuevo libro usando el BookFactory"""
    global library
    if library is None:
        print("✗ Error: Primero debe crear una biblioteca.")
        return

    print("\nTipo de libro:")
    print("1. Físico")
    print("2. Digital")
    tipo_opcion = input("Seleccione el tipo (1-2): ")

    tipo = "physical" if tipo_opcion == "1" else "digital"
    titulo = input("Título del libro: ")
    autor = input("Autor del libro: ")
    isbn = input("ISBN del libro: ")

    try:
        libro = BookFactory.create_book(tipo, titulo, autor, isbn, True)
        library.books.append(libro)
        books_dict[isbn] = libro
        print(f"✓ Libro '{titulo}' creado y agregado a la biblioteca.")
    except ValueError as e:
        print(f"✗ Error: {e}")


def crear_usuario():
    """Crea un nuevo usuario (estudiante o docente)"""
    global library
    if library is None:
        print("✗ Error: Primero debe crear una biblioteca.")
        return

    print("\nTipo de usuario:")
    print("1. Estudiante")
    print("2. Docente")
    tipo_usuario = input("Seleccione el tipo (1-2): ")

    nombre = input("Nombre completo: ")
    id_usuario = input("Número de identificación: ")

    if tipo_usuario == "1":
        carrera = input("Carrera: ")
        usuario = Student(nombre, id_usuario, carrera)
    elif tipo_usuario == "2":
        departamento = input("Departamento: ")
        usuario = Teacher(nombre, id_usuario, departamento)
    else:
        print("✗ Opción inválida.")
        return

    library.users.append(usuario)
    users_dict[id_usuario] = usuario
    print(f"✓ Usuario creado: {usuario}")


def prestar_libro():
    """Presta un libro a un usuario"""
    if library is None:
        print("✗ Error: Primero debe crear una biblioteca.")
        return

    if not library.users:
        print("✗ Error: No hay usuarios registrados.")
        return

    if not library.books:
        print("✗ Error: No hay libros en la biblioteca.")
        return

    # Mostrar usuarios
    print("\nUsuarios disponibles:")
    for i, user in enumerate(library.users, 1):
        print(f"{i}. {user}")

    user_idx = int(input("\nSeleccione el usuario (número): ")) - 1
    if user_idx < 0 or user_idx >= len(library.users):
        print("✗ Usuario inválido.")
        return

    usuario = library.users[user_idx]

    # Mostrar libros disponibles
    print("\nLibros disponibles:")
    libros_disponibles = [libro for libro in library.books if libro.is_available]
    if not libros_disponibles:
        print("✗ No hay libros disponibles.")
        return

    for i, libro in enumerate(libros_disponibles, 1):
        print(f"{i}. {libro.title} - {libro.author} (ISBN: {libro.isbn})")

    libro_idx = int(input("\nSeleccione el libro (número): ")) - 1
    if libro_idx < 0 or libro_idx >= len(libros_disponibles):
        print("✗ Libro inválido.")
        return

    libro = libros_disponibles[libro_idx]

    # Prestar libro
    resultado_prestamo = libro.lend_book()
    resultado_usuario = usuario.request_book(libro.title)
    print(resultado_prestamo)
    print(resultado_usuario)


def devolver_libro():
    """Devuelve un libro prestado"""
    if library is None:
        print("✗ Error: Primero debe crear una biblioteca.")
        return

    if not library.users:
        print("✗ Error: No hay usuarios registrados.")
        return

    # Mostrar usuarios con libros prestados
    usuarios_con_libros = [u for u in library.users if u.libros_prestados]
    if not usuarios_con_libros:
        print("✗ No hay usuarios con libros prestados.")
        return

    print("\nUsuarios con libros prestados:")
    for i, user in enumerate(usuarios_con_libros, 1):
        print(f"{i}. {user.name} - Libros: {', '.join(user.libros_prestados)}")

    user_idx = int(input("\nSeleccione el usuario (número): ")) - 1
    if user_idx < 0 or user_idx >= len(usuarios_con_libros):
        print("✗ Usuario inválido.")
        return

    usuario = usuarios_con_libros[user_idx]

    if not usuario.libros_prestados:
        print("✗ Este usuario no tiene libros prestados.")
        return

    print("\nLibros prestados:")
    for i, libro_titulo in enumerate(usuario.libros_prestados, 1):
        print(f"{i}. {libro_titulo}")

    libro_idx = int(input("\nSeleccione el libro a devolver (número): ")) - 1
    if libro_idx < 0 or libro_idx >= len(usuario.libros_prestados):
        print("✗ Libro inválido.")
        return

    libro_titulo = usuario.libros_prestados[libro_idx]

    # Encontrar el libro en la biblioteca y devolverlo
    for libro in library.books:
        if libro.title.lower() == libro_titulo.lower():
            resultado_libro = libro.return_book()
            resultado_usuario = usuario.return_book(libro_titulo)
            print(resultado_libro)
            print(resultado_usuario)
            return

    print(f"✗ No se encontró el libro '{libro_titulo}' en la biblioteca.")


def ver_libros_populares():
    """Muestra los libros más prestados"""
    if not Book.borrowed_books:
        print("✗ No hay libros populares aún.")
        return

    print("\n" + "=" * 50)
    print("LIBROS POPULARES (Más prestados)")
    print("=" * 50)
    for libro in Book.borrowed_books:
        print(f"- {libro}")


def ver_libros_disponibles():
    """Muestra los libros disponibles en la biblioteca"""
    if library is None:
        print("✗ Error: Primero debe crear una biblioteca.")
        return

    if not library.books:
        print("✗ No hay libros en la biblioteca.")
        return

    libros_disponibles = library.books_available()
    if not libros_disponibles:
        print("✗ No hay libros disponibles en este momento.")
        return

    print("\n" + "=" * 50)
    print("LIBROS DISPONIBLES")
    print("=" * 50)
    # for titulo in libros_disponibles:
    #     print(f"- {titulo}")
    print(libros_disponibles)


def ver_usuarios():
    """Muestra los usuarios de la biblioteca"""
    if library is None:
        print("✗ Error: Primero debe crear una biblioteca.")
        return

    if not library.users:
        print("✗ No hay usuarios registrados.")
        return

    print("\n" + "=" * 50)
    print("USUARIOS DE LA BIBLIOTECA")
    print("=" * 50)
    print(library.library_users())


def guardar_datos():
    """Guarda los datos de la biblioteca en archivo JSON"""
    global library
    if library is None:
        print("✗ Error: No hay biblioteca para guardar.")
        return

    try:
        persistence.save_data(library)
        print("✓ Datos guardados exitosamente en 'library.json'.")
    except Exception as e:
        print(f"✗ Error al guardar datos: {e}")


def cargar_datos():
    """Carga los datos de la biblioteca desde archivo JSON"""
    global library, users_dict, books_dict
    try:
        library = persistence.load_data()

        # Actualizar diccionarios de usuarios y libros
        users_dict = {user.id: user for user in library.users}
        books_dict = {book.isbn: book for book in library.books}

        print(f"✓ Datos cargados exitosamente: {library.name}")
        print(f"  - {len(library.books)} libros")
        print(f"  - {len(library.users)} usuarios")
    except FileNotFoundError:
        print("✗ No se encontró archivo de datos previo.")
    except Exception as e:
        print(f"✗ Error al cargar datos: {e}")


def main():
    """Función principal con el menú interactivo"""
    # Intentar cargar datos al iniciar
    print("Intentando cargar datos guardados...")
    cargar_datos()

    while True:
        show_menu()
        opcion = input("\nSeleccione una opción: ")

        match opcion:
            case "1":
                crear_biblioteca()
            case "2":
                crear_libro()
            case "3":
                crear_usuario()
            case "4":
                prestar_libro()
            case "5":
                devolver_libro()
            case "6":
                ver_libros_populares()
            case "7":
                ver_libros_disponibles()
            case "8":
                ver_usuarios()
            case "9":
                guardar_datos()
            case "10":
                cargar_datos()
            case "0":
                # Preguntar si desea guardar antes de salir
                if library is not None:
                    guardar = input(
                        "\n¿Desea guardar los datos antes de salir? (s/n): "
                    )
                    if guardar.lower() == "s":
                        guardar_datos()
                print("\n¡Gracias por usar el sistema de biblioteca!")
                break
            case _:
                print("✗ Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
