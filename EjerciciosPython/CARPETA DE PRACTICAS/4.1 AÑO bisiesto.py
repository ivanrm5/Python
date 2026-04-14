"""
Pide un año y dice si es bisiesto

-Divisible por 400, divisible por 4 pero no por 100

"""

year=int(input("Introduce un numero entero: "))
if year%4==0 and year%100!=0 or year%400==0:
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")