class Libro:
    def __init__(self, id_libro: int, titulo: str, autor: str,
                 anio: int, prestado: bool = False):

        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.prestado = prestado


    def __str__(self):
        return (
            f"id_libro: {self.id_libro}\n"
            f"titulo: {self.titulo}\n"
            f"autor: {self.autor}\n"
            f"anio: {self.anio}\n"
            f"prestado: {self.prestado}\n"
        )

    def prestar(self):
        self.prestado = True

    def devolver(self):
        self.prestado = False

class Biblioteca:
    def __init__(self, nombre: str, direccion: str):
        self.nombre = nombre
        self.direccion = direccion
        self.libros  = []

    def __str__(self):
        return (
            f"Nombre: {self.nombre}\n"
            f"Direccion: {self.direccion}\n"
        )

    def agregar_libro(self, libro: Libro):
        for l in self.libros:
            if l.id_libro == libro.id_libro:
                print("El libro ya existe")
                return
        self.libros.append(libro)

    def eliminar_libro(self, id_libro):
        for l in self.libros:
            if l.id_libro == id_libro:
                self.libros.remove(l)
                return
        print("No existe el libro en la lista")

    def listar_libros(self):
        for libro in self.libros:
            print(f"ID: {libro.id_libro} -Titulo: {libro.titulo}")

    def prestar_libro(self, id_libro):
        for libro in self.libros:
            if libro.id_libro == id_libro:
                libro.prestar()
                return
        print("No existe el libro en la lista")


    def filtrar_por_autor(self, autor):
        print("Libros del autor: " + autor)
        for libro in self.libros:
            if libro.autor == autor:
                print(libro.titulo)



def principal():

    bibliotecas = []

    while True:
        print("\nMENU PRINCIPAL BIBLIOTECA DEL LIBRO")
        print("1. Crear biblioteca")
        print("2. Listar biblioteca")
        print("3. Gestionar biblioteca")
        print("4. Salir")

        opcion = int(input("Opcion: "))

        if opcion == 1:
            nombre = input("Nombre: ")
            direccion = input("Direccion: ")

            biblioteca = Biblioteca(nombre, direccion)
            bibliotecas.append(biblioteca)
            print("Biblioteca creada correctamente")


        elif opcion == 2:
            print("\nLista de bibliotecas")
            for biblioteca in bibliotecas:
                print("-",biblioteca.nombre)

        elif opcion == 3:
            print("\nGestionar biblioteca")
            nombre_biblioteca = input("Nombre: ")

            for biblioteca in bibliotecas:
                if biblioteca.nombre == nombre_biblioteca:
                    menu_biblioteca(biblioteca)
                    break
            else:
                print("No existe el biblioteca")

        elif opcion == 4:
            break



def menu_biblioteca(biblioteca):

    while True:
        print(f"\nMenu para la biblioteca: {biblioteca.nombre}")
        print("1. Agregar libro")
        print("2. Eliminar libro")
        print("3. Prestar libro")
        print("4. Listar libros")
        print("5. Filtrar por autor")
        print("6. Volver al menu")

        opcion = int(input("Opcion: "))
        if opcion == 1:
            id_libro = int(input("ID de libro: "))
            nombre = input("Nombre: ")
            autor = input("Autor: ")
            anio = int(input("Anio: "))

            nuevo_libro= Libro(id_libro, nombre, autor, anio)

            biblioteca.agregar_libro(nuevo_libro)


        elif opcion == 2:
            id_libro = int(input("ID de libro: "))
            biblioteca.eliminar_libro(id_libro)
            print("Libro eliminado correctamente")

        elif opcion == 3:
            id_libro=int(input("ID de libro: "))
            biblioteca.prestar_libro(id_libro)

            print("Libro prestado correctamente")


        elif opcion == 4:
            print("\nLista de libros de la biblioteca")
            biblioteca.listar_libros()


        elif opcion == 5:
            autor=input("Autor: ")
            biblioteca.filtrar_por_autor(autor)


        elif opcion == 6:
            break


if __name__ == "__main__":
    principal()