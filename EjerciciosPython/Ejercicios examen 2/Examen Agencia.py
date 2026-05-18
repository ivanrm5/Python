"""
PROYECTO AGENCIA DE VIAJES
Gestiona destinos, paquetes y reservas
Complejidad real pero funciones simples
"""


class Destino:
    """Representa un destino turístico"""

    contador_destinos = 0

    def __init__(self, nombre, pais, temperatura, atractivos):
        Destino.contador_destinos += 1
        self.id_destino = Destino.contador_destinos
        self.nombre = nombre
        self.pais = pais
        self.temperatura = temperatura  # Promedio en grados
        self.atractivos = atractivos  # Lista de atracciones
        self.puntuacion = 0.0  # Calificación promedio de turistas
        self.total_turistas = 0  # Número de turistas que visitaron

    def __str__(self):
        return (f"ID: {self.id_destino}: {self.nombre} ({self.pais}) - "
                f"Temp: {self.temperatura}°C, Puntuación: {self.puntuacion:.1f}/5, "
                f"Visitantes: {self.total_turistas}")

    def registrar_turista(self, calificacion):
        """Registra que un turista visitó el destino"""
        pass

    def obtener_atractivos(self):
        """Devuelve la lista de atractivos"""
        pass

    def es_recomendado(self):
        """Devuelve True si la puntuación es >= 4.0"""
        pass


class Paquete:
    """Representa un paquete de viaje"""

    contador_paquetes = 0

    def __init__(self, nombre, destino_id, duracion, precio_base, incluye):
        Paquete.contador_paquetes += 1
        self.id_paquete = Paquete.contador_paquetes
        self.nombre = nombre
        self.destino_id = destino_id  # ID del destino
        self.duracion = duracion  # Días
        self.precio_base = precio_base  # Precio por persona
        self.incluye = incluye  # Lista de servicios incluidos
        self.descuento = 0.0  # Porcentaje de descuento (0-100)
        self.disponible = True
        self.vendidos = 0  # Número de reservas vendidas

    def __str__(self):
        precio_final = self.precio_base * (1 - self.descuento / 100)
        return (f"ID: {self.id_paquete}: {self.nombre} - "
                f"{self.duracion} días, {precio_final}€, "
                f"Vendidos: {self.vendidos}")

    def aplicar_descuento(self, porcentaje):
        """Aplica un descuento al paquete"""
        pass

    def obtener_precio_final(self):
        """Calcula el precio con descuento"""
        pass

    def registrar_venta(self):
        """Registra que se vendió una reserva"""
        pass

    def obtener_servicios(self):
        """Devuelve los servicios incluidos"""
        pass


class Turista:
    """Representa un turista/cliente"""

    contador_turistas = 0

    def __init__(self, nombre, email, edad, pais_origen):
        Turista.contador_turistas += 1
        self.id_turista = Turista.contador_turistas
        self.nombre = nombre
        self.email = email
        self.edad = edad
        self.pais_origen = pais_origen
        self.reservas = []  # Lista de IDs de paquetes reservados
        self.total_gastado = 0.0
        self.destinos_visitados = []  # Lista de destinos visitados

    def __str__(self):
        return (f"ID: {self.id_turista}: {self.nombre} ({self.edad} años, {self.pais_origen}), "
                f"Reservas: {len(self.reservas)}, Gasto total: {self.total_gastado}€")

    def hacer_reserva(self, id_paquete):
        """Añade una reserva"""
        pass

    def cancelar_reserva(self, id_paquete):
        """Cancela una reserva"""
        pass

    def registrar_gasto(self, monto):
        """Añade un gasto realizado"""
        pass

    def registrar_destino_visitado(self, id_destino):
        """Registra que visitó un destino"""
        pass

    def obtener_reservas(self):
        """Devuelve la lista de reservas"""
        pass


# FUNCIONES GLOBALES

def mostrar_menu_principal():
    """Menú principal"""
    print("\n" + "=" * 70)
    print("--- GESTOR DE AGENCIA DE VIAJES ---")
    print("=" * 70)
    print("1. Ver Destinos Disponibles")
    print("2. Ver Paquetes de Viaje")
    print("3. Ver Turistas Registrados")
    print("4. Hacer Reserva")
    print("5. Cancelar Reserva")
    print("6. Registrar Viaje Completado")
    print("7. Ver Destinos Recomendados")
    print("8. Ver Turistas VIP (Más de 3 reservas)")
    print("9. Ver Estadísticas de Destinos")
    print("10. Buscar Turista")
    print("11. Salir")
    print("=" * 70)


def gestionar_turista(turista, paquetes):
    """Menú para gestionar un turista específico"""
    while True:
        print(f"\n--- Perfil de {turista.nombre} ---")
        print("1. Ver Reservas")
        print("2. Ver Destinos Visitados")
        print("3. Ver Total Gastado")
        print("4. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # TODO - Ver reservas del turista
            pass

        elif opcion == "2":
            # TODO - Ver destinos visitados
            pass

        elif opcion == "3":
            # TODO - Mostrar total gastado
            pass

        elif opcion == "4":
            break

        else:
            print("❌ Opción no válida")


def buscar_destino_por_id(id_destino, destinos):
    """Busca un destino por ID"""
    pass


def buscar_paquete_por_id(id_paquete, paquetes):
    """Busca un paquete por ID"""
    pass


def buscar_turista_por_id(id_turista, turistas):
    """Busca un turista por ID"""
    pass


def paquetes_por_destino(id_destino, paquetes):
    """Devuelve paquetes de un destino específico"""
    pass


def destinos_por_temperatura(temp_minima, destinos):
    """Devuelve destinos con temperatura >= temp_minima"""
    pass


def paquetes_con_descuento(paquetes):
    """Devuelve paquetes que tienen descuento"""
    pass


def destinos_recomendados(destinos):
    """Devuelve destinos recomendados (puntuación >= 4.0)"""
    pass


def turistas_vip(turistas):
    """Devuelve turistas con más de 3 reservas"""
    pass


def precio_promedio_paquetes(paquetes):
    """Calcula el precio promedio de todos los paquetes"""
    pass


def destino_mas_visitado(destinos):
    """Devuelve el destino con más visitantes"""
    pass


# PROGRAMA PRINCIPAL
if __name__ == "__main__":

    destinos = []
    paquetes = []
    turistas = []

    # Crear destinos
    dest1 = Destino("Barcelona", "España", 18, ["Sagrada Familia", "Park Güell", "Playas"])
    dest2 = Destino("París", "Francia", 12, ["Torre Eiffel", "Louvre", "Champs-Élysées"])
    dest3 = Destino("Tokio", "Japón", 16, ["Templos", "Tecnología", "Gastronomía"])
    dest4 = Destino("Marrakech", "Marruecos", 28, ["Medina", "Desierto", "Palacios"])
    dest5 = Destino("Ámsterdam", "Holanda", 10, ["Canales", "Museos", "Bicicletas"])
    dest6 = Destino("Bangkok", "Tailandia", 30, ["Templos", "Mercados", "Playas"])

    destinos.extend([dest1, dest2, dest3, dest4, dest5, dest6])

    # Crear paquetes
    paq1 = Paquete("Barcelona Deluxe", 1, 5, 1500, ["Hotel 5*", "Tours", "Comidas"])
    paq2 = Paquete("París Romántico", 2, 7, 2000, ["Hotel 4*", "Museos", "Cenas"])
    paq3 = Paquete("Tokio Express", 3, 10, 2500, ["Hotel 4*", "Tours", "Gastronomía"])
    paq4 = Paquete("Marrakech Aventura", 4, 6, 1200, ["Riad", "Excursiones", "Guía"])
    paq5 = Paquete("Ámsterdam Clásico", 5, 4, 1000, ["Hotel 3*", "Paseos", "Bicicletas"])
    paq6 = Paquete("Bangkok Sunset", 6, 8, 1800, ["Hotel 4*", "Templos", "Playas"])

    paquetes.extend([paq1, paq2, paq3, paq4, paq5, paq6])

    # Crear turistas
    tur1 = Turista("Juan García", "juan@email.com", 35, "España")
    tur2 = Turista("María López", "maria@email.com", 28, "Argentina")
    tur3 = Turista("Carlos Ruiz", "carlos@email.com", 45, "México")
    tur4 = Turista("Ana Martínez", "ana@email.com", 32, "Colombia")
    tur5 = Turista("Pedro Sánchez", "pedro@email.com", 50, "Portugal")
    tur6 = Turista("Laura Fernández", "laura@email.com", 26, "Chile")

    turistas.extend([tur1, tur2, tur3, tur4, tur5, tur6])

    # Añadir algunas reservas de ejemplo
    tur1.hacer_reserva(1)
    tur1.registrar_gasto(1500)
    tur1.hacer_reserva(2)
    tur1.registrar_gasto(2000)

    tur2.hacer_reserva(3)
    tur2.registrar_gasto(2500)

    tur3.hacer_reserva(4)
    tur3.registrar_gasto(1200)
    tur3.hacer_reserva(5)
    tur3.registrar_gasto(1000)

    # Registrar algunos destinos visitados
    dest1.registrar_turista(4.5)
    dest2.registrar_turista(4.8)
    dest4.registrar_turista(4.2)

    # Aplicar descuentos a algunos paquetes
    paq1.aplicar_descuento(10)
    paq4.aplicar_descuento(15)

    # Menú principal
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # TODO - Ver destinos
            # Mostrar todos los destinos
            pass

        elif opcion == "2":
            # TODO - Ver paquetes
            # Mostrar todos los paquetes
            pass

        elif opcion == "3":
            # TODO - Ver turistas
            # Mostrar todos los turistas
            pass

        elif opcion == "4":
            # TODO - Hacer reserva
            # Pedir: ID turista, ID paquete
            # Buscar ambos
            # Añadir reserva al turista
            # Registrar venta en paquete
            # Actualizar gasto del turista
            pass

        elif opcion == "5":
            # TODO - Cancelar reserva
            # Pedir: ID turista, ID paquete
            # Buscar turista
            # Cancelar reserva
            pass

        elif opcion == "6":
            # TODO - Registrar viaje completado
            # Pedir: ID turista, ID destino, calificación
            # Buscar turista y destino
            # Registrar gasto/destino/calificación
            pass

        elif opcion == "7":
            # TODO - Ver destinos recomendados
            # Llamar función
            # Mostrar lista
            pass

        elif opcion == "8":
            # TODO - Ver turistas VIP
            # Llamar función
            # Mostrar lista
            pass

        elif opcion == "9":
            # TODO - Ver estadísticas
            # Precio promedio paquetes
            # Destino más visitado
            # Mostrar
            pass

        elif opcion == "10":
            # TODO - Buscar turista
            # Pedir: ID turista
            # Buscar
            # Llamar: gestionar_turista()
            pass

        elif opcion == "11":
            print("\n¡Hasta luego!")
            break

        else:
            print("❌ Opción no válida")