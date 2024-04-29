class Circulo:
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return 3.14 * self.radio ** 2
    def perimetro(self):
        return 2 * 3.14 * self.radio

circulo1 = Circulo(2)
circulo2 = Circulo(3)

print("El área del primer círculo es:", circulo1.area())
print("El perímetro del primer círculo es:", circulo1.perimetro())
print("El área del segundo círculo es:", circulo2.area())
print("El perímetro del segundo círculo es:", circulo2.perimetro())