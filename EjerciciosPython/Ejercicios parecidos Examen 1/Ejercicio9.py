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

estudiantes = {}


while True:
    nombre = input("Nombre del estudiante (o 'fin' para terminar): ").strip()
    if nombre.lower() == "fin":
        break

    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))

    promedio = (nota1 + nota2 + nota3) / 3
    estudiantes[nombre] = promedio

# Mostrar resultados
if estudiantes:
    print("\n" + "Estudiante | Promedio | Estado".center(40))
    print("-" * 40)

    aprobados = 0
    suspendidos = 0

    for nombre, promedio in estudiantes.items():
        estado = "Aprobado" if promedio >= 5 else "Suspendido"
        if promedio >= 5:
            aprobados += 1
        else:
            suspendidos += 1
        print(f"{nombre:10} | {promedio:8.2f} | {estado}")

    # Estadísticas
    promedios = list(estudiantes.values())
    print("\n--- Estadísticas ---")
    print(f"Nota más alta: {max(promedios):.2f}")
    print(f"Nota más baja: {min(promedios):.2f}")
    print(f"Aprobados: {aprobados}")
    print(f"Suspendidos: {suspendidos}")

    # Ordenar por calificación
    print("\nOrdenado por calificación (mejor a peor):")
    ordenado = sorted(estudiantes.items(), key=lambda x: x[1], reverse=True)
    for nombre, promedio in ordenado:
        print(f"{nombre}: {promedio:.2f}")
else:
    print("No introdujiste estudiantes")

