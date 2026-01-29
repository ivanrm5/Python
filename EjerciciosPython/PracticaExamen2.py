class Alumno:
    def __init__(self, id_alumno: int, nombre: str, edad:int, email:str, activo:bool=True):
        self.id_alumno = id_alumno
        self.nombre=nombre
        self.edad=edad
        self.email=email
        self.activo=activo

    #Mostrar todos los datos
    def __str__(self):
        return (
            f"id_alumno: {self.id_alumno}\n"
            f"nombre: {self.nombre}\n"
            f"edad: {self.edad}\n"
            f"email: {self.email}\n"
            f"activo: {self.activo}\n"
        )

    #metodos de dar de baja -cambiar activo a false

    def dar_baja(self):
        self.activo=False


class Curso:
    def __init__(self, codigo:str, nombre:str, duracion:int):
        self.codigo=codigo
        self.nombre=nombre
        self.duracion=duracion
        self.alumnos=[]

    def __str__(self):
        return (
            f"codigo: {self.codigo}\n"
            f"nombre: {self.nombre}\n"
            f"duracion: {self.duracion}\n"
        )

    #Agregar alumno por su nombre
    def agregar_alumno(self, alumno:Alumno):
        for a in self.alumnos:
            if a.id_alumno == alumno.id_alumno:
                print("El alumno ya existe")
                return
        self.alumnos.append(alumno)


    #Eliminar alumno por id
    def eliminar_alumno(self, id_alumno):
        for alumno in self.alumnos:
            if alumno.id_alumno == id_alumno:
                self.alumnos.remove(alumno)
                return
        print("El alumno no existe")


    #Dar de baja alumno por id
    def dar_de_baja(self, id_alumno):
        for alumno in self.alumnos:
            if alumno.id_alumno == id_alumno:
                alumno.dar_baja(id_alumno)
                return
        print("El alumno no existe")


    #Listar alumnos solo mostrar id y nombre
    def listar_alumnos(self):
        for alumno in self.alumnos:
            print(alumno.id_alumno,"- nombre:",alumno.nombre)


    #Filtrar alumnos por edad, minima y maxima
    def filtrar_edad_alumno(self, min, max):
        for alumno in self.alumnos:
            if alumno.edad >= min and alumno.edad <= max:



    #porcentaje de activos




