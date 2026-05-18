"""
EJERCICIO 9: CALCULADORA DE NOTAS
Escribe un programa que:
- Guarde nombres de estudiantes y sus 3 notas
- Calcule el promedio de cada estudiante
- Muestre quién aprobó (nota >= 5) y quién no
- Muestre la nota más alta y más baja de todo el grupo
- Cuente cuántos aprobaron y cuántos suspendieron
- Muestre lista ordenada por calificación

Ejemplo:
  Nombre del estudiante (o 'fin' para terminar): Juan
  Nota 1: 7
  Nota 2: 8
  Nota 3: 6
  Nombre del estudiante (o 'fin' para terminar): María
  Nota 1: 4
  Nota 2: 5
  Nota 3: 4
  Nombre del estudiante (o 'fin' para terminar): fin

  Estudiante | Promedio | Estado
  Juan       | 7.00     | Aprobado
  María      | 4.33     | Suspendido

  Nota más alta: 7.0
  Nota más baja: 4.33
  Aprobados: 1
  Suspendidos: 1
"""

estudiantes={}

while(True):
    nombre_estudiante=input("Nombre del estudiante (o 'fin' para terminar): ").strip()

    if nombre_estudiante.lower() == "fin":
        break

    nota1=float(input("Nota 1: "))
    nota2=float(input("Nota 2: "))
    nota3=float(input("Nota 3: "))

    promedio=(nota1+nota2+nota3)/3

    estudiantes[nombre_estudiante]=promedio




if estudiantes:
    print("\n Estudiante | Promedio | Estado")

    aprobados = 0
    suspendidos = 0

    for nombre, promedio in estudiantes.items():
        if promedio >= 5:
            estado="Aprobado"
            aprobados += 1
        else:
            estado="Suspendido"
            suspendidos += 1

        print(f"{nombre} | {promedio} | {estado}")


promedios=list(estudiantes.values())

print("\nEstadisticas")
print(f"Nota mas alta: {max(promedios)}")
print(f"Nota mas baja: {min(promedios)}")
print(f"Aprobados: {aprobados}")
print(f"Suspendidos: {suspendidos}")


print("\n Lista ordenada por calificación")

lista_ordenada=sorted(estudiantes.items(), key=lambda x: x[1], reverse=True)
print(lista_ordenada)

#Recordad en listas .items() se refiere a la clave y el valor:::
#.values() se refiere al valor que tiene la clave dentro del item.

