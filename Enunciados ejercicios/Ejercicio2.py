"""
Introducir una frase y determine si es creciente (cada palabra de la frase es mas larga que la anterior)
Mostrar longitudes de cada palabra de la frase e indicar cantidad de palabras
"""

cadena=input("Ingresa un cadena de texto: ").lower()
palabras=cadena.split()

print(f"Cantidad de palabras: {len(palabras)}")

#Longitud de cada palabra

for palabra in palabras:
    print(f"Longitud de palabra: {len(palabra)} caracteres")


es_creciente=True

for i in range(1, len(palabras)):
    if len(palabras[i])<=len(palabras[i-1]):
        es_creciente=False
        break

if es_creciente and len(palabras)>0:
    print ("La frase es creciente")
else:
    print ("La frase no es creciente")