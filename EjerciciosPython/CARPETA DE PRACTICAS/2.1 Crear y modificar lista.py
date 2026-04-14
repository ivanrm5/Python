"""
Pide numeros hasta que escriba salir
Guarda los numeros en una lista
Muestre el maximo y minimo y promedio
Ordene la lista y muestrala

USOS:
- try/except --> para comprobar si es un numero entero en la cadena
- .append() --> papra añadir a la lista
- .max(), .min(), .sum() --> maximo, minimo, media
- .sort() --> ordenar lista
- NOT numeros --> verificar si la linea esta vacia
"""

numeros=[]

while(True):
    n=input("introduce un numero o salir: ")
    if n.lower()=="salir":
        break

    try:
        numero = float(n)
        numeros.append(numero)
    except ValueError:
        print("introduce un numero correctamente")

if not numeros:
    print("No hay numeros")
    exit()

promedio= sum(numeros)/len(numeros)

#RESULTADOS
print(f"Numero maximo: {max(numeros)}")
print(f"Numero minimo: {min(numeros)}")
print(f"Media de numeros: {promedio: .2f}")
numeros.sort()
print(f"lisa ordenada: {numeros}")