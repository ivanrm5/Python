class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre}")

    def __str__(self):
        return f"{self.nombre} ({self.edad} años)"

persona1 = Persona("Juan", 30)
persona1.presentarse()
print(persona1)