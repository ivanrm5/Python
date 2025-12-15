"""
Ejercicio3
Introducir una cadena de texto y crear un diccionario, contar las consonantes de cada palabra del diccionario.
"""

cadena = input("Introduce una cadena: ")

palabras = cadena.split()
vocales="aeiou"
diccionario = {}

for palabra in palabras:
    contador=0
    for caracter in palabra:
        if caracter.isalpha() and caracter in vocales:
            contador += 1
    diccionario[palabra] = contador
print (diccionario)

