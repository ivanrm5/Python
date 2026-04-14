"""
Pide al usuario una cadena. Muestra
- numero total de caracteres
- numero de caracteres alfabeticos
- numero de espacios
- numero de digitos

USOS APLICADOS:
    • isalpha(): devuelve True si es una letra
    • isdigit(): devuelve True si es un número
    • len(): cuenta todos los caracteres
    • El bucle for recorre cada carácter uno a uno
"""

cadena=input("Introduce una cadena: ")

caracteres = len(cadena)
alfabeticos= 0
espacios= 0
digitos= 0

for caracter in cadena:
    if caracter.isalpha():
        alfabeticos += 1
    elif caracter == " ":
        espacios += 1
    elif caracter.isdigit():
        digitos += 1

#RESULTADOS

print(f"Total de caracteres: {caracteres}")
print(f"Caracteres alfabeticos: {alfabeticos}")
print(f"Total de espacios: {espacios}")
print(f"Total de digitos: {digitos}")

