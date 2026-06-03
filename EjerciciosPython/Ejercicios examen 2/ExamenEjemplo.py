class Mascota:
    def __init__(self, nombre, edad, especie, salud):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
        self.salud = salud

    def hacer_sonido(self):
        print("Sonido de animal")


    def __str__(self):
        return f"{self.nombre}, {self.edad}, {self.especie}, {self.salud}"


class Perro(Mascota):
    def __init__(self, raza, nombre, edad, especie, salud):
        super().__init__(nombre, edad, especie, salud)

        self.raza = raza
        self.necesita_paseo = True

    def hacer_sonido(self):
        print("GUAU, GUAU")

class Gato(Mascota):
    def __init__(self, nombre, edad, especie, salud):
        super().__init__(nombre, edad, especie, salud)
        self.es_casero = True

    def hacer_sonido(self):
        print("MIAU, MIAU")

