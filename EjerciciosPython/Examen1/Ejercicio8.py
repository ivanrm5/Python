"""
EJERCICIO 8: VALIDADOR DE EMAILS
Escribe un programa que:
- Almacene emails en una lista
- El usuario puede: añadir, buscar, eliminar, mostrar todos
- Un email es válido si contiene @ y al menos un punto después de @
- Valida que no se repitan emails
- Menú simple (no menú de clase)

Ejemplo:
  1. Añadir email
  2. Buscar email
  3. Eliminar email
  4. Ver todos
  5. Salir

  Selecciona opción: 1
  Introduce email: juan@gmail.com
  Email añadido

  Selecciona opción: 2
  Introduce email a buscar: juan@gmail.com
  Email encontrado

  Selecciona opción: 4
  Emails guardados: ['juan@gmail.com']
"""

emails=[]

while True:
    print("1. Añadir un email")
    print("2. Buscar email")
    print("3. Eliminar email")
    print("4. Ver todos")
    print("5. Salir")

    opcion= int(input("Introduce una opcion: "))

    if opcion == 1:
        email=input("Introduce un email (tiene que contener @ y un .): ").strip()

        if email in emails:
            print("\nEste email ya existe")
        else:
            emails.append(email)
            print("\nEmail creado correctamente")


    if opcion == 2:

        email_buscado=input("Introduce un email para buscar: ").strip()
        if email_buscado in emails:
            print(f"Existe este email: {email_buscado}")
        else:
            print(f"Este email no existe: {email_buscado}")


    if opcion == 3:
        eliminar_email=input("Introduce un email para eliminar: ").strip()
        if eliminar_email not in emails:
            print(f"Este email no existe: {eliminar_email}")
        else:
            emails.remove(eliminar_email)
            print("\nEmail eliminado correctamente")


    if opcion == 4:
        if emails:
            print("Emails guardados", emails)
        else:
            print("No existen emails")

    if opcion == 5:
        break