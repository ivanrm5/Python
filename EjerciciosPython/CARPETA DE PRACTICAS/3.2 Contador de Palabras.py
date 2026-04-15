"""
Pide una frase y cuenta cuantas veces aparece cada palabra

if clave in diccionario:
    diccionario[clave]+=1
else:
    diccionario[clave]=1
"""

cadena=input("introduce una cadena de texto: ").lower()
palabras=cadena.split() #.split()--> Crea un diccionario

contador={}

for palabra in palabras:
    if palabra in contador:
        contador[palabra]+=1
    else:
        contador[palabra]=1

print(f"Palabras en diccionario: {palabras} y veces repetidas: {contador}")


