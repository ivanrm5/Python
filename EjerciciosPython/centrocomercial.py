class Tienda:

    # TODO Constructor y Atributo Estático
    def __init__(self, id_tienda, nombre, cif, tipo_tienda, propietario, num_socios_actuales):
        self.id_tienda = id_tienda
        self.nombre = nombre
        self.cif = cif
        self.tipo_tienda = tipo_tienda
        self.propietario = propietario
        self.num_socios_actuales=num_socios_actuales
        self.lista_socios = []


    def __str__(self):
        return f"Tienda {self.id_tienda}: {self.nombre} - {self.tipo_tienda}, Propietario: {self.propietario}, Socios: {self.num_socios_actuales}"

    contador_socios=0

    #Metodo añadir_socio
    def anadir_socio(self, cliente:Cliente):
        for cliente in self.lista_socios:
            if cliente.id_cliente == cliente.id_cliente:
                print("El socio ya existe en la lista de clientes")
                return
        Tienda.contador_socios += 1
        self.lista_socios.append(cliente)

    #Metodo eliminar_socio

    def elimina_socio(self, id_cliente):
        for c in self.lista_socios:
            if c.id_cliente == id_cliente:
                Tienda.contador_socios -= 1
                self.lista_socios.remove(c)

    # Metodo obtener_socios
    def obtener_socios(self):
        for c in self.lista_socios:
            print("Nombre: ",c.nombre)


    def crear_tienda(self, tienda:Tienda):
        for tienda in self.id_tienda:
            if tienda.id_tienda == tienda.id_tienda:
                print("El tienda ya existe en la lista de tiendas")
                return
        self.tienda.append(tienda)


    def elimina_tienda(self, id_tienda):
        for tienda in self.id_tienda:
            if tienda.id_tienda == id_tienda:
                self.tienda.remove(tiendas)
        print("La tienda no existe")

    def listar_tiendas(self):
        for t in self.nombre:
            print("nombre: ",t)



class Cliente:

    #TODO Completa constructor, Atributo Estático, Actualización y Uso del Atributo Estático

    #Contador de clientes


    def __init__(self,id_cliente, nombre, nif, codigo_postal, edad, cantidad_compras, dinero_gastado):

        self.id_cliente = id_cliente
        self.nombre = nombre
        self.nif = nif
        self.codigo_postal = codigo_postal
        self.edad = edad
        self.cantidad_compras = cantidad_compras
        self.dinero_gastado = dinero_gastado

    def __str__(self):
        return f"Cliente {self.id_cliente}: {self.nombre}, {self.edad} años, {self.cantidad_compras} compras, Total gastado: {self.dinero_gastado}€"

    contador_socios=0

    # TODO Método comprar
    def comprar(self, id_cliente, dinero_gastado):
        for c in self.id_cliente:
            if c.id_cliente == id_cliente:
                self.dinero_gastado += c.dinero_gastado
                self.cantidad_compras +=1
                print("Cantidad de compras actualizada")
                return


    # TODO Método devolver
    def devolver(self, id_cliente, dinero_gastado):
        for c in self.id_cliente:
            if c.id_cliente == id_cliente:
                self.dinero_gastado -= c.dinero_gastado
                self.cantidad_compras -= 1
                print("Cantidad de compras actualizada")
                return




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
            nombre = input("Nombre: ")

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
    tienda1 = Tienda(1,"Gourmet Plaza", "B11111111", "Restaurante", "Juan López", 0 )
    tienda2 = Tienda(2,"Fashion World", "B22222222", "Ropa", "Ana Martínez",0)
    tienda3 = Tienda(3, "Tech Mobile", "B33333333", "Smartphone", "Carlos Sánchez",0)

    # NO ELIMINAR - Añadir tiendas a la lista de tiendas del centro comercial
    tiendas.append(tienda1)
    tiendas.append(tienda2)
    tiendas.append(tienda3)


    # NO ELIMINAR - Crear clientes de ejemplo
    cliente1 = Cliente(1,"Pedro García", "11111111A", "21001", 35,5,1000)
    cliente2 = Cliente(2,"Laura Torres", "22222222B", "21002", 28, 2,900)
    cliente3 = Cliente(3,"Miguel Fernández", "33333333C", "21003", 40, 3, 500)
    cliente4 = Cliente(4,"Sofía Ramírez", "44444444D", "21004", 32,21,500)
    cliente5 = Cliente(5,"Carlos Gómez", "55555555E", "21005", 30,5,1000)  # Cliente que es socio en las 3 tiendas
    cliente6 = Cliente(6,"Pedro Orozco", "66666666F", "21007", 49,4,100)
    cliente7 = Cliente(7,"Santiago Sancho", "77777777G", "21009", 37,5,1233)
    cliente8 = Cliente(8,"Daniel Perez", "88888888H", "21010", 46,5,3423)
    cliente9 = Cliente(9,"Lola García", "99999999I", "21035", 26,2,200)
    cliente10 = Cliente(10,"Ainara Sanchez", "10101010J", "21005", 21,5,344)
    cliente11 = Cliente(11,"Jesús Aguilar", "20202020K", "21045", 50,9,900)
    cliente12 = Cliente(12,"Carlos Frasco", "30303030L", "21002", 50,8,709)

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
        tienda=[]

        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            #TODO - Implementa la opción 1 - Añadir Tienda
            id = int(input("Ingrese el id del cliente: "))
            nombre = input("Ingrese el nombre del cliente: ")
            cif = input("Ingrese el cifra del cliente: ")
            tipo_tienda = input("Ingrese el tipo de tienda: ")
            propietario = input("Ingrese el propietario: ")
            numero_socios = int(input("Ingrese el numero socios: "))

            nueva_tienda = Tienda(id, nombre, cif, tipo_tienda, propietario, numero_socios)
            Tienda.crear_tienda(nueva_tienda)

        elif opcion == "2":
            #TODO - Implementa la opción 2 - Listar Tiendas
            print("Lista de tiendas creadas")
            Tienda.listar_tiendas()


        elif opcion == "3":
            #TODO - Implementa la opción 3 - Eliminar Tienda
            print("Ingrese id de tienda que quieras eliminar")
            id_tienda = input("Ingrese el id del tienda: ")
            Tienda.elimina_tienda(id_tienda)


        elif opcion == "4":
            #TODO - Implementa la opción 4 - Gestionar Tienda
            # Obviamente,esta opción debe llamar al otro menú, al que gestiona una única tienda

            nombre_tienda=input("Ingrese el nombre del tienda: ")
            gestionar_tienda(nombre_tienda)



        elif opcion == "5":
            #TODO - Implementa la opción 5 - Gestionar Socios
            # Obviamente,esta opción debe llamar a otro menú, al que gestiona los socios del cetro comercial
            print("Entrando al menu de gestion de clientes")
            gestionar_clientes()


        elif opcion == "6":
            break

