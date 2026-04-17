"""
EXAMEN TIPO 1: GESTOR DE BIBLIOTECA
Estructura base completa - Solo implementa los TODO
"""

class Libro:
    """Representa un libro en la biblioteca"""
    contador_libros = 0
    
    def __init__(self, titulo, autor, ano_publicacion, copias_disponibles):
        Libro.contador_libros += 1
        self.id_libro = Libro.contador_libros
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacion = ano_publicacion
        self.copias_disponibles = copias_disponibles
        self.copias_prestadas = 0

    def __str__(self):
        return (f"Libro {self.id_libro}: {self.titulo} - {self.autor} ({self.ano_publicacion}), "
                f"Disponibles: {self.copias_disponibles}, Prestadas: {self.copias_prestadas}")

    # TODO: Implementar método prestar
    def prestar(self):
        """Presta una copia del libro si hay disponibles"""
        if self.copias_disponibles <= 0:
            print(f"No hay copias disponibles de {self.titulo}")
            return False

        self.copias_disponibles-=1
        self.copias_prestadas+=1
        print(f"Copia {self.titulo} prestada")
        return True


    # TODO: Implementar método devolver
    def devolver(self):
        """Devuelve una copia del libro"""
        if self.copias_prestadas <= 0:
            print(f"No hay copias prestadas {self.titulo}")
            return False

        self.copias_disponibles+=1
        self.copias_prestadas-=1
        print(f"Copia de {self.titulo} devuelto")
        return True


class Usuario:
    """Representa un usuario de la biblioteca"""
    contador_usuarios = 0
    
    def __init__(self, nombre, nif, fecha_registro):
        Usuario.contador_usuarios += 1
        self.id_usuario = Usuario.contador_usuarios
        self.nombre = nombre
        self.nif = nif
        self.fecha_registro = fecha_registro
        self.libros_prestados = []  # Lista de libros que tiene prestados

    def __str__(self):
        return f"Usuario {self.id_usuario}: {self.nombre} ({self.nif}), Libros prestados: {len(self.libros_prestados)}"

    # TODO: Implementar método tomar_libro
    #Comprobar por el nombre si ya esta en la lista -> mostrar mensaje
    #Añadir libro .append() ->Mostrar mensaje

    def tomar_libro(self, libro):
        """El usuario toma un libro prestado"""
        if libro in self.libros_prestados:
            print(f"{self.nombre}ya tiene prestado el libro {libro.titulo}")
            return False

        self.libros_prestados.append(libro)
        print(f"{self.nombre} tomo {libro.titulo}")
        return True


    # TODO: Implementar método devolver_libro
    #Comprueba en la lista de libros prestado cada libro por un id introducido para borrarlo
    #borrar con .remove() -> mensaje
    #mensaje de error
    def devolver_libro(self, id_libro):
        """El usuario devuelve un libro"""
        for libro in self.libros_prestados:
            if libro.id_libro == id_libro:
                self.libros_prestados.remove(libro)

        print(f"El libro no esta en la lista")



    # TODO: Implementar método obtener_libros
    def obtener_libros(self):
        """Devuelve los libros que tiene prestados"""
        print(self.libros_prestados)


def mostrar_menu():
    print("\n" + "="*50)
    print("--- GESTOR DE BIBLIOTECA ---")
    print("="*50)
    print("1. Listar Libros")
    print("2. Listar Usuarios")
    print("3. Prestar Libro")
    print("4. Devolver Libro")
    print("5. Ver Libros de un Usuario")
    print("6. Buscar Libro por Autor")
    print("7. Salir")
    print("="*50)


# TODO: Implementar función buscar_libro_por_id
def buscar_libro_por_id(id_libro, libros):
    """Busca un libro por su ID"""
    if not libros:
        print(f"No hay libros en la biblioteca")
        return None


    for libro in libros:
        if id_libro == libro.id_libro:
            return libro
    print(f"Libro con ID:{libro.id_libro} no encontrado")
    return None


# TODO: Implementar función buscar_usuario_por_id
def buscar_usuario_por_id(id_usuario, usuarios):
    """Busca un usuario por su ID"""
    if not usuarios:
        print(f"No hay usuarios")
        return None

    for usuario in usuarios:
        if id_usuario == usuario.id_usuario:
            return usuario
    print(f"Usuario con ID: {usuario.id_usuario} no encontrado")
    return None




# TODO: Implementar función libros_por_autor
def libros_por_autor(autor, libros):
    """Devuelve todos los libros de un autor"""
    libros_encontrados=[]

    for libro in libros:
        if libro.autor.lower() == autor.lower():
            libros_encontrados.append(libro)

    if not libros_encontrados:
        print("No hay libros de este autor")

    return libros_encontrados



if __name__ == "__main__":
    # Listas globales
    libros = []
    usuarios = []

    # Crear libros de ejemplo
    libro1 = Libro("1984", "George Orwell", 1949, 3)
    libro2 = Libro("El Quijote", "Miguel de Cervantes", 1605, 2)
    libro3 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967, 4)
    libro4 = Libro("La metamorfosis", "Franz Kafka", 1915, 2)
    libro5 = Libro("El principito", "Antoine de Saint-Exupéry", 1943, 5)

    libros.extend([libro1, libro2, libro3, libro4, libro5])

    # Crear usuarios de ejemplo
    usuario1 = Usuario("Pedro García", "11111111A", "2024-01-15")
    usuario2 = Usuario("María López", "22222222B", "2024-02-20")
    usuario3 = Usuario("Juan Martínez", "33333333C", "2024-03-10")
    usuario4 = Usuario("Laura Fernández", "44444444D", "2024-01-30")

    usuarios.extend([usuario1, usuario2, usuario3, usuario4])

    # Programa principal
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Listar libros
            print("\nLibros en la biblioteca:")
            for libro in libros:
                print(f"  {libro}")

        elif opcion == "2":
            # Listar usuarios
            print("\nUsuarios registrados:")
            for usuario in usuarios:
                print(f"  {usuario}")

        elif opcion == "3":
            # Prestar libro
            try:
                print("\nLibros disponibles:")
                for libro in libros:
                    if libro.copias_disponibles > 0:
                        print(f"  [{libro.id_libro}] {libro.titulo} ({libro.copias_disponibles} copias)")
                
                id_libro = int(input("ID del libro a prestar: "))
                id_usuario = int(input("ID del usuario: "))
                
                # TODO: Implementar lógica para prestar libro
            except ValueError:
                print("❌ Debes introducir números válidos")
                pass

        elif opcion == "4":
            # Devolver libro
            try:
                id_usuario = int(input("ID del usuario: "))
                # TODO: Implementar lógica para devolver libro
                pass
            except ValueError:
                print("❌ Debes introducir números válidos")

        elif opcion == "5":
            # Ver libros de un usuario
            try:
                id_usuario = int(input("ID del usuario: "))
                # TODO: Implementar lógica para mostrar libros del usuario
                pass
            except ValueError:
                print("❌ Debes introducir números válidos")
        elif opcion == "6":
            # Buscar por autor
            autor = input("Nombre del autor: ")
            # TODO: Implementar lógica para buscar libros por autor
            libros_encontrados = libros_por_autor(autor,libros)

            if libros_encontrados:
                for libro in libros_encontrados:
                    print(libro)



        elif opcion == "7":
            print("\n¡Hasta luego!")
            break

        else:
            print("Opción no válida")
