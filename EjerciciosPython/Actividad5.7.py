from datetime import datetime

class Empleado:

    contador_empleado=0

    def __init__(self,id_empleado: int, nombre: str, edad: int, cargo: str, salario: float, fecha_contratacion: datetime, correo: str,
                 telefono: str, direccion: str, horario: str, contratado=bool, fecha_salida= datetime):

        self.id_empleado = id_empleado
        self.nombre = nombre
        self.edad = edad
        self.cargo = cargo
        self.salario = salario
        self.fecha_contratacion = fecha_contratacion
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion
        self.horario = horario
        self.contratado = contratado
        self.fecha_salida = fecha_salida

        Empleado.contador_empleado+=1

    def __str__(self):
        return (
            f"id_empleado: {self.id_empleado}\n"
            f"nombre: {self.nombre}\n"
            f"edad: {self.edad}\n"
            f"cargo: {self.cargo}\n"
            f"salario: {self.salario}\n"
            f"fecha contratacion: {self.fecha_contratacion}\n"
            f"correo: {self.correo}\n"
            f"telefono: {self.telefono}\n"
            f"direccion: {self.direccion}\n"
            f"horario: {self.horario}\n"
            f"contratado: {self.contratado}\n"
            f"fecha_salida: {self.fecha_salida}"
        )

    def despedir(self):
        if self.contratado:
            self.contratado = False
            self.fecha_salida = datetime.now()
            print(f"El empleado {self.nombre} ha sido despedido...")
            Empleado.contador_empleado -= 1

        else:
            print(f"{self.nombre} ya no estaba contratado")




class Empresa:

    contador_empresas=0

    def __init__(self, nombre: str , direccion: str, industria: str, telefono: str, correo: str):
        self.nombre = nombre
        self.direccion = direccion
        self.industria = industria
        self.telefono = telefono
        self.correo = correo
        self.empleados = []

        Empresa.contador_empresas+=1


    def agregar_empleado(self, empleado: Empleado):
        for empleado in self.empleados:
            if empleado.id_empleado == empleado.id_empleado:
                print("Ya existe el empleado")
                return
        self.empleados.append(empleado)
    #append

    def eliminar_empleado(self, id_empleado):
        for empleado in self.empleados:
            if empleado.id_empleado == id_empleado:
                self.empleados.remove(empleado)
                return
        print("No existe el empleado")
#remove

    def calcular_costo_salario(self):
        total = 0
        for empleado in self.empleados:
            if empleado.contratado:
                total += empleado.salario


    def listar_empleado(self):
        for empleado in self.empleados:
            print (empleado)


    def __str__(self):
        return (
            f"nombre: {self.nombre}\n"
            f"direccion: {self.direccion}\n"
            f"industria: {self.industria}\n"
            f"telefono: {self.telefono}\n"
            f"correo: {self.correo}\n"
            f"empleados: {len(self.empleados)}\n"
        )


def principal():
    print ("\nCREAR EMPLEADOS\n")

#Crear dos empleados, una empresa. Agregar empleados a la empresa
    empleado1 = Empleado(1, "Juan", 25, "Desarrollador",
                         2000, "20/02/2025", "juan@gmail.com",
                         600000000, "Calle Ibiza 1", "8:00-14:00")


    empleado2 = Empleado(2, "Marta", 26, "Informatico",
                         4000, "21/02/2025", "marta@gmail.com",
                         600000001, "Calle Ibiza 12", "8:30-15:00")


    empresa1 = Empresa("Ejemplo", "Calle Lugo", "Tecnologica", "910000000", "ejemplo@gmail.com")


    empresa1.agregar_empleado(empleado1)
    empresa1.agregar_empleado(empleado2)


    #empresa1.eliminar_empleado(1)
    #empresa1.eliminar_empleado(2)



#Lista de empleados, costo total de salarios
    print("Lista de empleados:\n")
    print(empleado1)



#Añadir un nuevo empleado y mostrar de nuevo la lista y el costo




#Eliminar un empleado y mostar de nuevo



if __name__ == "__main__":
    principal()