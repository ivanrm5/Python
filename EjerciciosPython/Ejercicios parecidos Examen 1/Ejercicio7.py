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


frase=input("Introduce una frase: ").lower()
diccionario={}

contador_letras=0

for caracter in frase:
    if caracter.isalpha():
        if caracter in diccionario:
            diccionario[caracter]+=1
        else:
            diccionario[caracter]=1

print(f"{diccionario}")



print("Ordenado por frecuencia:")
diccionario_ordenado=sorted(diccionario.items(), key=lambda x: x[1], reverse=True)
for letra, count in diccionario_ordenado:
    print(f"{letra}: {count}")