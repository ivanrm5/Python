"""
Crea una clase Producto con:
    - Atributos: id, nombre, precio
    - Metodo que calcule precio con 21% IVA
    - Metodo _str_ para mostrar informacion
    - Atributo estatico para contar productos
"""

class Producto:

    contador=0

    def __init__(self,id,nombre,precio):
        self.id=Producto.contador+1
        self.nombre=nombre
        self.precio=precio
        Producto.contador+=1

    def precio_iva(self):
        "Precio de la compra mas IVA"
        return self.precio*1.21

    def __str__(self):
        return f"Producto {self.id}: {self.nombre} precio: {self.precio}"

pr1 = Producto(1, "Nombre",500)
pr2 = Producto(2, "Precio",100)

print(pr1)
print(pr2)
print("PRECIO CON IVA")
print(pr1.precio_iva())
print(pr2.precio_iva())
