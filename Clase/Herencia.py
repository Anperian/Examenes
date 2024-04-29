class Carro:
    #atributos
    ruedas = 4

    #Constructor: Valores que tendrá la clase en una variable

    def __init__(self, color, aceleración):
        self.color = color
        self.aceleración = aceleración
        self.velocidad = 10

    def acelerar(self):
        self.velocidad = self.velocidad + self.aceleración

    def frena(self):
        frena = self.velocidad - self.aceleración
        if velocidad < 0:
            velocidad = 0
            self.velocidad = velocidad

class CarroVolador(Carro):

    ruedas = 6

    def __init__(self, color, aceleración, volando=False):
        self.color = color
        self.aceleración = aceleración
        self.volando = volando

    def vuela(self):
        self.volando = True

    def aterriza(self):
        self.volando = False

carro_1 = Carro("Rojo", 50)
carro_volador = CarroVolador("Blanco", 30)
print(f"El color del carro volador es {carro_volador.color}")
print(f"La velocidad del carro volador es {carro_volador.velocidad}")
print(f"El estado inicial del carro volador es {carro_volador.volando}")
carro_volador.vuela()
print(f"El estado actual del carro volador es {carro_volador.volando}")