"""
Crear clase base Vehiculo y subclases Coche y Moto
"""

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

        def descripcion(self):
            return f"{self.marca} {self.modelo}"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def __str__(self):
        return f"Coche: {self.descripcion()} - {self.puertas}"

class Moto(Vehiculo):
    def __init__(self, marca, modelo, tiene_sidecar):
        super().__init__(marca, modelo)
        self.tiene_sidecar = tiene_sidecar

    def __str__(self):
        sidecar= "con" if self.tiene_sidecar else "no tiene"
        return f"Moto: {self.descripcion()} - {sidecar} sidecar"

# Uso
coche = Coche("Toyota", "Corolla", 4)
moto = Moto("Honda", "CB500", False)

print(coche)
print(moto)
print(isinstance(coche, Vehiculo))  # True
print(isinstance(moto, Vehiculo))  # True