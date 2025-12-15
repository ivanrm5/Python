"""
Ejercicio 1
Escribe un programa que solicite una cadena y cuente cuantos caracteres alfabeticos contiene y cuantos caracteres
no alfabeticos contiene (incluye espacios, signos, numeros).
Tambien debera mostrar la cadena en orden inverso y en mayusculas:
"""

cadena = input("Introduce una cadena: ")

contador_alfabeticos = 0
contador_noAlfabeticos = 0

for caracter in cadena:
    if caracter.isalpha():
        contador_alfabeticos += 1
    else:
        contador_noAlfabeticos += 1

print("Caracteres alfabéticos:",contador_alfabeticos)
print("Caracteres no alfabéticos:",contador_noAlfabeticos)
print("Invertida en mayúsculas",cadena.upper() [::-1])