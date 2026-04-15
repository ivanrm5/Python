"""
PROYECTO: GESTOR DE CENTRO COMERCIAL
Versión corregida y completa
"""


class Tienda:
    """Clase que representa una tienda del centro comercial"""

    # Atributo estático para contar tiendas
    contador_tiendas = 0

    def __init__(self, nombre, cif, tipo_tienda, propietario):
        """Constructor de Tienda"""
        Tienda.contador_tiendas += 1
        self.id_tienda = Tienda.contador_tiendas
        self.nombre = nombre
        self.cif = cif
        self.tipo_tienda = tipo_tienda
        self.propietario = propietario
        self.lista_socios = []  # Lista de objetos Cliente
        self.num_socios_actuales = 0

    def __str__(self):
        """Representación en string de la Tienda"""
        return (f"Tienda {self.id_tienda}: {self.nombre} - {self.tipo_tienda}, "
                f"Propietario: {self.propietario}, Socios: {self.num_socios_actuales}")

    def anadir_socio(self, cliente):
        """Añade un cliente como socio de la tienda"""
        # Verificar que el cliente no sea ya socio
        if cliente in self.lista_socios:
            print(f"{cliente.nombre} ya es socio de {self.nombre}")
            return

        # Añadir a la lista
        self.lista_socios.append(cliente)
        self.num_socios_actuales += 1
        print(f"✓ {cliente.nombre} añadido como socio de {self.nombre}")

    def eliminar_socio(self, cliente):
        """Elimina un cliente de la lista de socios"""
        if cliente in self.lista_socios:
            self.lista_socios.remove(cliente)
            self.num_socios_actuales -= 1
            print(f"✓ {cliente.nombre} eliminado de {self.nombre}")
        else:
            print(f"{cliente.nombre} no es socio de {self.nombre}")

    def obtener_socios(self):
        """Devuelve la lista de socios"""
        return self.lista_socios

    def mostrar_socios(self):
        """Muestra todos los socios de la tienda"""
        if not self.lista_socios:
            print(f"  No hay socios en {self.nombre}")
            return

        print(f"\n  Socios de {self.nombre}:")
        for socio in self.lista_socios:
            print(f"    - {socio.nombre} (ID: {socio.id_cliente}, gastado: {socio.dinero_gastado}€)")


class Cliente:
    """Clase que representa un cliente del centro comercial"""

    # Atributo estático para contar clientes
    contador_clientes = 0

    def __init__(self, nombre, nif, codigo_postal, edad):
        """Constructor de Cliente"""
        Cliente.contador_clientes += 1
        self.id_cliente = Cliente.contador_clientes
        self.nombre = nombre
        self.nif = nif
        self.codigo_postal = codigo_postal
        self.edad = edad
        self.cantidad_compras = 0
        self.dinero_gastado = 0.0
        self.tiendas_asociadas = []  # Lista de tiendas donde es socio

    def __str__(self):
        """Representación en string del Cliente"""
        return (f"Cliente {self.id_cliente}: {self.nombre}, {self.edad} años, {self.cantidad_compras} compras, "
                f"Total gastado: {self.dinero_gastado}€")

    def comprar(self, cantidad):
        """Registra una compra del cliente"""
        if cantidad <= 0:
            print("La cantidad debe ser positiva")
            return

        self.dinero_gastado += cantidad
        self.cantidad_compras += 1
        print(f"✓ {self.nombre} ha gastado {cantidad}€. Total: {self.dinero_gastado}€")

    def devolver(self, cantidad):
        """Registra una devolución del cliente"""
        if cantidad <= 0:
            print("La cantidad debe ser positiva")
            return

        if self.dinero_gastado >= cantidad:
            self.dinero_gastado -= cantidad
            print(f"✓ {self.nombre} devolvió {cantidad}€. Total: {self.dinero_gastado}€")
        else:
            print(f"No se puede devolver {cantidad}€ (total gastado: {self.dinero_gastado}€)")


# ============================================================================
# FUNCIONES DE MENÚ
# ============================================================================

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "=" * 50)
    print("--- Menú de Gestión del Centro Comercial ---")
    print("=" * 50)
    print("1. Añadir Tienda")
    print("2. Listar Tiendas")
    print("3. Eliminar Tienda")
    print("4. Gestionar Tienda")
    print("5. Gestionar Clientes")
    print("6. Salir")
    print("=" * 50)


def gestionar_tienda(tienda, clientes_centro_comercial):
    """Menú para gestionar una tienda específica"""
    while True:
        print(f"\n--- Gestión de la Tienda {tienda.nombre} ---")
        print("1. Añadir Socio (Cliente)")
        print("2. Eliminar Socio")
        print("3. Ver Socios")
        print("4. Registrar Compra Realizada por un Socio")
        print("5. Registrar Devolución Realizada por un Socio")
        print("6. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Añadir socio: buscar cliente y añadirlo a la tienda
            print("\nClientes disponibles:")
            for cliente in clientes_centro_comercial:
                print(f"  [{cliente.id_cliente}] {cliente.nombre}")

            try:
                id_cliente = int(input("ID del cliente a añadir: "))
                cliente_encontrado = None

                for cliente in clientes_centro_comercial:
                    if cliente.id_cliente == id_cliente:
                        cliente_encontrado = cliente
                        break

                if cliente_encontrado:
                    tienda.anadir_socio(cliente_encontrado)
                else:
                    print("Cliente no encontrado")
            except ValueError:
                print("Debes introducir un número válido")

        elif opcion == "2":
            # Eliminar socio
            print("\nSocios actuales:")
            tienda.mostrar_socios()

            try:
                id_cliente = int(input("ID del cliente a eliminar: "))
                cliente_encontrado = None

                for cliente in tienda.obtener_socios():
                    if cliente.id_cliente == id_cliente:
                        cliente_encontrado = cliente
                        break

                if cliente_encontrado:
                    tienda.eliminar_socio(cliente_encontrado)
                else:
                    print("Cliente no encontrado en socios")
            except ValueError:
                print("Debes introducir un número válido")

        elif opcion == "3":
            # Ver socios
            tienda.mostrar_socios()

        elif opcion == "4":
            # Registrar compra
            print("\nSocios actuales:")
            tienda.mostrar_socios()

            try:
                id_cliente = int(input("ID del cliente que compra: "))
                cantidad = float(input("Cantidad a gastar: "))

                cliente_encontrado = None
                for cliente in tienda.obtener_socios():
                    if cliente.id_cliente == id_cliente:
                        cliente_encontrado = cliente
                        break

                if cliente_encontrado:
                    cliente_encontrado.comprar(cantidad)
                else:
                    print("Cliente no encontrado en socios")
            except ValueError:
                print("Datos inválidos")

        elif opcion == "5":
            # Registrar devolución
            print("\nSocios actuales:")
            tienda.mostrar_socios()

            try:
                id_cliente = int(input("ID del cliente que devuelve: "))
                cantidad = float(input("Cantidad a devolver: "))

                cliente_encontrado = None
                for cliente in tienda.obtener_socios():
                    if cliente.id_cliente == id_cliente:
                        cliente_encontrado = cliente
                        break

                if cliente_encontrado:
                    cliente_encontrado.devolver(cantidad)
                else:
                    print("Cliente no encontrado en socios")
            except ValueError:
                print("Datos inválidos")

        elif opcion == "6":
            break


def gestionar_clientes(clientes_centro_comercial, tiendas):
    """Menú para gestionar clientes del centro comercial"""
    while True:
        print("\n--- Gestión de Clientes ---")
        print("1. Añadir Cliente al Centro Comercial")
        print("2. Listar Clientes")
        print("3. Ver Detalles de un Cliente")
        print("4. Identificar Clientes VIP (>1000€ gastado)")
        print("5. Identificar Clientes Premium (>5 compras)")
        print("6. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Añadir cliente
            try:
                nombre = input("Nombre del cliente: ")
                nif = input("NIF: ")
                codigo_postal = input("Código postal: ")
                edad = int(input("Edad: "))

                nuevo_cliente = Cliente(nombre, nif, codigo_postal, edad)
                clientes_centro_comercial.append(nuevo_cliente)
                print(f"✓ {nombre} añadido como cliente (ID: {nuevo_cliente.id_cliente})")
            except ValueError:
                print("Datos inválidos")

        elif opcion == "2":
            # Listar clientes
            print("\nClientes del centro comercial:")
            if not clientes_centro_comercial:
                print("  No hay clientes registrados")
            else:
                for cliente in clientes_centro_comercial:
                    print(f"  {cliente}")

        elif opcion == "3":
            # Ver detalles de un cliente
            try:
                id_cliente = int(input("ID del cliente: "))
                cliente_encontrado = None

                for cliente in clientes_centro_comercial:
                    if cliente.id_cliente == id_cliente:
                        cliente_encontrado = cliente
                        break

                if cliente_encontrado:
                    print(f"\n{cliente_encontrado}")
                    print(f"NIF: {cliente_encontrado.nif}")
                    print(f"Código postal: {cliente_encontrado.codigo_postal}")
                    print("Socios en tiendas:")

                    cliente_en_alguna = False
                    for tienda in tiendas:
                        if cliente_encontrado in tienda.obtener_socios():
                            print(f"  - {tienda.nombre}")
                            cliente_en_alguna = True

                    if not cliente_en_alguna:
                        print("  No es socio en ninguna tienda")
                else:
                    print("Cliente no encontrado")
            except ValueError:
                print("Debes introducir un número válido")

        elif opcion == "4":
            # Clientes VIP
            print("\nClientes VIP (>1000€ gastado):")
            vip_encontrados = False
            for cliente in clientes_centro_comercial:
                if cliente.dinero_gastado > 1000:
                    print(f"  {cliente.nombre}: {cliente.dinero_gastado}€")
                    vip_encontrados = True
            if not vip_encontrados:
                print("  No hay clientes VIP")

        elif opcion == "5":
            # Clientes Premium
            print("\nClientes Premium (>5 compras):")
            premium_encontrados = False
            for cliente in clientes_centro_comercial:
                if cliente.cantidad_compras > 5:
                    print(f"  {cliente.nombre}: {cliente.cantidad_compras} compras")
                    premium_encontrados = True
            if not premium_encontrados:
                print("  No hay clientes premium")

        elif opcion == "6":
            break


# ============================================================================
# PROGRAMA PRINCIPAL
# ============================================================================

if __name__ == "__main__":
    # Listas globales
    tiendas = []
    clientes_centro_comercial = []

    # Crear tiendas de ejemplo
    tienda1 = Tienda("Gourmet Plaza", "B11111111", "Restaurante", "Juan López")
    tienda2 = Tienda("Fashion World", "B22222222", "Ropa", "Ana Martínez")
    tienda3 = Tienda("Tech Mobile", "B33333333", "Smartphone", "Carlos Sánchez")

    tiendas.append(tienda1)
    tiendas.append(tienda2)
    tiendas.append(tienda3)

    # Crear clientes de ejemplo
    cliente1 = Cliente("Pedro García", "11111111A", "21001", 35)
    cliente2 = Cliente("Laura Torres", "22222222B", "21002", 28)
    cliente3 = Cliente("Miguel Fernández", "33333333C", "21003", 40)
    cliente4 = Cliente("Sofía Ramírez", "44444444D", "21004", 32)
    cliente5 = Cliente("Carlos Gómez", "55555555E", "21005", 30)
    cliente6 = Cliente("Pedro Orozco", "66666666F", "21007", 49)
    cliente7 = Cliente("Santiago Sancho", "77777777G", "21009", 37)
    cliente8 = Cliente("Daniel Perez", "88888888H", "21010", 46)
    cliente9 = Cliente("Lola García", "99999999I", "21035", 26)
    cliente10 = Cliente("Ainara Sanchez", "10101010J", "21005", 21)
    cliente11 = Cliente("Jesús Aguilar", "20202020K", "21045", 50)
    cliente12 = Cliente("Carlos Frasco", "30303030L", "21002", 50)

    clientes_centro_comercial.extend([cliente1, cliente2, cliente3, cliente4, cliente5, cliente6,
                                      cliente7, cliente8, cliente9, cliente10, cliente11, cliente12])

    # Asignar clientes a tiendas como socios
    tienda1.anadir_socio(cliente1)
    tienda1.anadir_socio(cliente2)
    tienda1.anadir_socio(cliente3)
    tienda1.anadir_socio(cliente11)
    tienda1.anadir_socio(cliente10)
    tienda1.anadir_socio(cliente5)

    tienda2.anadir_socio(cliente4)
    tienda2.anadir_socio(cliente6)
    tienda2.anadir_socio(cliente7)
    tienda2.anadir_socio(cliente12)
    tienda2.anadir_socio(cliente10)
    tienda2.anadir_socio(cliente5)

    tienda3.anadir_socio(cliente8)
    tienda3.anadir_socio(cliente9)
    tienda3.anadir_socio(cliente10)
    tienda3.anadir_socio(cliente5)

    # Registrar algunas compras para los ejemplos
    cliente1.comprar(500)
    cliente2.comprar(400)
    cliente5.comprar(1500)
    cliente11.comprar(600)

    # Menú principal
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Añadir tienda
            try:
                nombre = input("Nombre de la tienda: ")
                cif = input("CIF: ")
                tipo = input("Tipo de tienda: ")
                propietario = input("Propietario: ")

                nueva_tienda = Tienda(nombre, cif, tipo, propietario)
                tiendas.append(nueva_tienda)
                print(f"✓ Tienda '{nombre}' creada (ID: {nueva_tienda.id_tienda})")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "2":
            # Listar tiendas
            print("\nTiendas del centro comercial:")
            if not tiendas:
                print("  No hay tiendas registradas")
            else:
                for tienda in tiendas:
                    print(f"  {tienda}")

        elif opcion == "3":
            # Eliminar tienda
            print("\nTiendas disponibles:")
            for tienda in tiendas:
                print(f"  [{tienda.id_tienda}] {tienda.nombre}")

            try:
                id_tienda = int(input("ID de la tienda a eliminar: "))
                tienda_encontrada = None

                for tienda in tiendas:
                    if tienda.id_tienda == id_tienda:
                        tienda_encontrada = tienda
                        break

                if tienda_encontrada:
                    tiendas.remove(tienda_encontrada)
                    print(f"Tienda '{tienda_encontrada.nombre}' eliminada")
                else:
                    print("Tienda no encontrada")
            except ValueError:
                print("Debes introducir un número válido")

        elif opcion == "4":
            # Gestionar tienda
            print("\nTiendas disponibles:")
            for tienda in tiendas:
                print(f"  [{tienda.id_tienda}] {tienda.nombre}")

            try:
                id_tienda = int(input("ID de la tienda a gestionar: "))
                tienda_encontrada = None

                for tienda in tiendas:
                    if tienda.id_tienda == id_tienda:
                        tienda_encontrada = tienda
                        break

                if tienda_encontrada:
                    gestionar_tienda(tienda_encontrada, clientes_centro_comercial)
                else:
                    print("Tienda no encontrada")
            except ValueError:
                print("Debes introducir un número válido")

        elif opcion == "5":
            # Gestionar clientes
            gestionar_clientes(clientes_centro_comercial, tiendas)

        elif opcion == "6":
            print("\n¡Hasta luego!")
            break

        else:
            print("Opción no válida")