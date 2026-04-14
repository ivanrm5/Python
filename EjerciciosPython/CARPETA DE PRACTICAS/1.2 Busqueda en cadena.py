"""
Pide una frase y una palabra. Muestra:
    • - Si la palabra está en la frase
    • - Cuántas veces aparece
    • - Posición de la primera aparición

USOS APLICADOS
    • ✓ in: verifica si una subcadena está en el string
    • ✓ .count(): cuenta cuántas veces aparece una subcadena
    • ✓ .find(): devuelve la posición (-1 si no existe)
    • ✓ .lower(): convertimos a minúsculas para búsqueda sin importar mayúsculas
"""

cadena=input("Introduce una cadena: ").lower()
palabra=input("Introduce una palabra: ").lower()

if palabra in cadena:
    print(f"La palabra {palabra} esta en la frase")
else:
    print(f"La palabra {palabra} no existe")

contador=cadena.count(palabra)
print(f"{contador} veces aparece")

posicion=cadena.find(palabra)
print(f"Esta en la posicion {posicion}")