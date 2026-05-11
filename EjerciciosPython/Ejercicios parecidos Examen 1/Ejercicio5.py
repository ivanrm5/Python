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
from EjerciciosPython.Examen1.Ejercicio2 import contador_letras

contador_noAlfabeticos=0
contador_alfabeticos=0
contador_letras=0

palabra=input("Introduce una palabra: ").lower()
vocales={"a","e","i","o","u"}

palindromo = palabra[::-1]

if palabra == palindromo:
    print(palabra, "Es palindromo")
else:
    print(palabra, "No es palindromo")

for letra in palabra:
    if letra.isalpha():
        contador_letras += 1
        if letra in vocales:
            contador_alfabeticos += 1
        else:
            contador_noAlfabeticos += 1

    print(letra)
print(f"Letras, {contador_letras}")
print(f"Vocales,{contador_alfabeticos}")
print("Consonantes",contador_noAlfabeticos)