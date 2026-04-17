"""
PROYECTO GESTOR DE HOTEL
Gestiona hoteles, habitaciones y clientes
Estructura similar a centro comercial pero más compleja
"""

class Hotel:
    """Representa un hotel del grupo"""
    contador_hoteles=0

    # TODO Constructor y Atributo Estático
    def __init__(self, nombre, ciudad, numero_habitaciones, categoria):
        Hotel.contador_hoteles+=1
        self.id_hotel = Hotel.contador_hoteles
        self.nombre=nombre
        self.ciudad=ciudad
        self.numero_habitaciones=numero_habitaciones
        self.categoria=categoria
        self.huespedes_actuales=[]
        self.ocupacion_actual=0


    def __str__(self):
        return (f"Hotel {self.id_hotel}: {self.nombre} ({self.ciudad}) - Categoría: {self.categoria}*, "
                f"Ocupación: {self.ocupacion_actual}/{self.numero_habitaciones}")

    # TODO Método agregar_cliente_habitacion
    # Parámetro: cliente
    # Acción: Añade cliente a lista de huespedes
    def agregar_cliente_habitacion(self, cliente):
        if cliente in self.huespedes_actuales:
            print(f"{cliente.nombre} ya esta hospedado en el hotel {self.nombre}")
            return

        self.huespedes_actuales.append(cliente)
        self.ocupacion_actual+=1



    # TODO Método liberar_habitacion
    # Parámetro: id_cliente
    # Acción: Quita cliente de la lista
    def liberar_habitacion(self):
        pass

    # TODO Método obtener_huespedes
    # Devuelve: Lista de huéspedes actuales
    def obtener_huespedes(self):
        pass

class Cliente:
    """Representa un cliente que se hospeda en un hotel"""
    contador_clientes=0

    # TODO Constructor y Atributo Estático
    def __init__(self, nombre, pasaporte, email, edad):
        Cliente.contador_clientes+=1
        self.id_cliente=Cliente.contador_clientes
        self.nombre=nombre
        self.pasaporte=pasaporte
        self.email=email
        self.edad=edad
        self.total_noches = 0
        self.total_gastado = 0.0
        self.hotel_actual= None


    def __str__(self):
        return (f"Cliente {self.id_cliente}: {self.nombre}, {self.edad} años, "
                f"Total noches: {self.total_noches}, Total gastado: {self.total_gastado}€")

    # TODO Método registrar_hospedaje
    # Parámetros: numero_noches, precio_noche
    # Acción: Incrementa total_noches, calcula gasto
    def registrar_hospedaje(self):
        pass

    # TODO Método solicitar_servicio_extra
    # Parámetro: precio_servicio
    # Acción: Suma dinero a total_gastado
    def solicitar_servicio_extra(self):
        pass

    # TODO Método checkout
    # Acción: Devuelve el total a pagar y resetea datos
    def checkout(self):
        pass

# FUNCIONES GLOBALES

def mostrar_menu_principal():
    """Muestra el menú principal del centro de hoteles"""
    print("\n" + "=" * 50)
    print("--- GESTOR DE CADENA DE HOTELES ---")
    print("=" * 50)
    print("1. Añadir Hotel")
    print("2. Listar Hoteles")
    print("3. Eliminar Hotel")
    print("4. Gestionar Hotel")
    print("5. Gestionar Clientes")
    print("6. Salir")
    print("=" * 50)


def gestionar_hotel(hotel):
    """Menú para gestionar un hotel específico"""
    while True:
        print(f"\n--- Gestión del Hotel {hotel.nombre} ---")
        print("1. Registrar Nuevo Huésped")
        print("2. Liberar Habitación")
        print("3. Ver Huéspedes Actuales")
        print("4. Aplicar Servicio Extra a Huésped")
        print("5. Hacer Checkout de Huésped")
        print("6. Ver Ocupación del Hotel")
        print("7. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # TODO - Registrar Nuevo Huésped
            # Pedir ID cliente
            # Buscar cliente
            # Pedir número de noches y precio
            # Agregar cliente al hotel
            # Registrar hospedaje en cliente
            pass

        elif opcion == "2":
            # TODO - Liberar Habitación
            # Pedir ID cliente a desalojar
            # Buscar cliente en hotel
            # Liberar habitación
            pass

        elif opcion == "3":
            # TODO - Ver Huéspedes Actuales
            # Obtener lista de huéspedes del hotel
            # Mostrar cada uno
            pass

        elif opcion == "4":
            # TODO - Aplicar Servicio Extra
            # Pedir ID cliente
            # Pedir precio del servicio
            # Aplicar el servicio
            pass

        elif opcion == "5":
            # TODO - Hacer Checkout
            # Pedir ID cliente
            # Mostrar total a pagar
            # Liberar habitación
            # Resetear datos del cliente
            pass

        elif opcion == "6":
            # TODO - Ver Ocupación
            # Mostrar cuántas habitaciones están ocupadas



            pass

        elif opcion == "7":
            break


def gestionar_clientes(clientes_centro):
    """Menú para gestionar clientes del grupo de hoteles"""
    while True:
        print("\n--- Gestión de Clientes del Grupo de Hoteles ---")
        print("1. Añadir Nuevo Cliente")
        print("2. Buscar Cliente por ID")
        print("3. Identificar Clientes VIP (Más de 5 noches)")
        print("4. Identificar Clientes Premium (Más de 500€ gastados)")
        print("5. Ver Todos los Clientes")
        print("6. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # TODO - Añadir Nuevo Cliente

            try:
                nombre=input("Introduce un nombre para el cliente nuevo: ")
                pasaporte=input("Introduce un pasaporte: ")
                email=input("Introduce un email: ")
                edad=int(input("Introduce una edad: "))

                nuevo_cliente= Cliente(nombre, pasaporte, email, edad)
                clientes_centro.append(nuevo_cliente)
                print(f"{nombre} añadido como Cliente (ID: {nuevo_cliente.id_cliente})")
            except ValueError:
                print("Datos incorrectos")




        elif opcion == "2":
            # TODO - Buscar Cliente por ID
            # Pedir ID
            # Buscar en lista
            # Mostrar información

            id_cliente=int(input("Introduce un id de cliente: "))
            cliente_encontrado=buscar_cliente_por_id(id_cliente, clientes_centro)





        elif opcion == "3":
            # TODO - Clientes VIP
            # Iterar clientes
            # Filtrar por total_noches > 5
            # Mostrar lista

            for cliente in clientes_centro:
                if cliente.total_noches > 5:
                    return cliente

            return None


        elif opcion == "4":
            # TODO - Clientes Premium
            # Iterar clientes
            # Filtrar por total_gastado > 500
            # Mostrar lista

            for cliente in clientes_centro:
                if cliente.total_gastado > 500:
                    return cliente

            return None


        elif opcion == "5":
            # TODO - Ver Todos
            # Mostrar cada cliente

            for cliente in clientes_centro:
                print(f"[{cliente.id_cliente}], nombre: {cliente.nombre}, "
                      f"noches: {cliente.total_noches}, gastado: {cliente.total_gastado}")

            if not clientes_centro:
                print("No hay clientes en la lista")
                continue


        elif opcion == "6":
            break


def buscar_hotel_por_id(id_hotel, hoteles):
    """Busca un hotel por su ID"""

    for hotel in hoteles:
        if hotel.id_hotel == id_hotel:
            return hotel
    print(f"Hotel no encontrado con ID: {id_hotel}")

    return None


def buscar_cliente_por_id(id_cliente, clientes):
    """Busca un cliente por su ID"""
    for cliente in clientes_centro:
        if cliente.id_cliente == id_cliente:
            return cliente
    print(f"Cliente no encontrado con ID: {id_cliente}")

    return None


def hoteles_por_ciudad(ciudad, hoteles):
    """Devuelve hoteles de una ciudad específica"""
    pass


# PROGRAMA PRINCIPAL
if __name__ == "__main__":

    hoteles = []
    clientes_centro = []

    # Crear hoteles de ejemplo
    hotel1 = Hotel("Sol Mediterráneo", "Barcelona", 50, 4)
    hotel2 = Hotel("Montaña Blanca", "Andorra", 30, 3)
    hotel3 = Hotel("Costa Brava Resort", "Tossa de Mar", 40, 4)
    hotel4 = Hotel("Ciudad Antigua", "Toledo", 25, 2)

    hoteles.extend([hotel1, hotel2, hotel3, hotel4])

    # Crear clientes de ejemplo
    cliente1 = Cliente("Juan García", "A12345678", "juan@email.com", 35)
    cliente2 = Cliente("María López", "B87654321", "maria@email.com", 28)
    cliente3 = Cliente("Carlos Ruiz", "C11111111", "carlos@email.com", 45)
    cliente4 = Cliente("Ana Martínez", "D22222222", "ana@email.com", 32)
    cliente5 = Cliente("Pedro Sánchez", "E33333333", "pedro@email.com", 50)
    cliente6 = Cliente("Laura Fernández", "F44444444", "laura@email.com", 26)
    cliente7 = Cliente("Miguel Torres", "G55555555", "miguel@email.com", 38)
    cliente8 = Cliente("Sofia Gómez", "H66666666", "sofia@email.com", 29)
    cliente9 = Cliente("Diego Moreno", "I77777777", "diego@email.com", 42)
    cliente10 = Cliente("Isabel Castro", "J88888888", "isabel@email.com", 31)

    clientes_centro.extend([cliente1, cliente2, cliente3, cliente4, cliente5,
                           cliente6, cliente7, cliente8, cliente9, cliente10])

    # Asignar clientes iniciales a hoteles
    hotel1.agregar_cliente_habitacion(cliente1)
    hotel1.agregar_cliente_habitacion(cliente2)
    hotel1.agregar_cliente_habitacion(cliente3)

    hotel2.agregar_cliente_habitacion(cliente4)
    hotel2.agregar_cliente_habitacion(cliente5)

    hotel3.agregar_cliente_habitacion(cliente6)
    hotel3.agregar_cliente_habitacion(cliente7)
    hotel3.agregar_cliente_habitacion(cliente8)

    hotel4.agregar_cliente_habitacion(cliente9)
    hotel4.agregar_cliente_habitacion(cliente10)

    # Menú principal
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # TODO - Añadir Hotel
            try:
                # Pedir nombre, ciudad, número habitaciones, categoría
                nombre=input("Introduce un nombre: ")
                ciudad=input("Introduce un ciudad: ")
                numero_habitaciones=int(input("Introduce numero de habitaciones: "))
                categoria=int(input("Introduce una categoria(1-5): "))

                #Añadir hotel
                nuevo_hotel= Hotel(nombre, ciudad, numero_habitaciones, categoria)
                hoteles.append(nuevo_hotel)

                print(f"{nombre} añadido como Hotel (ID: {nuevo_hotel.id_hotel})")
            except ValueError:
                print("Valores incorrectos")


        elif opcion == "2":
            # TODO - Listar Hoteles
            for hotel in hoteles:
                print(hotel)

            if not hoteles:
                print("No hay hoteles en la lista")


        elif opcion == "3":
            # TODO - Eliminar Hotel
            # Pedir ID
            # Buscar
            # Eliminar de lista

            id_hotel=int(input("Introduce un id: "))
            hotel_encontrado=buscar_hotel_por_id(id_hotel, hoteles)

            if not hotel_encontrado:
                continue

            hoteles.remove(hotel_encontrado)
            print(f"Hotel {hotel_encontrado.id_hotel} borrado")


        elif opcion == "4":
            # TODO - Gestionar Hotel
            # Pedir ID hotel
            # Buscar
            id_hotel = int(input("Introduce un id: "))
            hotel_encontrado = buscar_hotel_por_id(id_hotel, hoteles)

            if not hotel_encontrado:
                continue

            # Llamar a gestionar_hotel()
            gestionar_hotel(hotel_encontrado)



        elif opcion == "5":
            # TODO - Gestionar Clientes
            # Llamar a gestionar_clientes()
            gestionar_clientes(clientes_centro)



        elif opcion == "6":
            print("\n¡Hasta luego!")
            break

        else:
            print("❌ Opción no válida")