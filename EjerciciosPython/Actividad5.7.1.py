from datetime import datetime

class Empleado:

    contador_empleado=0

    def __init__(self,id_empleado: int, nombre: str, edad: int, cargo: str, salario: float, fecha_contratacion: datetime, correo: str,
                 telefono: str, direccion: str, horario: str, contratado: bool =True, fecha_salida: datetime=None):

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

    def despedir(self):
        if self.contratado:
            self.contratado = False
            self.fecha_salida = datetime.now()
            print(f"El empleado {self.nombre} ha sido despedido...")
            Empleado.contador_empleado -= 1

        else:
            print(f"{self.nombre} ya no estaba contratado")

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


    #Buscamos todos los empleados en la clase empleado, comparamos id del empleado para ver si ya existe, sino añadimos un empleado nuevo
    def agregar_empleado(self, empleado: Empleado):
        for empleados in self.empleados:
            if empleados.id_empleado == empleado.id_empleado:
                print("Ya existe el empleado")
                return
        self.empleados.append(empleado)


    #Mismo procedimiento de busqueda de empleado, si es ese exactamente eliminamos empleado con remove(), sino existe mandamos error.
    def eliminar_empleado(self, id_empleado):
        for empleados in self.empleados:
            if empleados.id_empleado == id_empleado:
                self.empleados.remove(empleados)
                return
        print("No existe el empleado")


    def calcular_costo_salario(self):
        total = 0
        for empleados in self.empleados:
            if empleados.contratado:
                total += empleados.salario
        return total


    def listar_empleado(self):
        for empleados in self.empleados:
            print (empleados,"\n")



    def despedir_empleado(self, id_empleado):
        for empleados in self.empleados:
            if empleados.id_empleado == id_empleado:
                empleados.despedir()
                return
            print("No existe el empleado")


    def filtrar_edad_empleado(self, edad_min, edad_max):
        for empleados in self.empleados:
            if empleados.contratado and edad_min <= empleados.edad <= edad_max:
                print (empleados,"\n")



    def filtrar_por_cargo(self, cargo):
        for empleados in self.empleados:
            if empleados.contratado and empleados.cargo.lower() == cargo.lower():
                print (empleados,"\n")


    def filtrar_por_salario(self, salario):
        for empleados in self.empleados:
            if empleados.contratado and empleados.salario >= salario:
                print (empleados,"\n")


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

    empresas = []

    while True:
        print("\n--MENU GESTION DE EMPRESA--")
        print("1. Crear empresa")
        print("2. Listar empresa")
        print("3. Eliminar empresa")
        print("4. Listar empresas con menos de 10 empleados")
        print("5. Listar empresas con mas de 10 empleados")
        print("6. Procesar empleados de una empresa")
        print("7. Salir")

        opcion = input("Opcion : ")

        #Crear empresas
        if opcion == "1":
            nombre = input("Nombre : ")
            direccion = input("Direccion : ")
            industria = input("Industria : ")
            telefono = input("Telefono : ")
            correo = input("Correo : ")

            empresa= Empresa(nombre, direccion, industria, telefono, correo)
            empresas.append(empresa)
            print("Empresa creada")

        #Listar empresas
        elif opcion == "2":
            print("\nLISTAS DE EMPRESAS")
            for empresa in empresas:
                print("-",empresa.nombre)

        #Eliminar empresa
        elif opcion == "3":
            nombreEmpresa = input("Nombre Empresa : ")
            for empresa in empresas:
                if empresa.nombre == nombreEmpresa:
                    empresas.remove(empresa)
                    print("Empresa eliminada")
            else:
                print("No existe el empresa")

        #Listar empresas con menos de 10 empleados
        elif opcion == "4":
            print("Empresas con menos de 10 empleados")
            for empresa in empresas:
                if len(empresa.empleados)<10:
                    print(empresa.nombre)
            else:
                print("No existe empresas con menos de 10 empleados")

        #Listar empresas con 10 o mas de 10 empleados
        elif opcion == "5":
            print("Empresas con menos de 10 empleados")
            for empresa in empresas:
                if len(empresa.empleados) >= 10:
                    print(empresa.nombre)
            else:
                print("No existe empresas con 10 o mas de 10 empleados")

        #Procesar empleados de una empresa
        elif opcion == "6":
            nombre_empresa = input("Empresa : ")
            for empresa in empresas:
                if empresa.nombre == nombre_empresa:
                    menu_empresa(empresa)
                    break
            else:
                print("No existe el empresa")


        elif opcion == "7":
            break



def menu_empresa(empresa):

    while True:
        print(f"\n--- EMPRESA: {empresa.nombre} ---")
        print("1. Agregar empleado")
        print("2. Eliminar empleado")
        print("3. Despedir empleado")
        print("4. Costo salarial")
        print("5. Listar empleados")
        print("6. Filtrar por edad")
        print("7. Filtrar por cargo")
        print("8. Filtrar por salario")
        print("9. Volver")
        opcion = input("Opcion : ")


        if opcion == "1":
            id_empleado = int(input("ID Empleado : "))
            nombre = input("Nombre Empleado : ")
            edad = int(input("Edad Empleado : "))
            cargo = input("Cargo Empleado : ")
            salario = float(input("Salario Empleado : "))
            fecha = datetime.now()
            correo = input("Correo Empleado : ")
            telefono = input("Telefono : ")
            direccion = input("Direccion : ")
            horario = input("Horario Empleado : ")

            nuevo_empleado = Empleado(id_empleado, nombre, edad, cargo,salario,
                                      fecha, correo, telefono, direccion, horario)

            empresa.agregar_empleado(nuevo_empleado)


        elif opcion == "2":
            id_empleado = int(input("ID Empleado : "))
            empresa.eliminar_empleado(id_empleado)

        elif opcion == "3":
            id_empleado = int(input("ID Empleado : "))
            empresa.despedir_empleado(id_empleado)

        elif opcion == "4":
            print("Costo total", empresa.calcular_costo_salario)
        elif opcion == "5":
            empresa.listar_empleados()
        elif opcion == "6":
            edad_minima = int(input("Edad Minima : "))
            edad_maxima = int(input("Edad Maxima : "))
            empresa.filtrar_edad_empleado(edad_minima, edad_maxima)

        elif opcion == "7":
            cargo = int(input("Cargo Empleado : "))
            empresa.filtrar_por_cargo(cargo)

        elif opcion == "8":
            salario = float(input("Salario Empleado : "))
            empresa.filtrar_por_salario(salario)

        elif opcion == "9":
            break

if __name__ == "__main__":
    principal()
