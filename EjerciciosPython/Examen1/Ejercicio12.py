"""
EJERCICIO 12: FORMATEADOR DE TEXTO CON ESTADÍSTICAS
Escribe un programa que:
- Lea un texto por teclado
- Cuente palabras, letras, números, espacios, signos
- Muestre estadísticas
- Encuentre la palabra más larga y más corta
- Busque una palabra específica y reemplacela

Ejemplo:
  Introduce texto: Hola mundo 123! Este es un texto.

  Estadísticas:
  Palabras: 6
  Letras: 21
  Números: 3
  Espacios: 6
  Signos: 1

  Palabra más larga: "mundo" (6 letras)
  Palabra más corta: "es" (2 letras)

  Introduce palabra a buscar: mundo
  "mundo" aparece 1 vez

  Introduce reemplazo: tierra
  Resultado: Hola tierra 123! Este es un texto.
"""

cadena=input("Introduce texto: ").lower()

contador_palabras=0
contador_letras=0
contador_numeros=0
contador_espacios=0
contador_signos=0

#Contador de palabras
for palabra in cadena.split():
    contador_palabras+=1

#Contador de letras
for letra in cadena:
    if letra.isalpha():
        contador_letras+=1
    elif letra.isdigit():
        contador_numeros+=1
    elif letra.isspace():
        contador_espacios+=1
    else:
        contador_signos+=1

print(f"Cantidad de palabras: {contador_palabras}")
print(f"Cantidad de letras: {contador_letras}")
print(f"Cantidad de numeros: {contador_numeros}")
print(f"Cantidad de espacios: {contador_espacios}")
print(f"Cantidad de signos: {contador_signos}")

if cadena.split():
    palabra_larga= max(cadena.split(), key=len)
    palabra_corta= min(cadena.split(), key=len)
    print(f"Palabra mas larga: {palabra_larga}")
    print(f"Palabra corta: {palabra_corta}")


#Buscar y reemplazar

palabra_buscar=input("Introduce texto: ").lower()
apariciones= cadena.count(palabra_buscar)
print(f"{palabra_buscar}: {apariciones}")


palabra_remplazo=input("Introduce texto: ").lower()
cadena_modificada=cadena.replace(palabra_buscar, palabra_remplazo)

print(f"Resultado de cadena nueva {cadena_modificada}")
