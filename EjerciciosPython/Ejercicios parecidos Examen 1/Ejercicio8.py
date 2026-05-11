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

emails = []

def email_valido(email):
    if "@" not in email:
        return False
    partes = email.split("@")
    if len(partes) != 2:
        return False
    if "." not in partes[1]:
        return False
    return True

while True:
    print("\nGESTOR DE EMAILS")
    print("1. Crear email")
    print("2. Buscar email")
    print("3. Eliminar email")
    print("4. Ver todos")
    print("5. Salir")

    opcion = int(input("Introduce una opcion: "))

    if opcion == 1:
        email = input("Introduce email: ").strip()
        if email_valido(email):
            if email in emails:
                print("El usuario ya existe")
            else:
                emails.append(email)
                print("El usuario creado exitosamente")

        else:
            print("Email no valido")

    elif opcion == 2:
        email = input("Introduce email para buscar: ").strip()
        if email in emails:
            print("Email encontrado")
        else:
            print("Email no encontrado")


    elif opcion == 3:
        email = input("Introduce email para eliminar: ").strip()
        if email in emails:
            emails.remove(email)
            print("El usuario eliminado exitosamente")
        else:
            print("Email no encontrado")


    elif opcion == 4:
        print("Ver todos")
        if emails:
            print(emails)
        else:
            print("No hay emails")

    elif opcion == 5:
        break