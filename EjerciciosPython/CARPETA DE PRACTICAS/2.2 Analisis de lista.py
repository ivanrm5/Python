"""
Dada una lista de numeros, muestra:
    - numeros pares --> numero%2==0
    - impares --> numero%2==1
    - cantidad de pares e impares  -->len()
"""

numeros=[2,2,4,4,5,6,6,8,9,10]
pares=[]
impares=[]

for numero in numeros:
    if numero%2==0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f"Numeros pares: {pares}")
print(f"Numeros impares: {impares}")
#cantidades
print(f"Cantidad de pares es: {len(pares)}")
print(f"Cantidad de impares es: {len(impares)}")