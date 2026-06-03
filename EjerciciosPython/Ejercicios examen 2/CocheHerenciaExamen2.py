from datetime import datetime
from enum import Enum


# =========================================================
# CLASE COCHE
# =========================================================
class Coche:

    # Atributo de clase
    contadorcoches = 0

    def __init__(self, color, marca, modelo):
        self._color = color
        self.aceleracion = 0
        self.velocidad = 0

        self.marca = marca
        self.modelo = modelo
        self.matricula = ""

        Coche.contadorcoches += 1

    # ==========================
    # GETTERS Y SETTERS
    # ==========================
    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def get_velocidad(self):
        return self.velocidad

    def set_velocidad(self, velocidad):
        self.velocidad = velocidad

    # ==========================
    # MÉTODOS
    # ==========================
    def acelerar(self, aceleracion):
        self.rugir()
        self.aceleracion = aceleracion
        self.velocidad += aceleracion

    def frenar(self, aceleracion):
        v = self.velocidad - aceleracion
        self.aceleracion = aceleracion

        if v < 0:
            v = 0

        self.velocidad = v

    def rugir(self):
        print("Brrrrrrr")

    def __str__(self):
        return (
            f"Coche(marca={self.marca}, modelo={self.modelo}, "
            f"color={self._color}, velocidad={self.velocidad})"
        )


# =========================================================
# CLASE COCHEMARCHAS
# =========================================================
class Cochemarchas(Coche):

    def __init__(self, marchas, color, marca, modelo):
        super().__init__(color, marca, modelo)

        self.marchas = marchas
        self.marchaactual = 0
        self.frenomano = True

    def cambiomarcha(self, nueva_marcha):

        # Cambio entre marcha atrás y positiva
        if ((self.marchaactual == -1 and nueva_marcha > 0) or
                (self.marchaactual > 0 and nueva_marcha == -1)):

            if self.velocidad != 0 or self.marchaactual != 0:
                print("ERROR: Debe estar parado y en punto muerto")
                return

        # Marchas largas a poca velocidad
        if nueva_marcha >= 5 and self.velocidad < 40:
            print("ERROR: El coche se cala")
            return

        # Marchas cortas a mucha velocidad
        if nueva_marcha <= 2 and self.velocidad > 80:
            print("AVISO: El coche está revolucionado")

        self.marchaactual = nueva_marcha
        print(f"Marcha cambiada a {self.marchaactual}")

    def ponerpuntomuerto(self):
        self.marchaactual = 0
        print("El coche está en punto muerto")

    def ponerfrenomano(self):

        if self.velocidad > 0:
            print("ERROR: No puede ponerse el freno de mano en movimiento")
            return

        self.frenomano = True
        print("Freno de mano activado")

    def quitarfrenomano(self):
        self.frenomano = False
        print("Freno de mano desactivado")

    def rugir(self):
        print("BRRRRRMMMMM")

    def __str__(self):
        return (
            super().__str__() +
            f", marchas={self.marchas}, marchaactual={self.marchaactual}, "
            f"frenomano={self.frenomano}"
        )


# =========================================================
# CLASE COCHEAUTOMATICO
# =========================================================
class Cocheautomatico(Coche):

    def __init__(self, color, marca, modelo, modo="P"):
        super().__init__(color, marca, modelo)

        self.modo = modo

    def cambiar_modo(self, modo):

        modos_validos = ["P", "R", "N", "D"]

        if modo in modos_validos:
            self.modo = modo
            print(f"Modo cambiado a {modo}")
        else:
            print("Modo no válido")

    def rugir(self):
        print("Vruuuumm automático")

    def __str__(self):
        return super().__str__() + f", modo={self.modo}"



# =========================================================
# CLASE VENTA
# =========================================================

class Venta:

    #TO-DO Constructor y Atributo Estático
    def __init__(self, coche, propietario, precioventa):
        pass

    # ==================================
    # MÉTODOS DE LA CLASE VENTA
    # ==================================

    #TO-DO Método str
    def __str__(self):
        pass


    #TO-DO Método cambiarestado

    #TO-DO Método consultadocumentacionpendiente

    #TO-DO Método incluirInteresado

    #TO-DO Método registradocumentopendiente

    #TO-DO Método eliminadocumentopendiente

    #TO-DO Método finalizaventa


# =========================================================
# CLASE TIENDA
# =========================================================
class Tienda:

    #TO-DO Constructor
    def __init__(self, nif, propietario, nombre, direccion, url, telefono):
        pass

    # TO-DO Método str
    def __str__(self):
        pass

    #TO-DO Método agregarventa

    #TO-DO Método obtieneventas

    #TO-DO Método buscarventa





# =========================================================
# AQUÍ ACABAN LAS CLASES Y EMPIEZA EL CÓDIGO DEL PROGRAMA PRINCIPAL
# =========================================================



#TO-DO Programar la función que crea la tienda
def creartienda():
    pass



def gestionar_venta(venta):
    while True:

        print("\n--- SUBMENÚ VENTAS ---")
        print("1 - Incluir interesado")
        print("2 - Consultar documentos")
        print("3 - Registrar documento")
        print("4 - Eliminar documento")
        print("5 - Finalizar venta")
        print("0 - Volver")

        op2 = input("Seleccione opción: ")

        if op2 == "1":
            # TO-DO - Implementa la opción 1 - Incluir interesado
            pass

        elif op2 == "2":
            # TO-DO - Implementa la opción 2 - Consultar documentos
            pass

        elif op2 == "3":
            # TO-DO - Implementa la opción 3 - Registrar documento
            pass

        elif op2 == "4":
            # TO-DO - Implementa la opción 4 - Eliminar documento
            pass

        elif op2 == "5":
            # TO-DO - Implementa la opción 5 - Finalizar venta
            pass

        elif op2 == "0":
            break


# =========================================================
# NO ELIMINAR NI MODIFICAR - FUNCIÓN PRINCIPAL
# =========================================================
def principal():

    tienda = creartienda()

    while True:

        print("\n========= MENÚ TIENDA=========")
        print("1 - Nueva Venta")
        print("2 - Mostrar Ventas")
        print("3 - Procesar Venta")
        print("4 - Resumen Ventas")
        print("0 - Salir")

        opcion = input("Seleccione opción: ")

        # ====================================
        # NUEVA VENTA
        # ====================================
        if opcion == "1":
            #TO-DO - Implementa la opción 1 - Nueva Venta
            pass

        # ====================================
        # MOSTRAR VENTAS
        # ====================================
        elif opcion == "2":

            #TO-DO - Implementa la opción 2 - Mostrar Ventas
            pass

        # ====================================
        # PROCESAR VENTAS
        # ====================================
        elif opcion == "3":

            #TO-DO - Implementa la opción 3 - Procesar Venta
            pass


        # ====================================
        # RESUMEN VENTAS
        # ====================================
        elif opcion == "4":
            #TO-DO - Implementa la opción 4 - Resumen Ventas
            pass

        # ====================================
        # SALIR
        # ====================================
        elif opcion == "0":
            print("Fin del programa")
            break

        else:
            print("Opción no válida")


# =========================================================
# PUNTO DE ENTRADA
# =========================================================
if __name__ == '__main__':
    principal()
