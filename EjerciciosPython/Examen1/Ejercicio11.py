"""
EJERCICIO 11: ANALIZADOR DE LISTA DE NÚMEROS
Escribe un programa que:
- Lea números hasta que se introduzca -1
- Guarde solo los números válidos (enteros entre 0 y 1000)
- Cuente cuántos números hay en cada rango:
  * 0-100
  * 101-200
  * 201-300
  * ... hasta 901-1000
- Calcule media, máximo y mínimo
- Muestre en qué rango está cada número

Ejemplo:
  Introduce número (−1 para salir): 50
  Introduce número (−1 para salir): 150
  Introduce número (−1 para salir): 75
  Introduce número (−1 para salir): -1

  Números válidos: [50, 150, 75]

  Distribución por rangos:
  0-100: 2
  101-200: 1
  201-300: 0
  ...

  Media: 91.67
  Máximo: 150
  Mínimo: 50
"""


numeros_validos=[]
rangos={
    '0-100':0,
    '101-200':0,
    '201-300':0,
    '301-400':0,
    '401-500':0,
    '501-600':0,
    '601-700':0,
    '701-800':0,
    '801-900':0,
    '901-1000':0,
}


while(True):
    numero=int(input("Ingrese un numero (DEL 0-1000, -1 para salir): "))

    if numero == -1:
        break

    if numero < 0 or numero > 1000:
        print("Numero invalido")
    else:
        numeros_validos.append(numero)


if numeros_validos:
    for numero in numeros_validos:
        if numero <= 100:
            rangos['0-100']+=1
        elif numero <= 200:
            rangos['101-200']+=1
        elif numero <= 300:
            rangos['201-300']+=1
        elif numero <= 400:
            rangos['301-400']+=1
        elif numero <= 500:
            rangos['401-500']+=1
        elif numero <= 600:
            rangos['501-600']+=1
        elif numero <= 700:
            rangos['601-700']+=1
        elif numero <= 800:
            rangos['701-800']+=1
        elif numero <= 900:
            rangos['801-900']+=1
        else:
            rangos['901-1000']+=1

    print(f"Numeros validos: {numeros_validos}")

    print(f"Distribucion por rangos: {rangos}")

    for rango, cantidad in rangos.items():
        print(f"{rango}: {cantidad}")

    print(f"\nMedia: {sum(numeros_validos)/len(numeros_validos)}")
    print(f"Max: {max(numeros_validos)}")
    print(f"Min: {min(numeros_validos)}")

else:
    print("No hay numeros validos")


