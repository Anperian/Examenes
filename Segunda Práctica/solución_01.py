from datetime import datetime
class Persona:
    def __init__(self):
        self.nombre = ""
        self.edad = 0
        self.nacionalidad = "peruana"

    def datos(self):
        self.nombre = input("Ingresa tu nombre: ")
        while True:
            try:
                self.edad = int(input("Ingresa tu edad: "))
                break
            except ValueError:
                print("¡Tu edad en enteros!")

    def cumple(self):
        self.edad = self.edad + 1

    def tiempo(self):
        ahora = datetime.now()
        fecha = ahora.strftime("%d-%m-%Y %H:%M")
        return fecha

var1 = Persona()
var1.datos()
print(f"Eres {var1.nombre} ({var1.edad} años) de nacionalidad {var1.nacionalidad}")
var1.cumple()
print(f"Hoy fue tu cumpleaños. Ahora tienes {var1.edad} años")
print("Fecha de registro:", var1.tiempo())
print("***")
var2 = Persona()
var2.datos()
print(f"Eres {var2.nombre} ({var2.edad} años) de nacionalidad {var2.nacionalidad}")
var2.cumple()
print(f"Hoy fue tu cumpleaños. Ahora tienes {var2.edad} años")
print("Fecha de registro:", var2.tiempo())