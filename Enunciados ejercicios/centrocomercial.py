class Tienda:

    # TODO Constructor y Atributo Estático
    def __init__(self, nombre, cif, tipo_tienda, propietario):
        pass

    def __str__(self):
        return f"Tienda {self.id}: {self.nombre} - {self.tipo_tienda}, Propietario: {self.propietario}, Socios: {self.num_socios_actuales}"

    #TODO Método anadir_socio

    #TODO Método eliminar_socio

    #TODO Método obtener_socios



class Cliente:

    #TODO Completa constructor, Atributo Estático, Actualización y Uso del Atributo Estático
    def __init__(self, nombre, nif, codigo_postal, edad):

        self.id = id
        self.nombre = nombre
        self.nif = nif
        self.codigo_postal = codigo_postal
        self.edad = edad
        self.cantidad_compras = 0
        self.dinero_gastado = 0.0
        self.tiendas_asociadas=[]


    def __str__(self):
        return (f"Cliente {self.id}: {self.nombre}, {self.edad} años, {self.cantidad_compras} compras, "
                f"Total gastado: {self.dinero_gastado}€")

    # TODO Método comprar

    # TODO Método devolver





# NO ELIMINAR - función para pintar el menú principal
def mostrar_menu():
    print("\n--- Menú de Gestión del Centro Comercial ---")
    print("1. Añadir Tienda")
    print("2. Listar Tiendas")
    print("3. Eliminar Tienda")
    print("4. Gestionar Tienda")
    print("5. Gestionar Socios")
    print("6. Salir")


# NO ELIMINAR - función para gestionar una tienda concreta
def gestionar_tienda(tienda):
    while True:
        print(f"\n--- Gestión de la Tienda {tienda.nombre} ---")
        print("1. Añadir Socio")
        print("2. Eliminar Socio")
        print("3. Ver Socios")
        print("4. Registrar Compra Realizada por un Socio")
        print("5. Registrar Devolución Realizada por un Socio")
        print("6. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            #TO-DO - Implementa la opción 1 - Añadir Socio
            pass

        elif opcion == "2":

            #TODO - Implementa la opción 2 - Eliminar Socio
            pass

        elif opcion == "3":
            #TODO - Implementa la opción 3 - Ver Socios
            pass

        elif opcion == "4":
            #TODO - Implementa la opción 4 - Registrar Compra Realizada por un Socio
            pass

        elif opcion == "5":
            #TODO - Implementa la opción 5 - Registrar Devolución Realizada por un Socio
            pass


        elif opcion == "6":
            break




# NO ELIMINAR - función para gestionar clientes del centro comercial
def gestionar_clientes():
    while True:
        print("\n--- Gestión de Clientes ---")
        print("1. Añadir Cliente al Centro Comercial")
        print("2. Asociar Cliente a Varias Tiendas")
        print("3. Identificar Clientes VIP")
        print("4. Identificar Clientes Premium")
        print("5. Identificar Clientes sin Asociar")
        print("6. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            #TODO - Implementa la opción 1 - Añadir Cliente al Centro Comercial
            pass

        elif opcion == "2":
            #TODO - Implementa la opción 2 - Asociar Cliente a Varias Tiendas
            pass

        elif opcion == "3":
            #TODO - Implementa la opción 3 - Identificar Clientes VIP
            pass


        elif opcion == "4":
            #TODO - Implementa la opción 4 - Identificar Clientes Premium
            pass

        elif opcion == "5":
            #TODO - Implementa la opción 5 - Identificar Clientes sin Asociar
            pass

        elif opcion == "6":
            break



#Comienzo del programa principal
if __name__ == "__main__":

    # NO ELIMINAR - Listas de tiendas registradas y de clientes del centro comercial
    tiendas = []
    clientes_centro_comercial = []

    # NO ELIMINAR - Crear tiendas de ejemplo
    tienda1 = Tienda("Gourmet Plaza", "B11111111", "Restaurante", "Juan López")
    tienda2 = Tienda("Fashion World", "B22222222", "Ropa", "Ana Martínez")
    tienda3 = Tienda("Tech Mobile", "B33333333", "Smartphone", "Carlos Sánchez")

    # NO ELIMINAR - Añadir tiendas a la lista de tiendas del centro comercial
    tiendas.append(tienda1)
    tiendas.append(tienda2)
    tiendas.append(tienda3)


    # NO ELIMINAR - Crear clientes de ejemplo
    cliente1 = Cliente("Pedro García", "11111111A", "21001", 35)
    cliente2 = Cliente("Laura Torres", "22222222B", "21002", 28)
    cliente3 = Cliente("Miguel Fernández", "33333333C", "21003", 40)
    cliente4 = Cliente("Sofía Ramírez", "44444444D", "21004", 32)
    cliente5 = Cliente("Carlos Gómez", "55555555E", "21005", 30)  # Cliente que es socio en las 3 tiendas
    cliente6 = Cliente("Pedro Orozco", "66666666F", "21007", 49)
    cliente7 = Cliente("Santiago Sancho", "77777777G", "21009", 37)
    cliente8 = Cliente("Daniel Perez", "88888888H", "21010", 46)
    cliente9 = Cliente("Lola García", "99999999I", "21035", 26)
    cliente10 = Cliente("Ainara Sanchez", "10101010J", "21005", 21)
    cliente11 = Cliente("Jesús Aguilar", "20202020K", "21045", 50)
    cliente12 = Cliente("Carlos Frasco", "30303030L", "21002", 50)

    # NO ELIMINAR - Añadir clientes a la lista de clientes del centro comercial
    clientes_centro_comercial.append(cliente1)
    clientes_centro_comercial.append(cliente2)
    clientes_centro_comercial.append(cliente3)
    clientes_centro_comercial.append(cliente4)
    clientes_centro_comercial.append(cliente5)
    clientes_centro_comercial.append(cliente6)
    clientes_centro_comercial.append(cliente7)
    clientes_centro_comercial.append(cliente8)
    clientes_centro_comercial.append(cliente9)
    clientes_centro_comercial.append(cliente10)
    clientes_centro_comercial.append(cliente11)
    clientes_centro_comercial.append(cliente12)


    # NO ELIMINAR - Asignar clientes a tiendas
    tienda1.anadir_socio(cliente1)
    tienda1.anadir_socio(cliente2)
    tienda1.anadir_socio(cliente3)
    tienda1.anadir_socio(cliente11)
    tienda1.anadir_socio(cliente10) # Cliente común
    tienda1.anadir_socio(cliente5)  # Cliente común

    tienda2.anadir_socio(cliente4)
    tienda2.anadir_socio(cliente6)
    tienda2.anadir_socio(cliente7)
    tienda2.anadir_socio(cliente12)
    tienda2.anadir_socio(cliente10) # Cliente común
    tienda2.anadir_socio(cliente5)  # Cliente común

    tienda3.anadir_socio(cliente8)
    tienda3.anadir_socio(cliente9)
    tienda3.anadir_socio(cliente10) # Cliente común
    tienda3.anadir_socio(cliente5)  # Cliente común


    # NO ELIMINAR -Iniciar menú de gestión del centro comercial
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            #TODO - Implementa la opción 1 - Añadir Tienda
            pass

        elif opcion == "2":
            #TODO - Implementa la opción 2 - Listar Tiendas
            pass

        elif opcion == "3":
            #TODO - Implementa la opción 3 - Eliminar Tienda
            pass

        elif opcion == "4":
            #TODO - Implementa la opción 4 - Gestionar Tienda
            # Obviamente,esta opción debe llamar al otro menú, al que gestiona una única tienda
            pass

        elif opcion == "5":
            #TODO - Implementa la opción 5 - Gestionar Socios
            # Obviamente,esta opción debe llamar a otro menú, al que gestiona los socios del cetro comercial
            pass

        elif opcion == "6":
            break