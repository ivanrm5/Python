#Esta clase define el estado y comportamiento de un coche
class Coche:

    #Atributo de clase. Atributo estático
    contadorcoches = 0


# Este método es el constructor de la clase. Solo puede haber 1
    def __init__(self, color, marca, modelo):
        #Todos estos son atributos de la clase.
        self.color = color
        self.aceleracion = 0
        self.velocidad = 0
        self.marca = marca
        self.modelo = modelo
        self.matricula = ""

        Coche.contadorcoches += 1

#Método para acelerar
    def acelerar (self,aceleracion):
        self.rugir()
        self.aceleracion=aceleracion
        self.velocidad = self.velocidad + aceleracion

#Método para frenar
    def frenar (self,aceleracion):
        v = self.velocidad - aceleracion
        self.aceleracion=aceleracion

        if v < 0:
            v=0

        self.velocidad=v


    def rugir(self):
        if self.velocidad == 0:
            print("brrr...")
        elif 0 < self.velocidad <= 40:
            print("BRUM BRUM (motor suave)")
        elif 40 < self.velocidad <= 100:
            print("BRUAAAAAM (motor fuerte)")
        else:
            print("BRUUUUUUUMMMMM!!! (motor a tope)")


# Puede haber otra clase en el mismo fichero

#La clase hoja, lleva entre paréntesis el nombre de la clase padre.
#cochemarchas lleva el nombre de la clase coche en su declaración
class Cochemarchas(Coche):

    def __init__(self,marchas,color, marca, modelo):
        super().__init__(color, marca, modelo)
        #marchas indica el número de marchas hacia delante
        self.marchas=marchas
        self.marchaactual=0 #0 significa que está en punto muerto # -1 significa que está en marcha atrás
        self.frenomano=True


    def cambiomarcha(self, marchaactual):

        if marchaactual < -1 or marchaactual > self.marchas:
            print("Marcha no válida.")
            return

        #marcha atrás si el coche se esta moviendo
        if marchaactual == -1 and self.velocidad > 0:
            print("No se puede poner marcha atrás con el coche en movimiento.")
            return

        #positiva a marcha atrás
        if marchaactual == -1 and self.marchaactual > 0:
            print("Debe poner punto muerto antes de usar marcha atrás.")
            return

        #Evitar marchas largas con poca velocidad
        if marchaactual > 1:
            velocidad_minima = marchaactual * 10
            if self.velocidad < velocidad_minima:
                print(f"Velocidad insuficiente para la marcha {marchaactual}: el coche se calaría.")
                return

        if marchaactual in (1, 2) and self.velocidad > marchaactual * 30:
            print("Aviso: El coche está revolucionado para esta marcha.")

        # Si todo va bien → actualizar marcha
        self.marchaactual = marchaactual
        print(f"Cambiada a marcha {self.marchaactual}.")

    def ponerpuntomuerto(self):
        self.marchaactual=0
        print("El coche esta en punto muerto")


    def ponerfrenomano(self):
        if self.velocidad > 0:
            print("El coche esta en marcha no poner el freno de mano")
        else:
            self.frenomano=True
            print("Freno de mano puesto")

    def quitarfrenomano(self):
        self.frenomano=False
        print("Freno de mano quitado")




class CocheAutomatico(Coche):
    def __init__(self, color, marca, modelo):
        super().__init__(color,marca,modelo)

        #MODO DE UN COCHE AUTOMÁTICO (P, R, N, D)
        self.modo="P"


    def rugir(self):
        if self.modo == "P":
            print("(motor en parking)")
        elif self.modo == "R":
            print("PEE PEE (retrocediendo)")
        elif self.modo == "N":
            print("(motor en neutro)")
        elif self.modo == "D":
            if self.velocidad == 0:
                print("brrr... (listo para avanzar)")
            elif 0 < self.velocidad <= 40:
                print("BRUM BRUM (avanzando suave)")
            elif 40 < self.velocidad <= 100:
                print("BRUAAAAM (acelerando)")
            else:
                print("BRUUUMMMMMM!!! (alta velocidad)")
        else:
            print("El motor hace un ruido extraño...")




def principal():

    print("\n--- PRUEBAS DE COCHE CON MARCHAS ---\n")

    c4 = Cochemarchas(6, "blanco", "Toyota", "Auris")

    print(f"Marcha inicial: {c4.marchaactual}")
    print(f"Velocidad inicial: {c4.velocidad}")
    print()

    # Quitar freno de mano
    c4.quitarfrenomano()

    # Acelerar a 20 km/h
    c4.acelerar(20)
    print("Velocidad:", c4.velocidad)
    c4.rugir()

    # Intentar poner 3ª con poca velocidad
    print("\nIntentando poner 3ª marcha a 20 km/h...")
    c4.cambiomarcha(3)

    # Poner 2ª correctamente
    print("\nPoniendo 2ª marcha...")
    c4.cambiomarcha(2)

    # Acelerar fuerte
    print("\nAcelerando +60 km/h...")
    c4.acelerar(60)
    print("Velocidad:", c4.velocidad)
    c4.rugir()

    # Poner 1ª marcha con velocidad muy alta → aviso
    print("\nIntentando poner 1ª marcha a alta velocidad...")
    c4.cambiomarcha(1)

    # Frenar a 0
    print("\nFrenando a 0 km/h...")
    c4.frenar(200)
    print("Velocidad:", c4.velocidad)
    c4.rugir()

    # Poner punto muerto
    print("\nPoniendo punto muerto...")
    c4.ponerpuntomuerto()

    # Poner marcha atrás correctamente
    print("\nPoniendo marcha atrás...")
    c4.cambiomarcha(-1)

    # Poner freno de mano
    print("\nPoniendo freno de mano...")
    c4.ponerfrenomano()

    print("\nTotal de coches creados:", Coche.contadorcoches)



    print("\n--- PRUEBAS DE COCHE AUTOMÁTICO ---\n")

    c1 = CocheAutomatico("rojo", "Tesla", "Model S")

    print("Modo inicial:", c1.modo)
    c1.rugir()

    # Cambiar modo
    print("\nCambiando a modo D...")
    c1.modo = "D"
    c1.rugir()

    print("\nAcelerando 30 km/h...")
    c1.acelerar(30)
    c1.rugir()

    print("\nAcelerando +50 km/h...")
    c1.acelerar(50)
    c1.rugir()

    print("\nPoniendo modo Neutro...")
    c1.modo = "N"
    c1.rugir()

    print("\nPoniendo modo R (Marcha atrás)...")
    c1.modo = "R"
    c1.velocidad = 5
    c1.rugir()

    print("\nPoniendo modo Parking...")
    c1.velocidad = 0
    c1.modo = "P"
    c1.rugir()

    print("\nTotal coches creados:", Coche.contadorcoches)




#Punto de entrada a la ejecución del programa en Python
if __name__ == '__main__':

    principal()