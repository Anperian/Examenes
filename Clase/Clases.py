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
        velocidad = self.velocidad - self.aceleración
        if velocidad < 0:
            velocidad = 0
            self.velocidad = velocidad

carro_1 = Carro("negro", 50)
print(f"La velocidad es {carro_1.velocidad}")
carro_1.acelerar()
carro_1.acelerar()
print(f"La velocidad actual es {carro_1.velocidad}")

#print(f"El color del carro es {carro_1.color}")
#print(f"La aceleración del carro es {carro_1.aceleración}")
#print(f"La cantidad de ruedas del carro es {carro_1.ruedas}")
#print("*****")
#carro_2 = Carro("azul", 90)
#print(f"El color del carro es {carro_2.color}")
#print(f"La aceleración del carro es {carro_2.aceleración}")
#print(f"La cantidad de ruedas del carro es {carro_2.ruedas}")