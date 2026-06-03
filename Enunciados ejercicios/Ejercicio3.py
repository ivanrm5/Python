"""
Escribe una cadena de texto y crea un diccionario.
Las claves seran las palabras de la cadena en minusculas y los valores la longitud de dicha palabra
"""

cadena=input("Ingresa un cadena de texto: ").lower()
cadena_diccionario={}

for palabra in cadena.split():
    cadena_diccionario[palabra]=len(palabra)

print(cadena_diccionario)