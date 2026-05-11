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

numeros = []

while True:
    numero=int(input("Introduce un numero: "))
    if numero == 0:
        break
    numeros.append(numero)

print(f"Lista original: {numeros}")
print(f"Lista invertida: {numeros[::-1]}")
print(f"Suma de todos los numeros: {sum(numeros)}")
print(f"Promedio: {sum(numeros)/len(numeros)}")
print(f"Numero mayor {max(numeros)}, numero menor {min(numeros)}")

