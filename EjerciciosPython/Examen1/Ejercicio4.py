"""
Ejercicio4
Escribir nombre y cantidad de habitantes de ciudades sin repetirse y termina cuando ponga 0, generar diccionario.
Cuando termine de crear el diccionario, pedira por teclado un número de habitantes y mostrara el diccionario con nombre
y cantidad de habitantes con el número menor introducido.
"""

poblacion={}


while True:
    ciudad=input("Introduce una ciudad: (0 para salir): ").strip()
    if ciudad == "0" :
        break

    if ciudad in poblacion:
        print("Ya existe un poblacion en el diccionario")

    habitantes=int(input("Introduce una cantidad de habitantes: ").strip())
    poblacion[ciudad]=habitantes


cantidad_habitantes=int(input("Introduce una cantidad de habitantes a buscar en el diccionario: "))

filtro={ciudad: hab for ciudad, hab in poblacion.items() if hab < cantidad_habitantes}

print("Diccionario completo")
print(poblacion)

print("Con filto")
print(filtro)

