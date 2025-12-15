from datetime import datetime

class Empleado:

    contador_empleado=0

    def __init__(self,id_empleado, nombre, edad, cargo, salario, fecha_contratacion, correo,
                 telefono, direccion, horario, contratado=True, fecha_salida= None):

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
            f"fecha_salida: {self.fecha_salida}\n"
        )

    def despedir(self):
        if self.contratado:
            self.contratado = False
            self.fecha_salida = datetime.now()
            print("El empleado {self.nombre} ha sido despedido...}")
        else:
            print("Ya no estaba contratado")


class Empresa:
    def __init__(self, nombre, direccion, industria, telefono, correo, empleados):
        self.nombre = nombre
        self.direccion = direccion
        self.industria = industria
        self.telefono = telefono
        self.correo = correo
        self.empleados = empleados


    def __str__(self):
        pass

    def agregar_empleado(self):
        pass

    def eliminar_empleado(self):
        pass

    def calcular_costo_salario(self):
        pass

    def listar_empleado(self):
        pass

def principal():
    pass








if __name__ == "__main__":
    principal()