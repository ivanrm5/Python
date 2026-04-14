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

#Método para rugir
    def rugir(self):
        print ("Brrrrrrr")


# Puede haber otra clase en el mismo fichero

#La clase hoja, lleva entre paréntesis el nombre de la clase padre.
#cochemarchas lleva el nombre de la clase coche en su declaración
class Cochemarchas(Coche):

    def __init__(self,marchas,color, marca, modelo):
        super().__init__(color, marca, modelo)
        #marchas indica el número de marchas hacia delante
        self.marchas=marchas

        # 0 significa que está en punto muerto
        # -1 significa que está en marcha atrás
        self.marchaactual=0

        self.frenomano=True


    def cambiomarcha(self, marchaactual):
        pass

    def ponerpuntomuerto(self):
        pass

    def ponerfrenomano(self):
        pass

    def quitarfrenomano(self):
        pass


def principal():

    #LLamada al constructor
    c1 = Coche('rojo', 'Peugeot', '307')

    #Mostramos el valor de un atributo
    print("Color de c1: " + c1.color)

    # Mostramos el valor del atributo de clase
    print("El número de coches actual es: " + str(c1.contadorcoches))

    #Imprimimos la clase. No tiene definido el método de impresión, __str__????
    print(str(c1))

    # LLamada al constructor
    c2 = Coche('azul', 'Ford', 'Fiesta')

    print("Color de c2: " + c2.color)

    print("El número de coches actual es: " + str(c2.contadorcoches))

    #Imprimimos el valor del atributo de clase, sin hacer uso de una instancia, sino del nombre de la clase
    print("El número de coches actual es: " + str(Coche.contadorcoches))

    #LLamadas a métodos
    c1.acelerar(20)

    print("Velocidad de c1: " + str(c1.velocidad))

    c1.acelerar(30)

    print("Velocidad de c1: " + str(c1.velocidad))

    #Otra forma de llamar a los métodos
    #Se utiliza el método como una función de la clase, y se le pasa un objto y los atributos
    Coche.acelerar(c1, 60)

    print("Velocidad de c1: " +str(c1.velocidad))

    c2.acelerar(100)

    print("Velocidad de c2: " + str(c2.velocidad))

    Coche.frenar(c2,20)

    print("Velocidad de c2: " + str(c2.velocidad))

    c3=Cochemarchas(6,'azul', 'Wolkswagen', 'Passat cc')

    print("El número de marchas de c3 es: " + str(c3.marchas))

    print(type(c1))
    print(type(c2))
    print(type(c3))

    print("c1 es instancia de Coche?: " + str(isinstance(c1,Coche)))
    print("c1 es instancia de Cochemarchas?: " + str(isinstance(c1, Cochemarchas)))

    print("c3 es instancia de Coche?: " + str(isinstance(c3, Coche)))
    print("c3 es instancia de Cochemarchas?: " + str(isinstance(c3, Cochemarchas)))

    print("Clase Coche es subclase de Cochemarchas: " + str(issubclass(Coche,Cochemarchas)))

    print("Clase Cochemarchas es subclase de Coche: " + str(issubclass(Cochemarchas,Coche)))

    
#Punto de entrada a la ejecución del programa en Python
if __name__ == '__main__':

    principal()