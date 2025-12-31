# 📚 Sistema de Gestión de Biblioteca

Sistema completo de gestión bibliotecaria desarrollado en Python utilizando principios de Programación Orientada a Objetos (POO). Permite administrar libros físicos y digitales, gestionar usuarios (estudiantes y docentes), controlar préstamos con fechas de vencimiento, y persistir datos en formato JSON.

## ✨ Características

- 📖 **Gestión de Libros**: Soporte para libros físicos (14 días de préstamo) y digitales (7 días)
- 👥 **Gestión de Usuarios**: Estudiantes (máximo 3 libros) y docentes (sin límite)
- 🔄 **Sistema de Préstamos**: Control de préstamos y devoluciones con fechas reales
- ⏰ **Alertas de Vencimiento**: Notifica préstamos vencidos y días restantes
- 📊 **Libros Populares**: Ranking de libros más prestados (≥5 préstamos)
- 💾 **Persistencia de Datos**: Guarda y carga datos en JSON con fechas de préstamo
- 🏭 **Factory Pattern**: Creación dinámica de libros según tipo
- 🔍 **Búsquedas**: Búsqueda de usuarios por nombre o cédula, libros por título

## 🗂️ Estructura del Proyecto

```
POO/
├── main.py                    # Aplicación principal con menú interactivo
├── refactor_main.py          # Versión refactorizada del main
├── library.json              # Archivo de persistencia de datos
├── README.md                 # Documentación del proyecto
├── pyproject.toml            # Configuración del proyecto
│
├── models/                   # Modelos principales
│   ├── __init__.py
│   ├── book.py              # Clase base Book con gestión de fechas
│   └── library.py           # Clase Library para gestión de biblioteca
│
├── books/                    # Tipos de libros
│   ├── __init__.py
│   ├── physical_book.py     # Libro físico (14 días máximo)
│   └── digital_book.py      # Libro digital (7 días máximo)
│
├── users/                    # Gestión de usuarios
│   ├── __init__.py
│   ├── base_user.py         # Clase base de usuario
│   ├── user.py              # Usuario genérico
│   ├── student.py           # Estudiante (límite de 3 libros)
│   └── teacher.py           # Docente (sin límite)
│
├── protocols/                # Protocolos de tipo
│   ├── __init__.py
│   ├── protocol_book.py     # Protocol para libros
│   └── protocol_applicant.py # Protocol para solicitantes
│
├── exceptions/               # Excepciones personalizadas
│   ├── __init__.py
│   └── exception.py         # Excepciones del sistema
│
├── factories/                # Patrón Factory
│   ├── __init__.py
│   └── book_factory.py      # Factory para crear libros
│
├── persistence/              # Capa de persistencia
│   ├── __init__.py
│   ├── persistence.py       # Manejo de JSON con fechas
│   └── data.py              # Datos de prueba (25 libros, 20 usuarios)
│
└── ejercicios/               # Archivos de práctica
    ├── practica.py
    └── refactor_main.py
```

## 🛠️ Tecnologías Utilizadas

- **Python 3.10+** (Type hints, Pattern matching)
- **JSON** para persistencia de datos
- **datetime** para gestión de fechas de préstamo
- **POO** (Herencia, Polimorfismo, Encapsulamiento)
- **Design Patterns** (Factory, Protocol)

## 📋 Requisitos

- Python 3.10 o superior
- Sin dependencias externas (solo biblioteca estándar)

## 🚀 Instalación

1. **Clonar el repositorio**
```bash
git clone <url-del-repositorio>
cd POO
```

2. **Crear entorno virtual (opcional pero recomendado)**
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac
```

3. **Ejecutar la aplicación**
```bash
python main.py
```

## 💻 Uso

### Menú Principal

```
==================================================
SISTEMA DE GESTIÓN DE BIBLIOTECA
==================================================
1. Crear Biblioteca
2. Crear Libro
3. Crear Usuario (Estudiante/Docente)
4. Prestar Libro
5. Devolver Libro
6. Ver Libros Populares
7. Ver Libros Disponibles
8. Ver Usuarios de la Biblioteca
9. Guardar Datos
10. Cargar Datos
0. Salir
==================================================
```

### Ejemplos de Uso

**Crear una biblioteca:**
```
Opción: 1
Nombre: Biblioteca Central
✓ Biblioteca 'Biblioteca Central' creada exitosamente.
```

**Prestar un libro:**
```
Opción: 4
Seleccionar usuario y libro
✓ El libro Python Crash Course ha sido prestado el 2025-12-31 12:42.
✓ Prestamo exitoso: Libro Python Crash Course, Estudiante Juan Pérez.
```

**Ver duración de préstamo:**
```python
libro.calculate_duration()
# Salida: "Días restantes: 10 de 14"
# o "⚠️ Préstamo VENCIDO hace 3 días"
```

## 🎯 Funcionalidades Principales

### 1. Gestión de Libros

- **Libros Físicos**: Máximo 14 días de préstamo
- **Libros Digitales**: Máximo 7 días de préstamo
- Cálculo automático de días restantes o vencimiento
- Registro de fecha exacta de préstamo

### 2. Gestión de Usuarios

- **Estudiantes**: Límite de 3 libros simultáneos, incluye carrera
- **Docentes**: Sin límite de préstamos, incluye departamento
- Búsqueda por nombre o identificación

### 3. Sistema de Préstamos

- Registro de fecha y hora de préstamo
- Cálculo de duración real (días y horas)
- Alertas de vencimiento automáticas
- Control de disponibilidad

### 4. Persistencia

- Guardado completo en JSON (libros, usuarios, fechas)
- Carga automática al iniciar la aplicación
- Opción de guardar antes de salir

### 5. Estadísticas

- Ranking de libros más populares (≥5 préstamos)
- Lista de libros disponibles
- Información de usuarios y sus préstamos actuales

## 🏗️ Arquitectura

### Principios de Diseño

- **SOLID**: Separación de responsabilidades, clases abiertas a extensión
- **DRY**: Reutilización de código mediante herencia
- **Factory Pattern**: Creación centralizada de objetos libro
- **Protocol Pattern**: Definición de contratos de tipo

### Jerarquía de Clases

```
BaseUser
    └── User
        ├── Student
        └── Teacher

Book
    ├── PhysicalBook
    └── DigitalBook
```

## 🔧 Características Técnicas

- **Type Hints**: Tipado estático completo
- **Dataclasses**: Uso de `__init__` y properties
- **Match-Case**: Pattern matching en menú (Python 3.10+)
- **Exception Handling**: Manejo robusto de errores
- **JSON Serialization**: Conversión de datetime a ISO format

## 📝 Excepciones Personalizadas

- `ExceptionLibrary`: Error general de biblioteca
- `BookNotAvailableError`: Libro no disponible para préstamo
- `UserNotFoundError`: Usuario no encontrado en el sistema
- `InvalidTitleError`: Título de libro inválido

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la [Licencia MIT](LICENSE).

## 👨‍💻 Autor

**Samir**
- Universidad: UPTC
- Semestre: 8
- Curso: Programación Orientada a Objetos

## 📧 Contacto

Para preguntas o sugerencias, por favor abre un issue en el repositorio.

---

⭐ Si te gusta este proyecto, no olvides darle una estrella en GitHub!
