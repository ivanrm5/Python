from datetime import datetime
from enum import Enum


# =========================================================
# CLASES COCHE (Sin cambios significativos necesarios)
# =========================================================
class Coche:
    contadorcoches = 0

    def __init__(self, color, marca, modelo):
        self._color = color
        self.aceleracion = 0
        self.velocidad = 0
        self.marca = marca
        self.modelo = modelo
        self.matricula = ""
        Coche.contadorcoches += 1

    def get_color(self): return self._color

    def set_color(self, color): self._color = color

    def get_velocidad(self): return self.velocidad

    def set_velocidad(self, velocidad): self.velocidad = velocidad

    def acelerar(self, aceleracion):
        self.rugir()
        self.aceleracion = aceleracion
        self.velocidad += aceleracion

    def frenar(self, aceleracion):
        v = self.velocidad - aceleracion
        self.aceleracion = aceleracion
        if v < 0: v = 0
        self.velocidad = v

    def rugir(self): print("Brrrrrrr")

    def __str__(self):
        return f"Coche(marca={self.marca}, modelo={self.modelo}, color={self._color}, velocidad={self.velocidad})"


class Cochemarchas(Coche):
    def __init__(self, marchas, color, marca, modelo):
        super().__init__(color, marca, modelo)
        self.marchas = marchas
        self.marchaactual = 0
        self.frenomano = True

    def cambiomarcha(self, nueva_marcha):
        if ((self.marchaactual == -1 and nueva_marcha > 0) or (self.marchaactual > 0 and nueva_marcha == -1)):
            if self.velocidad != 0 or self.marchaactual != 0:
                print("ERROR: Debe estar parado y en punto muerto")
                return
        if nueva_marcha >= 5 and self.velocidad < 40:
            print("ERROR: El coche se cala")
            return
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
        return super().__str__() + f", marchas={self.marchas}, marchaactual={self.marchaactual}, frenomano={self.frenomano}"


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
# CLASE VENTA - CORREGIDA
# =========================================================
class Venta:
    contador_ventas = 0

    def __init__(self, coche, propietario, precioventa):
        Venta.contador_ventas += 1
        self.id_venta = Venta.contador_ventas
        self.coche = coche
        self.propietario = propietario
        self.precioventa = precioventa
        self.fechaentrada = datetime.now()
        self.fechaventa = None
        self.estado = "Sin interesado"
        self.documentacionpendiente = ["Permiso Circulacion", "Impuesto Coche", "Ficha Técnica"]
        self.cliente_interesado = None  # Guardaremos el nombre aquí

    def __str__(self):
        return f"ID: {self.id_venta} | Coche: {self.coche.marca} {self.coche.modelo} | Estado: {self.estado} | Precio: {self.precioventa}€"

    def cambiarestado(self, nuevo_estado):
        # Lógica simplificada para el estado
        if nuevo_estado == "Vendido" and len(self.documentacionpendiente) > 0:
            print("Error: Queda documentación pendiente.")
            return
        self.estado = nuevo_estado

    def consultadocumentacionpendiente(self):
        return self.documentacionpendiente

    def incluirInteresado(self, nombre):
        self.cliente_interesado = nombre
        self.estado = "Con interesado"
        print(f"Interesado {nombre} registrado.")

    def registradocumentopendiente(self, documento):
        if documento not in self.documentacionpendiente:
            self.documentacionpendiente.append(documento)
            print("Documento añadido.")
        else:
            print("El documento ya estaba en la lista.")

    def eliminadocumentopendiente(self, documento):
        if documento in self.documentacionpendiente:
            self.documentacionpendiente.remove(documento)
            print(f"Documento '{documento}' eliminado.")
        else:
            print(f"No existe el documento: {documento}")

    def finalizaventa(self):
        if len(self.documentacionpendiente) == 0 and self.cliente_interesado:
            self.estado = "Vendido"
            self.fechaventa = datetime.now()
            print("Venta finalizada con éxito.")
        else:
            print("No se puede finalizar: revise documentación o interesado.")


# =========================================================
# CLASE TIENDA - CORREGIDA
# =========================================================
class Tienda:
    contador_tiendas = 0

    def __init__(self, nif, propietario, nombre, direccion, url, telefono):
        Tienda.contador_tiendas += 1
        self.id_tienda = Tienda.contador_tiendas
        self.nif = nif
        self.propietario = propietario
        self.nombre = nombre
        self.direccion = direccion
        self.url = url
        self.telefono = telefono
        self.listaventas = []

    def __str__(self):
        return f"Tienda: {self.nombre} (NIF: {self.nif}) - Propietario: {self.propietario}"

    def agregarventa(self, venta):
        self.listaventas.append(venta)
        print(f"Venta ID {venta.id_venta} agregada a la tienda.")

    def obtieneventas(self):
        return self.listaventas

    def buscarventa(self, id_venta):
        for v in self.listaventas:
            if v.id_venta == int(id_venta):
                return v
        return None


# =========================================================
# PROGRAMA PRINCIPAL
# =========================================================

def creartienda():
    print("--- REGISTRO DE TIENDA ---")
    nif = input("NIF: ")
    propietario = input("Propietario: ")
    nombre = input("Nombre: ")
    dir = input("Dirección: ")
    url = input("URL: ")
    tel = input("Teléfono: ")
    return Tienda(nif, propietario, nombre, dir, url, tel)


def gestionar_venta(venta):
    while True:
        print(f"\n--- GESTIÓN VENTA ID: {venta.id_venta} ---")
        print("1 - Incluir interesado")
        print("2 - Consultar documentos")
        print("3 - Registrar documento")
        print("4 - Eliminar documento")
        print("5 - Finalizar venta")
        print("0 - Volver")

        op2 = input("Seleccione opción: ")
        if op2 == "1":
            nom = input("Nombre del interesado: ")
            venta.incluirInteresado(nom)
        elif op2 == "2":
            docs = venta.consultadocumentacionpendiente()
            print(f"Pendiente: {docs}" if docs else "Sin documentos pendientes.")
        elif op2 == "3":
            doc = input("Nuevo documento: ")
            venta.registradocumentopendiente(doc)
        elif op2 == "4":
            doc = input("Documento a eliminar: ")
            venta.eliminadocumentopendiente(doc)
        elif op2 == "5":
            venta.finalizaventa()
            if venta.estado == "Vendido": break
        elif op2 == "0":
            break


def principal():

    tienda = creartienda()

    while True:
        print(f"\n========= MENÚ {tienda.nombre.upper()} =========")
        print("1 - Nueva Venta (Coche Manual)")
        print("2 - Mostrar Ventas")
        print("3 - Procesar/Gestionar Venta")
        print("4 - Resumen Total")
        print("0 - Salir")

        opcion = input("Seleccione: ")

        if opcion == "1":
            m = input("Marca: ")
            mod = input("Modelo: ")
            col = input("Color: ")
            p = float(input("Precio: "))
            # Creamos un coche manual por defecto para la práctica
            c = Cochemarchas(6, col, m, mod)
            v = Venta(c, "Tienda", p)
            tienda.agregarventa(v)

        elif opcion == "2":
            ventas = tienda.obtieneventas()
            for v in ventas: print(v)

        elif opcion == "3":
            id_v = input("ID de la venta a procesar: ")
            venta_encontrada = tienda.buscarventa(id_v)
            if venta_encontrada:
                gestionar_venta(venta_encontrada)
            else:
                print("Venta no encontrada.")

        elif opcion == "4":
            ventas = tienda.obtieneventas()
            total = sum(v.precioventa for v in ventas if v.estado == "Vendido")
            print(f"Total recaudado en ventas finalizadas: {total}€")

        elif opcion == "0":
            break


if __name__ == '__main__':
    principal()