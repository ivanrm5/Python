"""
EJERCICIO 7: CONTADOR DE CARACTERES EN DICCIONARIO
Escribe un programa que:
- Pida una frase
- Cuente cuantas veces aparece cada letra (ignorando mayúsculas/minúsculas)
- Cree un diccionario con las letras y sus conteos
- Muestre el diccionario
- Ordene las letras por número de apariciones (mayor a menor)

Ejemplo:
  Introduce una frase: hello world
  Diccionario: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
  Ordenado por frecuencia:
  l: 3
  o: 2
  h: 1
  e: 1
  w: 1
  r: 1
  d: 1
"""

frase=input("Ingrese una frase: ")
diccionario={}

for caracter in frase:
    if caracter.isalpha():
        if caracter in diccionario:
            diccionario[caracter]+=1
        else:
            diccionario[caracter]=1

print(f"Diccionario: {diccionario}")

print("\nOrdenar por frecuencia: ")

#Ordenar un diccionario por mayor valor
valores_unicos= sorted(set(diccionario.values()),  reverse=True)

for valor in valores_unicos:
    for letra, count in diccionario.items():
        if count == valor:
            print(f"{letra}: {valor}")


#Ordenar diccionario por clave
diccionario2= diccionario.copy()

print("\nOrdenacion por clave")
orden_clave = sorted(diccionario2.items())
for clave, valor in orden_clave:
    print(f"{clave}: {valor}")

print(orden_clave)


