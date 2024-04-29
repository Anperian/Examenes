var1 = "Hola Pythonista, seguimos adelante"
class Reversion:
    def __init__(self):
        pass
    def reversion(self, var1):
        oracion = var1.split()
        oracion2 = reversed(oracion)
        oracion3 = " ".join(oracion2)
        return oracion3

reversor = Reversion()
oracion3 = reversor.reversion(var1)

print(var1)
print(oracion3)