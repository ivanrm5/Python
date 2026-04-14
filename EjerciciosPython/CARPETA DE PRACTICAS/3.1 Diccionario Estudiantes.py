"""
Pide nombre y edad de estudiantes
Guarde en un diccionario {nombre: edad}
Mostrar mayores de 18
Mostrar promedio de edad

DICCIONARIOS
.items() --> para ver clave y valor
.key() --> solo clave
.values() --> solo valor

"""

estudiantes={}

while True:
    nombre=input("Introduce nombre del estudiante: (0 para salir): ").strip()
    if nombre=="0":
        break
    try:
        edad=int(input(f"Edad de estudiante {nombre}: "))
        estudiantes[nombre]=edad #Añade nombre y edad al diccionario
    except ValueError:
        print("Introduce un numero valido")

if not estudiantes:
    print("No hay estudiantes")
    exit()

#MAYORES 18
print("MAYORES DE EDAD")
for nombre, edad in estudiantes.items():
    if edad >=18:
        print(f"Estudiante {nombre}: Edad: {edad}")

#PROMEDIO DE EDAD
promedio = sum(estudiantes.values())/len(estudiantes)
print(f"Promedio de edad: {promedio}")

