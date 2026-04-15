"""
EXAMEN TIPO 5: GESTOR DE PELÍCULAS Y CRÍTICAS
Estructura base completa - Solo implementa los TODO
"""

class Pelicula:
    """Representa una película"""
    contador_peliculas = 0
    
    def __init__(self, titulo, director, año, genero, duracion_minutos):
        Pelicula.contador_peliculas += 1
        self.id_pelicula = Pelicula.contador_peliculas
        self.titulo = titulo
        self.director = director
        self.año = año
        self.genero = genero
        self.duracion_minutos = duracion_minutos
        self.puntuacion_media = 0.0
        self.criticas = []

    def __str__(self):
        return f"Película {self.id_pelicula}: {self.titulo} ({self.año}) - Director: {self.director}, Puntuación: {self.puntuacion_media}/10"

    # TODO: Implementar método añadir_critica
    def añadir_critica(self, critica):
        """Añade una crítica a la película"""
        pass

    # TODO: Implementar método actualizar_puntuacion
    def actualizar_puntuacion(self):
        """Actualiza la puntuación media basada en las críticas"""
        pass

    # TODO: Implementar método obtener_criticas
    def obtener_criticas(self):
        """Devuelve lista de críticas"""
        pass


class Critica:
    """Representa una crítica de una película"""
    contador_criticas = 0
    
    def __init__(self, usuario, puntuacion, comentario):
        Critica.contador_criticas += 1
        self.id_critica = Critica.contador_criticas
        self.usuario = usuario
        self.puntuacion = puntuacion  # 1-10
        self.comentario = comentario
        self.likes = 0

    def __str__(self):
        return f"Crítica {self.id_critica}: {self.usuario} - {self.puntuacion}/10 - {self.comentario[:50]}..."

    # TODO: Implementar método dar_like
    def dar_like(self):
        """Incrementa los likes de la crítica"""
        pass


def mostrar_menu():
    print("\n" + "="*50)
    print("--- CRÍTICA DE PELÍCULAS ---")
    print("="*50)
    print("1. Añadir Película")
    print("2. Listar Películas")
    print("3. Añadir Crítica a Película")
    print("4. Ver Críticas de Película")
    print("5. Película mejor puntuada")
    print("6. Películas por género")
    print("7. Salir")
    print("="*50)


# TODO: Implementar función buscar_pelicula_por_id
def buscar_pelicula_por_id(id_pelicula, peliculas):
    """Busca una película por su ID"""
    pass


# TODO: Implementar función peliculas_por_genero
def peliculas_por_genero(genero, peliculas):
    """Devuelve películas de un género específico"""
    pass


# TODO: Implementar función pelicula_mejor_puntuada
def pelicula_mejor_puntuada(peliculas):
    """Devuelve la película con mejor puntuación"""
    pass


if __name__ == "__main__":
    peliculas = []

    # Crear películas de ejemplo
    p1 = Pelicula("Inception", "Christopher Nolan", 2010, "Ciencia Ficción", 148)
    p2 = Pelicula("Parasite", "Bong Joon-ho", 2019, "Drama", 132)
    p3 = Pelicula("The Shawshank Redemption", "Frank Darabont", 1994, "Drama", 142)
    p4 = Pelicula("Interstellar", "Christopher Nolan", 2014, "Ciencia Ficción", 169)
    p5 = Pelicula("Toy Story", "John Lasseter", 1995, "Animación", 81)

    peliculas.extend([p1, p2, p3, p4, p5])

    # Añadir críticas de ejemplo
    c1 = Critica("Juan García", 9, "Excelente película, muy entretenida")
    c2 = Critica("María López", 8, "Muy buena, aunque algo larga")
    p1.añadir_critica(c1)
    p1.añadir_critica(c2)
    p1.actualizar_puntuacion()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Añadir película
            try:
                titulo = input("Título: ")
                director = input("Director: ")
                año = int(input("Año: "))
                genero = input("Género: ")
                duracion = int(input("Duración (minutos): "))
                
                nueva_pelicula = Pelicula(titulo, director, año, genero, duracion)
                peliculas.append(nueva_pelicula)
                print(f"✓ Película '{titulo}' añadida (ID: {nueva_pelicula.id_pelicula})")
            except ValueError:
                print("❌ Datos inválidos")

        elif opcion == "2":
            # Listar películas
            print("\nPelículas disponibles:")
            for pelicula in peliculas:
                print(f"  {pelicula}")

        elif opcion == "3":
            # Añadir crítica
            try:
                id_pelicula = int(input("ID de la película: "))
                usuario = input("Tu nombre: ")
                puntuacion = int(input("Puntuación (1-10): "))
                comentario = input("Tu comentario: ")
                
                # TODO: Implementar lógica
                pass

        elif opcion == "4":
            # Ver críticas
            try:
                id_pelicula = int(input("ID de la película: "))
                # TODO: Implementar y mostrar críticas
                pass

        elif opcion == "5":
            # Película mejor puntuada
            # TODO: Implementar y mostrar
            pass

        elif opcion == "6":
            # Películas por género
            genero = input("Género a buscar: ")
            # TODO: Implementar y mostrar
            pass

        elif opcion == "7":
            print("\n¡Hasta luego!")
            break

        else:
            print("❌ Opción no válida")
