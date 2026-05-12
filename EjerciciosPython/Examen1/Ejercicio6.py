"""
EJERCICIO 6: INVERSOR DE NÚMEROS
Escribe un programa que:
- Pida números enteros hasta que introduzca 0
- Guarde los números en una lista
- Muestre la lista original
- Muestre la lista invertida
- Calcule la suma de todos los números
- Calcule el promedio
- Muestre el número mayor y el número menor

Ejemplo:
  Introduce un número (0 para salir): 10
  Introduce un número (0 para salir): 25
  Introduce un número (0 para salir): 5
  Introduce un número (0 para salir): 0

  Lista original: [10, 25, 5]
  Lista invertida: [5, 25, 10]
  Suma: 40
  Promedio: 13.33
  Mayor: 25
  Menor: 5
"""

lista_numeros=[]

while(True):
    numero=int(input("Introduce un numero (0 para salir): "))

    if numero==0:
        break

    lista_numeros.append(numero)

print(f"Lista original: {lista_numeros}")
print(f"Lista invertida: {lista_numeros[::-1]}")
print(f"Suma: {sum(lista_numeros)}")
print(f"Promedio: {sum(lista_numeros)/len(lista_numeros)}")
print(f"Mayor: {max(lista_numeros)}, Menor: {min(lista_numeros)}")


