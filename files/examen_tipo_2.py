"""
EXAMEN TIPO 2: GESTOR DE INVENTARIO DE TIENDA
Estructura base completa - Solo implementa los TODO
"""

class Producto:
    """Representa un producto en el inventario"""
    contador_productos = 0
    
    def __init__(self, nombre, categoria, precio, cantidad_stock):
        Producto.contador_productos += 1
        self.id_producto = Producto.contador_productos
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad_stock = cantidad_stock
        self.unidades_vendidas = 0

    def __str__(self):
        return f"Producto {self.id_producto}: {self.nombre} ({self.categoria}) - {self.precio}€, Stock: {self.cantidad_stock}"

    # TODO: Implementar método vender
    def vender(self, cantidad):
        """Vende una cantidad del producto si hay stock"""
        pass

    # TODO: Implementar método reabastecer
    def reabastecer(self, cantidad):
        """Añade stock al producto"""
        pass

    # TODO: Implementar método obtener_valor_stock
    def obtener_valor_stock(self):
        """Devuelve el valor total del stock (cantidad * precio)"""
        pass


class Venta:
    """Representa una venta realizada"""
    contador_ventas = 0
    
    def __init__(self, id_producto, cantidad):
        Venta.contador_ventas += 1
        self.id_venta = Venta.contador_ventas
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.total = 0.0

    def __str__(self):
        return f"Venta {self.id_venta}: Producto {self.id_producto}, Cantidad: {self.cantidad}, Total: {self.total}€"

    # TODO: Implementar método calcular_total
    def calcular_total(self, precio_unitario):
        """Calcula el total de la venta"""
        pass


def mostrar_menu():
    print("\n" + "="*50)
    print("--- GESTOR DE INVENTARIO ---")
    print("="*50)
    print("1. Listar Productos")
    print("2. Vender Producto")
    print("3. Reabastecer Producto")
    print("4. Ver Valor Total de Stock")
    print("5. Ver Productos por Categoría")
    print("6. Listar Ventas Realizadas")
    print("7. Ingresos Totales")
    print("8. Salir")
    print("="*50)


# TODO: Implementar función buscar_producto_por_id
def buscar_producto_por_id(id_producto, productos):
    """Busca un producto por su ID"""
    pass


# TODO: Implementar función productos_por_categoria
def productos_por_categoria(categoria, productos):
    """Devuelve todos los productos de una categoría"""
    pass


# TODO: Implementar función valor_total_stock
def valor_total_stock(productos):
    """Calcula el valor total de todo el stock"""
    pass


# TODO: Implementar función ingresos_totales
def ingresos_totales(ventas):
    """Calcula el total de ingresos por ventas"""
    pass


if __name__ == "__main__":
    # Listas globales
    productos = []
    ventas = []

    # Crear productos de ejemplo
    p1 = Producto("Laptop", "Electrónica", 800, 5)
    p2 = Producto("Ratón", "Electrónica", 25, 50)
    p3 = Producto("Teclado", "Electrónica", 75, 30)
    p4 = Producto("Monitor", "Electrónica", 300, 10)
    p5 = Producto("Silla Gamer", "Muebles", 200, 8)
    p6 = Producto("Escritorio", "Muebles", 150, 12)

    productos.extend([p1, p2, p3, p4, p5, p6])

    # Programa principal
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Listar productos
            print("\nProductos en inventario:")
            for producto in productos:
                print(f"  {producto}")

        elif opcion == "2":
            # Vender producto
            try:
                print("\nProductos disponibles:")
                for p in productos:
                    if p.cantidad_stock > 0:
                        print(f"  [{p.id_producto}] {p.nombre} - {p.precio}€ ({p.cantidad_stock} en stock)")
                
                id_producto = int(input("ID del producto a vender: "))
                cantidad = int(input("Cantidad a vender: "))
                
                # TODO: Implementar lógica de venta
                pass

        elif opcion == "3":
            # Reabastecer
            try:
                id_producto = int(input("ID del producto: "))
                cantidad = int(input("Cantidad a reabastecer: "))
                
                # TODO: Implementar lógica de reabastecimiento
                pass

        elif opcion == "4":
            # Valor total de stock
            # TODO: Implementar y mostrar valor total
            pass

        elif opcion == "5":
            # Productos por categoría
            categoria = input("Nombre de la categoría: ")
            # TODO: Implementar búsqueda y mostrar
            pass

        elif opcion == "6":
            # Listar ventas
            print("\nVentas realizadas:")
            for venta in ventas:
                print(f"  {venta}")

        elif opcion == "7":
            # Ingresos totales
            # TODO: Implementar y mostrar ingresos
            pass

        elif opcion == "8":
            print("\n¡Hasta luego!")
            break

        else:
            print("❌ Opción no válida")
