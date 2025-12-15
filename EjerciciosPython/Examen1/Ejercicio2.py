"""
Ejercicio 2
Escribe un programa que pida al usuario introducir una frase y determine si la frase es plana.
Es decir, si todas las palabras de la frase tienen la misma longitud (ignorando signos de puntuación),
indicando el número de caracteres de cada palabra.
También debe indicar cuantas palabras tiene la frase, entendiendo que cada palabra esta separada por espacios.
"""

cadena=input("Introduce una cadena: ")
contador_letras = 0

if len(cadena.split()[0]) == len(cadena.split()[1]):
   print(cadena, "es plana")
else:
   print(cadena, "no es plana")

for caracter in cadena.split():
    if caracter != " ":
        contador_letras += 1
print(contador_letras)


print("La frase tiene",len(cadena.split()),"palabras")