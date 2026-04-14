"""
Verifica si un numero es primo (divisible en 1 y el mismo)
"""

numero=int(input("Ingrese un numero: "))

for n in range(2,numero):
    if numero%n==0:
        print("No es primo")
        break
    else:
        print("Es primo")
        break