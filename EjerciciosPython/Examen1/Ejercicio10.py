"""
EJERCICIO 10: CALCULADORA DE CONVERSIONES DE UNIDADES
Escribe un programa que:
- Cree un diccionario con conversiones (metros a cm, km, mm, etc.)
- Pida por teclado una cantidad y la unidad origen
- Pida la unidad destino
- Valide que las unidades sean válidas
- Muestre la conversión

Conversiones base (metro = 1):
  - mm: 1000
  - cm: 100
  - m: 1
  - km: 0.001
  - milla: 0.000621371

Ejemplo:
  Introduce cantidad: 5
  Unidad origen (mm/cm/m/km/milla): cm
  Unidad destino (mm/cm/m/km/milla): m
  5 cm = 0.05 m
"""

conversiones={
    'mm': 1000,
    'cm': 100,
    'm': 1,
    'km': 0.001,
    'milla': 0.000621371,
}

cantidad=int(input("Introduce un numero: "))
unidad_origen=input("Introduce la unidad de origen (mm, cm, m, km, milla): ").lower()
unidad_destino=input("Introduce la unidad de destino (mm, cm, m, km, milla): ").lower()

if unidad_origen not in conversiones or unidad_destino not in conversiones:
    print("No existe esa unidad de medida")
else:
    #Realizar conversion
    metros= cantidad/conversiones[unidad_origen]
    resultado = metros * conversiones[unidad_destino]
    print(f"{cantidad} {unidad_origen} = {resultado} {unidad_destino}")


