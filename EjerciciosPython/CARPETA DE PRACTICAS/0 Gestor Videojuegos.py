"""
PROYECTO GESTOR DE TIENDA DE VIDEOJUEGOS
"""

class Videojuego:

    contador_videojuegos=0
    def __init__(self, titulo, plataforma, precio, stock, clasificacion_edad):
        Videojuego.contador_videojuegos+=1
        self.id_videojuego=Videojuego.contador_videojuegos
        self.titulo=titulo
        self.plataforma=plataforma
        self.precio=precio
        self.stock=stock
        self.clasificacion_edad=clasificacion_edad
        self.unidades_vendidas= 0

    def __str__(self):
        """String representation del Videojuego"""
        return (f"ID: {self.id_videojuego}: Titulo: { self.titulo}, Plataforma: {self.plataforma}, stock: {self.stock}"
                f", PEGI: {self.clasificacion_edad}, Vendidas: {self.unidades_vendidas}")

    def vender(self):
        self.stock-=1
        self.unidades_vendidas+=1

    def reabastecer(self):
        self.stock+=1



class Cliente:
    contador_clientes=0

    def __init__(self, nombre, email, edad, dinero_gastado):
        Cliente.contador_clientes+=1
        self.id_cliente=Cliente.contador_clientes
        self.nombre=nombre
        self.email=email
        self.edad=edad
        self.dinero_gastado=0
        self.videojuegos_comprados=[] #lista de compras

    def __str__(self):
        """"String representación del Cliente """
        return (f"ID: {self.id_cliente}: Nombre: {self.nombre}, email:{self.email}, "
                f"edad: {self.edad}, Dinero Gastado:{self.dinero_gastado}, Videojuegos comprados: {len(self.videojuegos_comprados)}")


    def comprar_videojuego(self, videojuego):
        self.videojuegos_comprados.append(videojuego)
        self.dinero_gastado += videojuego.precio

    def devolver_videojuego(self, videojuego):
        self.videojuegos_comprados.remove(videojuego)
        self.dinero_gastado += videojuego.precio

    def obtener_videojuegos(self):
        return self.videojuegos_comprados


#funciones principales o generales / MENU

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "=" * 50)
    print("--- Menú de Gestión del Centro Comercial ---")
    print("=" * 50)
    print("1. Listar videojuegos")
    print("2. Listar Clientes")
    print("3. Vender Videojuego")
    print("4. Devolver videojuego")
    print("5. Ver videojuegos del cliente")
    print("6. Videojuegos por plataforma")
    print("7. salir")
    print("=" * 50)

def buscar_videojuego_por_id(id_videojuego, videojuegos):
    for videojuego in videojuegos:
        if videojuego.id_videojuego == id_videojuego:
            return videojuego
    print(f"Videojuego no encontrado con ID: {id_videojuego}")
    return None


def buscar_cliente_por_id(id_cliente, clientes):
    for cliente in clientes:
        if cliente.id_cliente == id_cliente:
            return cliente

    print(f"Cliente no encontrado con ID: {id_cliente}")
    return None


def videojuegos_por_plataforma(plataforma, videojuegos):
    encontrado=[]
    for videojuego in videojuegos:
        if videojuego.plataforma.lower() == plataforma.lower():
            encontrado.append(videojuego)

    if not encontrado:
        print("No hay videojuegos de esta plataforma")

    return encontrado

if __name__ == "__main__":
    videojuegos=[]
    clientes=[]

    videojuego1 = Videojuego("Zelda", "Nintendo", 70, 15,7)
    videojuego2 = Videojuego("Elden Ring", "PlayStation 5", 59, 8,16)
    videojuego3 = Videojuego("Super Mario Odyssey", "Nintendo", 49, 12,3)
    videojuego4 = Videojuego("God of War", "PlayStation 5", 69, 5,18)
    videojuego5 = Videojuego("League of Legends", "PC", 0, 0, 12)

    videojuegos.append(videojuego1)
    videojuegos.append(videojuego2)
    videojuegos.append(videojuego3)
    videojuegos.append(videojuego4)
    videojuegos.append(videojuego5)


    cliente1 = Cliente("Pedro", "pedro@gmail.com", 28, 0)
    cliente2 = Cliente("Maria", "maria@gmail.com", 18, 0)
    cliente3 = Cliente("Laura", "laura@gmail.com", 16, 0)

    clientes.append(cliente1)
    clientes.append(cliente2)
    clientes.append(cliente3)


    while True:
        mostrar_menu()
        opcion = input("Introduce una opcion: ")

        if opcion == "1":
            #Listar videojuegos
            for videojuego in videojuegos:
                print(f"{videojuego}")

        if opcion == "2":
            #Listar clientes
            for cliente in clientes:
                print(f"{cliente}")

        #Vender videojuego
        if opcion == "3":
            try:
                #PASO 1 PEDIR ID
                id_videojuego = int(input("Introduce un id de videojuego: "))
                id_cliente = int(input("Introduce un id de cliente: "))

                #BUSCAR VIDEOJUEGO
                videojuego_encontrado = buscar_videojuego_por_id(id_videojuego, videojuegos)
                if not videojuego_encontrado:
                    continue

                #Buscar cliente
                cliente_encontrado = buscar_cliente_por_id(id_cliente, clientes)
                if not cliente_encontrado:
                    continue

                #Validar edad
                if cliente_encontrado.edad < videojuego_encontrado.clasificacion_edad:
                    print(f"El cliente es muy joven {cliente_encontrado.edad}, el PEGI es: {videojuego_encontrado.clasificacion_edad} ")
                    continue

                if videojuego_encontrado.stock <=0:
                    print("No hay stock")
                    continue

                #Proceso de venta
                videojuego_encontrado.vender()
                cliente_encontrado.comprar_videojuego(videojuego_encontrado)

                print(f"El cliente {cliente_encontrado.nombre} compro {videojuego_encontrado.titulo}")


            except ValueError:
                print("ERROR")

        if opcion == "4":
            #Devolver videojuego


            id_cliente= int(input("Introduce un id de cliente: "))

            cliente_encontrado = buscar_cliente_por_id(id_cliente, clientes)

            if not cliente_encontrado:
                continue

            videojuegos_cliente= cliente_encontrado.obtener_videojuegos()

            if not videojuegos_cliente:
                print("No hay videojuegos")
                continue

        







