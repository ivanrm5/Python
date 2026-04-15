"""
EXAMEN TIPO 3: GESTOR DE EVENTOS
Estructura base completa - Solo implementa los TODO
"""

class Evento:
    """Representa un evento"""
    contador_eventos = 0
    
    def __init__(self, nombre, fecha, ubicacion, capacidad_maxima):
        Evento.contador_eventos += 1
        self.id_evento = Evento.contador_eventos
        self.nombre = nombre
        self.fecha = fecha
        self.ubicacion = ubicacion
        self.capacidad_maxima = capacidad_maxima
        self.asistentes = []

    def __str__(self):
        return f"Evento {self.id_evento}: {self.nombre} - {self.fecha} ({self.ubicacion}), Asistentes: {len(self.asistentes)}/{self.capacidad_maxima}"

    # TODO: Implementar método registrar_asistente
    def registrar_asistente(self, persona):
        """Registra una persona en el evento si hay espacio"""
        pass

    # TODO: Implementar método cancelar_asistencia
    def cancelar_asistencia(self, id_persona):
        """Cancela la asistencia de una persona"""
        pass

    # TODO: Implementar método obtener_asistentes
    def obtener_asistentes(self):
        """Devuelve la lista de asistentes"""
        pass


class Persona:
    """Representa una persona que asiste a eventos"""
    contador_personas = 0
    
    def __init__(self, nombre, email, telefono):
        Persona.contador_personas += 1
        self.id_persona = Persona.contador_personas
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.eventos_registrados = []

    def __str__(self):
        return f"Persona {self.id_persona}: {self.nombre} ({self.email}), Eventos: {len(self.eventos_registrados)}"

    # TODO: Implementar método registrarse_en_evento
    def registrarse_en_evento(self, evento):
        """Se registra en un evento"""
        pass

    # TODO: Implementar método cancelar_evento
    def cancelar_evento(self, id_evento):
        """Cancela su asistencia a un evento"""
        pass


def mostrar_menu():
    print("\n" + "="*50)
    print("--- GESTOR DE EVENTOS ---")
    print("="*50)
    print("1. Crear Evento")
    print("2. Registrar Persona")
    print("3. Registrarse en Evento")
    print("4. Ver Evento")
    print("5. Ver Asistentes de Evento")
    print("6. Cancelar Asistencia")
    print("7. Salir")
    print("="*50)


# TODO: Implementar función buscar_evento_por_id
def buscar_evento_por_id(id_evento, eventos):
    """Busca un evento por su ID"""
    pass


# TODO: Implementar función buscar_persona_por_id
def buscar_persona_por_id(id_persona, personas):
    """Busca una persona por su ID"""
    pass


# TODO: Implementar función eventos_llenos
def eventos_llenos(eventos):
    """Devuelve lista de eventos llenos (sin capacidad)"""
    pass


if __name__ == "__main__":
    eventos = []
    personas = []

    # Crear eventos de ejemplo
    e1 = Evento("Conferencia Python", "2024-04-15", "Madrid", 100)
    e2 = Evento("Taller Django", "2024-04-20", "Barcelona", 50)
    e3 = Evento("Hackathon", "2024-05-01", "Valencia", 200)

    eventos.extend([e1, e2, e3])

    # Crear personas de ejemplo
    per1 = Persona("Juan García", "juan@example.com", "600123456")
    per2 = Persona("María López", "maria@example.com", "600234567")
    per3 = Persona("Pedro Martínez", "pedro@example.com", "600345678")
    per4 = Persona("Laura Fernández", "laura@example.com", "600456789")

    personas.extend([per1, per2, per3, per4])

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Crear evento
            try:
                nombre = input("Nombre del evento: ")
                fecha = input("Fecha (YYYY-MM-DD): ")
                ubicacion = input("Ubicación: ")
                capacidad = int(input("Capacidad máxima: "))
                
                nuevo_evento = Evento(nombre, fecha, ubicacion, capacidad)
                eventos.append(nuevo_evento)
                print(f"✓ Evento '{nombre}' creado (ID: {nuevo_evento.id_evento})")
            except ValueError:
                print("❌ Datos inválidos")

        elif opcion == "2":
            # Registrar persona
            try:
                nombre = input("Nombre: ")
                email = input("Email: ")
                telefono = input("Teléfono: ")
                
                nueva_persona = Persona(nombre, email, telefono)
                personas.append(nueva_persona)
                print(f"✓ Persona '{nombre}' registrada (ID: {nueva_persona.id_persona})")
            except ValueError:
                print("❌ Datos inválidos")

        elif opcion == "3":
            # Registrarse en evento
            try:
                id_evento = int(input("ID del evento: "))
                id_persona = int(input("ID de la persona: "))
                
                # TODO: Implementar lógica
                pass

        elif opcion == "4":
            # Ver evento
            print("\nEventos disponibles:")
            for evento in eventos:
                print(f"  {evento}")

        elif opcion == "5":
            # Ver asistentes
            try:
                id_evento = int(input("ID del evento: "))
                # TODO: Implementar y mostrar asistentes
                pass

        elif opcion == "6":
            # Cancelar asistencia
            try:
                id_persona = int(input("ID de la persona: "))
                id_evento = int(input("ID del evento: "))
                # TODO: Implementar lógica
                pass

        elif opcion == "7":
            print("\n¡Hasta luego!")
            break

        else:
            print("❌ Opción no válida")
