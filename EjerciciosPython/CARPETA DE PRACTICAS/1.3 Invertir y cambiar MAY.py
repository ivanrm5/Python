"""
Pide una palabra y muestra:
    • - La palabra invertida
    • - La palabra en mayúsculas
    • - La palabra en minúsculas
    • - La primera letra en mayúscula y el resto en minúsculas

USOS APLICADOS:
    • palabra[::-1] invierte el string (slicing con paso -1)
    • .upper() / .lower() / .capitalize() no cambian la variable original
    • Estos métodos devuelven un NUEVO string
"""

palabra = input("Introduce una palabra: ")

print(palabra.upper()) #MAYUSCULA
print(palabra.lower()) #MINUSCULA
print(palabra[::-1]) #IMPRIMIR AL REVES
print(palabra.capitalize()) #PRIMERA LETRA MAYUS