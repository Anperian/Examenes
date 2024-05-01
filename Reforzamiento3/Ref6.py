class Numeros:
    def __init__(self):
        self.numero = int(input("Ingresa un número: "))
    def cubo(self):
        return self.numero ** 3
    def cuadrado(self):
        cubo = self.cubo()
        return cubo ** 2

Num = Numeros()
cubo = Num.cubo()
cuadrado = Num.cuadrado()

print(f"El cubo del número {Num.numero} es {cubo} y su cuadrado es {cuadrado}")