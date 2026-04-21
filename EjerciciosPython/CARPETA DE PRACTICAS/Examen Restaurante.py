"""
PROYECTO GESTOR DE RESTAURANTE
Gestiona mesas, clientes y pedidos
Estructura compleja pero funciones simples
"""


class Plato:
    """Representa un plato del menú"""

    contador_platos = 0

    def __init__(self, nombre, precio, categoria):
        Plato.contador_platos += 1
        self.id_plato = Plato.contador_platos
        self.nombre = nombre
        self.precio = precio  # Precio en euros
        self.categoria = categoria  # "Entrante", "Principal", "Postre", "Bebida"
        self.stock = 20  # Cantidad disponible

    def __str__(self):
        return (f"ID: {self.id_plato}: {self.nombre} ({self.categoria}) - "
                f"{self.precio}€, Stock: {self.stock}")

    def reducir_stock(self):
        """Reduce el stock en 1"""
        self.stock-=1


    def aumentar_stock(self):
        """Aumenta el stock en 1"""
        self.stock+=1

    def hay_disponible(self):
        """Comprueba si hay stock"""
        if self.stock > 0:
            return True
        return False



class Mesa:
    """Representa una mesa del restaurante"""

    contador_mesas = 0

    def __init__(self, numero, capacidad):
        Mesa.contador_mesas += 1
        self.id_mesa = Mesa.contador_mesas
        self.numero = numero
        self.capacidad = capacidad  # Número de comensales
        self.disponible = True
        self.cliente_actual = None  # ID del cliente usando la mesa
        self.pedidos = []  # Lista de platos pedidos
        self.cuenta_total = 0.0  # Total a pagar

    def __str__(self):
        estado = "Disponible" if self.disponible else "Ocupada"
        return (f"ID: {self.id_mesa}: Mesa {self.numero} (Cap: {self.capacidad}), "
                f"Estado: {estado}, Cuenta: {self.cuenta_total}€")

    def ocupar_mesa(self, id_cliente):
        """Ocupa la mesa con un cliente"""
        self.disponible= False
        self.cliente_actual= id_cliente
        self.pedidos = []

    def liberar_mesa(self):
        """Libera la mesa"""
        self.disponible=True
        self.cliente_actual=None
        self.pedidos=[]
        self.cuenta_total=0.0


    def anadir_plato(self, plato):
        """Añade un plato al pedido"""
        self.pedidos.append(plato)
        self.cuenta_total+=plato.precio

    def obtener_cuenta(self):
        """Obtiene el total a pagar"""
        return self.cuenta_total

    def obtener_pedidos(self):
        """Obtiene la lista de platos pedidos"""
        if not self.pedidos:
            print("No hay pedidos en esta mesa")
        else:
            for pedido in self.pedidos:
                print(pedido)


class Cliente:
    """Representa un cliente del restaurante"""

    contador_clientes = 0

    def __init__(self, nombre, telefono, comensales):
        Cliente.contador_clientes += 1
        self.id_cliente = Cliente.contador_clientes
        self.nombre = nombre
        self.telefono = telefono
        self.comensales = comensales  # Número de personas
        self.total_gastado = 0.0
        self.visitas = 0  # Número de veces que vino
        self.mesa_asignada = None  # ID de la mesa

    def __str__(self):
        return (f"ID: {self.id_cliente}: {self.nombre} ({self.comensales} comensales), "
                f"Total gastado: {self.total_gastado}€, Visitas: {self.visitas}")

    def pagar_cuenta(self, monto):
        """Paga la cuenta"""
        self.total_gastado+=monto
        self.visitas+=1


    def registrar_visita(self):
        """Incrementa el contador de visitas"""
        self.visitas+=1


    def obtener_info(self):
        """Devuelve información del cliente"""
        print(f"Informacion del cliente {cliente.nombre}")
        print (cliente)



# FUNCIONES GLOBALES

def mostrar_menu_principal():
    """Menú principal"""
    print("\n" + "=" * 60)
    print("--- GESTOR DE RESTAURANTE ---")
    print("=" * 60)
    print("1. Ver Menú (Platos disponibles)")
    print("2. Ver Mesas")
    print("3. Ver Clientes")
    print("4. Hacer Reserva (Ocupar mesa)")
    print("5. Hacer Pedido")
    print("6. Ver Cuenta de Mesa")
    print("7. Cobrar y Liberar Mesa")
    print("8. Buscar Cliente")
    print("9. Salir")
    print("=" * 60)


def gestionar_mesa(mesa, platos):
    """Menú para gestionar una mesa específica"""
    while True:
        print(f"\n--- Gestión de Mesa {mesa.numero} ---")
        print("1. Ver Pedidos Actuales")
        print("2. Añadir Plato")
        print("3. Ver Cuenta")
        print("4. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # TODO - Ver pedidos de la mesa
            pass

        elif opcion == "2":
            # TODO - Añadir plato a la mesa
            pass

        elif opcion == "3":
            # TODO - Ver cuenta actual
            pass

        elif opcion == "4":
            break

        else:
            print("❌ Opción no válida")


def buscar_plato_por_id(id_plato, platos):
    """Busca un plato por ID"""
    for plato in platos:
        if plato.id_plato == id_plato:
            return plato
    return None


def buscar_mesa_por_numero(numero, mesas):
    """Busca una mesa por número"""

    for mesa in mesas:
        if mesa.numero == numero:
            return mesa
    return None



def buscar_cliente_por_id(id_cliente, clientes):
    """Busca un cliente por ID"""
    for cliente in clientes:
        if cliente.id_cliente == id_cliente:
            return cliente
    return None



def platos_por_categoria(categoria, platos):
    """Busca platos por categoría"""
    platos_categoria=[]

    for plato in platos:
        if plato.categoria.lower() == categoria.lower():
            platos_categoria.append(plato)

    if not platos_categoria:
        print("No hay platos de esta categoria")
    else:
        for plato in platos_categoria:
            print(f"{plato.nombre} - categoria {plato.categoria}")



def mesas_disponibles(mesas):
    """Devuelve mesas disponibles"""
    mesa_disponible=[]

    for mesa in mesas:
        if mesa.disponible:
            mesa_disponible.append(mesa)
    return mesa_disponible


def clientes_vip(clientes):
    """Devuelve clientes con más de 5 visitas"""
    clientes_vip=[]

    for cliente in clientes:
        if cliente.visitas > 5:
            clientes_vip.append(cliente)

    if not clientes_vip:
        print("No hay clientes VIP ")

    print(clientes_vip)


# PROGRAMA PRINCIPAL
if __name__ == "__main__":

    platos = []
    mesas = []
    clientes = []

    # Crear platos
    plato1 = Plato("Tabla de quesos", 12.50, "Entrante")
    plato2 = Plato("Sopa de cebolla", 8.00, "Entrante")
    plato3 = Plato("Carne a la parrilla", 22.00, "Principal")
    plato4 = Plato("Salmón a la mantequilla", 24.00, "Principal")
    plato5 = Plato("Pasta al trufa", 18.50, "Principal")
    plato6 = Plato("Chocolate derretido", 7.50, "Postre")
    plato7 = Plato("Flan casero", 6.00, "Postre")
    plato8 = Plato("Agua mineral", 2.50, "Bebida")
    plato9 = Plato("Vino tinto", 5.50, "Bebida")
    plato10 = Plato("Cerveza", 3.50, "Bebida")

    platos.extend([plato1, plato2, plato3, plato4, plato5, plato6, plato7, plato8, plato9, plato10])

    # Crear mesas
    mesa1 = Mesa(1, 2)
    mesa2 = Mesa(2, 4)
    mesa3 = Mesa(3, 4)
    mesa4 = Mesa(4, 6)
    mesa5 = Mesa(5, 2)
    mesa6 = Mesa(6, 8)

    mesas.extend([mesa1, mesa2, mesa3, mesa4, mesa5, mesa6])

    # Crear clientes
    cliente1 = Cliente("Juan García", "612345678", 2)
    cliente2 = Cliente("María López", "687654321", 4)
    cliente3 = Cliente("Carlos Ruiz", "698765432", 2)
    cliente4 = Cliente("Ana Martínez", "656789012", 3)
    cliente5 = Cliente("Pedro Sánchez", "645678901", 6)
    cliente6 = Cliente("Laura Fernández", "634567890", 2)

    clientes.extend([cliente1, cliente2, cliente3, cliente4, cliente5, cliente6])

    # Menú principal
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # TODO - Ver menú (platos por categoría)
            # Mostrar todos los platos o por categoría
            try:
                opcion=int(input("Buscar todos los platos --> 0 "
                                 "Buscar platos por categoria --> 1"))

                if opcion == 0:
                    for plato in platos:
                        print (plato)

                if opcion == 1:
                    categoria = input("Buscar categoria --> ").lower()
                    platos_por_categoria(categoria, platos)

            except ValueError:
                print("Opcion no valida")


        elif opcion == "2":
            # TODO - Ver mesas
            # Mostrar todas las mesas con su estado
            if not mesas:
                print("No hay mesas actualmente")
            else:
                for mesa in mesas:
                    print (mesa)

        elif opcion == "3":
            # TODO - Ver clientes
            # Mostrar todos los clientes
            if not clientes:
                print("No hay clientes")
            else:
                for cliente in clientes:
                    print (cliente)


        elif opcion == "4":
            # TODO - Hacer reserva
            # Pedir: nombre cliente, comensales
            # Buscar mesa disponible con capacidad
            # Ocupar mesa

            nombre=input("Introduce nombre del cliente: ")
            telefono=input("Intoduce un numero de telefono")
            comensales=int(input("Cuantos comensales: "))

            md=mesas_disponibles(mesas)

            for mesa in md:
                if mesa.capacidad >= comensales:
                    print(mesa)

            clientes.append(nombre, telefono, comensales)
            








        elif opcion == "5":
            # TODO - Hacer pedido
            # Pedir: número de mesa
            # Buscar mesa
            # Mostrar menú
            # Pedir: ID plato
            # Añadir a pedidos
            pass

        elif opcion == "6":
            # TODO - Ver cuenta
            # Pedir: número de mesa
            # Buscar mesa
            # Mostrar cuenta
            pass

        elif opcion == "7":
            # TODO - Cobrar y liberar
            # Pedir: número de mesa
            # Buscar mesa
            # Pedir: cliente que paga
            # Actualizar cliente: total_gastado, visitas
            # Liberar mesa
            pass

        elif opcion == "8":
            # TODO - Buscar cliente
            # Pedir: ID cliente
            # Buscar
            # Mostrar información
            pass

        elif opcion == "9":
            print("\n¡Hasta luego!")
            break

        else:
            print("❌ Opción no válida")