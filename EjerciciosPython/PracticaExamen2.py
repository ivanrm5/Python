class Alumno:
    def __init__(self, id_alumno: int, nombre: str, edad:int, email:str, activo:bool=True):
        self.id_alumno = id_alumno
        self.nombre=nombre
        self.edad=edad
        self.email=email
        self.activo=activo

    #metodos de dar de baja -cambiar activo a false
    def dar_baja(self):
        self.activo=False


    def __str__(self):
        return (
            f"id_alumno: {self.id_alumno}\n"
            f"nombre: {self.nombre}\n"
            f"edad: {self.edad}\n"
            f"email: {self.email}\n"
            f"activo: {self.activo}\n"
        )
    #Mostrar todos los datos


class Curso:
    def __init__(self, codigo:str, nombre:str, duracion:int):
        self.codigo=codigo
        self.nombre=nombre
        self.duracion=duracion
        self.alumnos=[]

    #Agregar alumno por su nombre
    def agregar_alumno(self, alumno:Alumno):
        for a in self.alumnos:
            if a.id_alumno == alumno.id_alumno:
                print("El alumno ya existe")
                return
        self.alumnos.append(alumno)
        print("Alumno creado correctamente")

    #Eliminar alumno por id
    def eliminar_alumno(self, id_alumno):
        for a in self.alumnos:
            if a.id_alumno == id_alumno:
                self.alumnos.remove(a)
                print("El alumno eliminado correctamente")
                return
        print("Alumno no encontrado")


    #Dar de baja alumno por id
    def dar_de_baja(self, id_alumno):
        for a in self.alumnos:
            if a.id_alumno == id_alumno:
                a.dar_baja()
                return
        print("Alumno no encontrado")


    #Listar alumnos solo mostrar id y nombre
    def listar_alumnos(self):
        for a in self.alumnos:
            estado = "Activo" if a.activo else "Inactivo"
            print(f"{a.id_alumno} - {a.nombre} ({estado})")


    # #Filtrar alumnos por edad, minima y maxima
    def filtrar_edad_alumno(self, min, max):
        for alumno in self.alumnos:
            if alumno.activo and min <= alumno.edad <= max:
                print(alumno.nombre,"\n")
                return



    # porcentaje de activos
    def porcentaje_activos(self):
        if len(self.alumnos) == 0:
            return 0

        activos=0
        for alumno in self.alumnos:
            if alumno.activo:
                activos += 1
        return (activos/len(self.alumnos)) * 100



    def __str__(self):
        return (
            f"codigo: {self.codigo}\n"
            f"nombre: {self.nombre}\n"
            f"duracion: {self.duracion}\n"
        )


def principal():

    cursos=[]

    while True:
        print(f"\nMENU PRINCIPAL")
        print("1. Crear curso")
        print("2. Listar cursos")
        print("3. Gestionar curso")
        print("4. Salir")

        opcion=int(input("Opcion : "))

        if opcion == 1:
            codigo=input("Codigo del curso: ")
            nombre=input("Nombre del curso: ")
            duracion=int(input("Duracion del curso: "))

            cursos.append(Curso(codigo, nombre, duracion))

            print("Curso creado con exito")



        elif opcion == 2:
            if len(cursos) == 0:
                print("No hay cursos")
            else:
                print("LISTA DE CURSOS")
                for curso in cursos:
                    print("-",curso.codigo,"-",curso.nombre)


        elif opcion == 3:
            print("Curso que quieres gestionar")

            if len(cursos) == 0:
                print("No hay cursos")

            else:
                nombre_curso= input("Nombre: ")

                for curso in cursos:
                    if curso.nombre == nombre_curso:
                        menu_alumnos(curso)
                        break
                else:
                    print("El curso no existe")


        elif opcion == 4:
            break



def menu_alumnos(curso):

    while True:
        print(f"CURSO: {curso.nombre}")
        print("1. Agregar alumno")
        print("2. Eliminar alumno")
        print("3. Dar de baja a alumno")
        print("4. Listar alumnos")
        print("5. Filtrar edad alumno")
        print("6. Mostrar porcentaje activos")
        print("7. Salir")

        opcion=int(input("Opcion : "))

        if opcion == 1:
            id_alumno=int(input("ID Alumno: "))
            nombre=input("Nombre del alumno: ")
            edad=int(input("Edad: "))
            email=input("Email: ")

            nuevo_alumno=Alumno(id_alumno, nombre, edad, email)
            curso.agregar_alumno(nuevo_alumno)

        elif opcion == 2:
            if len(curso.alumnos) == 0:
                print("No hay alumnos para eliminar")
            else:
                id_alumno=int(input("ID Alumno: "))
                curso.eliminar_alumno(id_alumno)
                print("Alumno eliminado con exito")


        elif opcion == 3:
            if len(curso.alumnos) == 0:
                print("No hay alumnos para dar de baja")
            else:
                id_alumno=int(input("ID Alumno: "))
                curso.dar_de_baja(id_alumno)

        elif opcion == 4:
            if len(curso.alumnos) == 0:
                print("No hay alumnos")
            else:
                print("Lista de alumnos")
                curso.listar_alumnos()

        elif opcion == 5:
            edad_minima=int(input("Edad minima: "))
            edad_maxima=int(input("Edad maxima: "))

            curso.filtrar_edad_alumno(edad_minima, edad_maxima)

        elif opcion == 6:
            print("Mostrar porcentaje activos")
            curso.porcentaje_activos()


        elif opcion == 7:
            break



if __name__ == "__main__":
    principal()






