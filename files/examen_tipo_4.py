"""
EXAMEN TIPO 4: GESTOR DE AULAS Y ESTUDIANTES
Estructura base completa - Solo implementa los TODO
"""

class Aula:
    """Representa un aula en una escuela"""
    contador_aulas = 0
    
    def __init__(self, nombre, capacidad, nivel):
        Aula.contador_aulas += 1
        self.id_aula = Aula.contador_aulas
        self.nombre = nombre
        self.capacidad = capacidad
        self.nivel = nivel  # "Primaria", "Secundaria", "Bachillerato"
        self.estudiantes = []

    def __str__(self):
        return f"Aula {self.id_aula}: {self.nombre} ({self.nivel}) - {len(self.estudiantes)}/{self.capacidad} estudiantes"

    # TODO: Implementar método matricular_estudiante
    def matricular_estudiante(self, estudiante):
        """Matricula un estudiante en el aula"""
        pass

    # TODO: Implementar método expulsar_estudiante
    def expulsar_estudiante(self, id_estudiante):
        """Expulsa un estudiante del aula"""
        pass

    # TODO: Implementar método obtener_estudiantes
    def obtener_estudiantes(self):
        """Devuelve lista de estudiantes"""
        pass


class Estudiante:
    """Representa un estudiante"""
    contador_estudiantes = 0
    
    def __init__(self, nombre, edad, expediente):
        Estudiante.contador_estudiantes += 1
        self.id_estudiante = Estudiante.contador_estudiantes
        self.nombre = nombre
        self.edad = edad
        self.expediente = expediente  # "Regular", "Bueno", "Excelente"
        self.calificacion_media = 0.0
        self.aula_actual = None

    def __str__(self):
        aula_info = f"Aula {self.aula_actual.nombre}" if self.aula_actual else "Sin aula"
        return f"Estudiante {self.id_estudiante}: {self.nombre} ({self.edad} años) - Media: {self.calificacion_media}€ - {aula_info}"

    # TODO: Implementar método actualizar_calificacion
    def actualizar_calificacion(self, nueva_calificacion):
        """Actualiza la calificación media"""
        pass


def mostrar_menu():
    print("\n" + "="*50)
    print("--- GESTOR DE AULAS ---")
    print("="*50)
    print("1. Crear Aula")
    print("2. Registrar Estudiante")
    print("3. Matricular Estudiante en Aula")
    print("4. Ver Estudiantes de Aula")
    print("5. Actualizar Calificación")
    print("6. Listar Aulas")
    print("7. Salir")
    print("="*50)


# TODO: Implementar función buscar_aula_por_id
def buscar_aula_por_id(id_aula, aulas):
    """Busca un aula por su ID"""
    pass


# TODO: Implementar función buscar_estudiante_por_id
def buscar_estudiante_por_id(id_estudiante, estudiantes):
    """Busca un estudiante por su ID"""
    pass


# TODO: Implementar función aulas_llenas
def aulas_llenas(aulas):
    """Devuelve aulas que están llenas"""
    pass


if __name__ == "__main__":
    aulas = []
    estudiantes = []

    # Crear aulas
    a1 = Aula("3A Primaria", 25, "Primaria")
    a2 = Aula("2B Secundaria", 30, "Secundaria")
    a3 = Aula("1A Bachillerato", 35, "Bachillerato")

    aulas.extend([a1, a2, a3])

    # Crear estudiantes
    e1 = Estudiante("Carlos García", 10, "Regular")
    e2 = Estudiante("Ana López", 11, "Bueno")
    e3 = Estudiante("Miguel Rodríguez", 14, "Excelente")
    e4 = Estudiante("Isabel Martínez", 15, "Bueno")
    e5 = Estudiante("Diego López", 17, "Regular")

    estudiantes.extend([e1, e2, e3, e4, e5])

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Crear aula
            try:
                nombre = input("Nombre del aula: ")
                capacidad = int(input("Capacidad: "))
                nivel = input("Nivel (Primaria/Secundaria/Bachillerato): ")
                
                nueva_aula = Aula(nombre, capacidad, nivel)
                aulas.append(nueva_aula)
                print(f"✓ Aula '{nombre}' creada (ID: {nueva_aula.id_aula})")
            except ValueError:
                print("❌ Datos inválidos")

        elif opcion == "2":
            # Registrar estudiante
            try:
                nombre = input("Nombre del estudiante: ")
                edad = int(input("Edad: "))
                expediente = input("Expediente (Regular/Bueno/Excelente): ")
                
                nuevo_estudiante = Estudiante(nombre, edad, expediente)
                estudiantes.append(nuevo_estudiante)
                print(f"✓ Estudiante '{nombre}' registrado (ID: {nuevo_estudiante.id_estudiante})")
            except ValueError:
                print("❌ Datos inválidos")

        elif opcion == "3":
            # Matricular en aula
            try:
                id_aula = int(input("ID del aula: "))
                id_estudiante = int(input("ID del estudiante: "))
                
                # TODO: Implementar lógica
                pass

        elif opcion == "4":
            # Ver estudiantes de aula
            try:
                id_aula = int(input("ID del aula: "))
                # TODO: Implementar y mostrar
                pass

        elif opcion == "5":
            # Actualizar calificación
            try:
                id_estudiante = int(input("ID del estudiante: "))
                nueva_cal = float(input("Nueva calificación (0-10): "))
                
                # TODO: Implementar lógica
                pass

        elif opcion == "6":
            # Listar aulas
            print("\nAulas disponibles:")
            for aula in aulas:
                print(f"  {aula}")

        elif opcion == "7":
            print("\n¡Hasta luego!")
            break

        else:
            print("❌ Opción no válida")
