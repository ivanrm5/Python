"""
Escribir una cadena de texto al usuario y caracter de "relleno".
Contar vocales y espacios en blanco de la cadena.
Generar una nueva cadena con un caracter nuevo que sustituya los espacios
Mostrar cadena nueva en MAYUS
"""

cadena = input("Ingresa una cadena de texto: ").lower()
vocales={"a", "e", "i", "o", "u"}

contar_vocales=0
contar_espacios=0


for caracter in cadena:
    if caracter in vocales:
        contar_vocales += 1
    elif caracter == " ":
        contar_espacios += 1


relleno=input("Ingresa un caracter especia para rellenar el espacio: ")

cadena_nueva=cadena.replace(" ", relleno)

print(f"Cadena original: {cadena}")
print(f"Vocales: {contar_vocales}")
print(f"Espacios: {contar_espacios}")
print(f"Resultado: {cadena_nueva.upper()}")
