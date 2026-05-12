"""
EJERCICIO 5: ANALIZADOR DE PALABRAS
Escribe un programa que pida una palabra y determine:
- Si es un palíndromo (se lee igual al revés)
- Cuantas letras tiene
- Cuantas vocales tiene
- Cuantas consonantes tiene
- Mostrar la palabra con cada carácter en una línea

Ejemplo:
  Introduce una palabra: radar
  Es palíndromo: Sí
  Letras: 5
  Vocales: 2
  Consonantes: 3
  Caracteres:
  r
  a
  d
  a
  r
"""

palabra = input("Introduce una palabra: ").lower()

es_palindromo = palabra == palabra[::-1]

vocales = {"a", "e", "i", "o", "u"}

contador_letras = 0
contador_vocales = 0
contador_consonantes = 0

for c in palabra:
    if c.isalpha():
        contador_letras += 1
        if c in vocales:
            contador_vocales += 1
        else:
            contador_consonantes += 1


print(f"Es palindromo: {'Si' if es_palindromo else 'No'}")
print(f"Letras: {contador_letras}")
print(f"Vocales: {contador_vocales}")
print(f"Consonantes: {contador_consonantes}")

print("Caracteres: ")
for caracter in palabra:
    if caracter.isalpha():
        print(caracter)

