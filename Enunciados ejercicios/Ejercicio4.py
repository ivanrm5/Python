"""
Gestiona el inventario de una tienda.
Recoge por teclado los nombres de productos y precio unitario.
Genera un diccionario donde la clave es el nombre del producto y valor el precio unitario del producto.
Se pedira datos hasta escribir "fin". No permitir productos repetidos.
Tras terminar de insertar datos se pedira lo siguiente:
    - Insertar un presupuesto maximo (int)
    - Mostrar la lista con los valores menor o igual que el presupuesto insertado
"""

tienda={}

while True:
    producto=input("Ingrese un producto: ").lower().strip()

    if producto == "fin":
        break

    if producto not in tienda:
        precio=float(input("Ingrese un precio al producto: "))
        tienda[producto]=precio
    else:
        print(f"El producto {producto} ya existe")


print(f"Diccionario generado: {tienda}")

presupuesto=int(input("Presupuesto maximo: "))


filtro={}

for producto, precio in tienda.items():
    if precio <= presupuesto:
        filtro[producto]=precio

print(filtro)



