class Persona:
    def __init__(self, nombre, edad, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo
    def datos(self):
        print(self.nombre)
        print(self.edad)
        print(self.sueldo)
    def mayor(self):
        if self.edad > 17:
            print(f"{self.nombre} es mayor de edad")
        else:
            print(f"{self.nombre} no es mayor de edad")
    def bono(self):
        bono = int(self.sueldo * 0.20)
        print(f"{self.nombre} recibe bonificación de {bono}.")

var1 = Persona("Renato", 27, 4000)
var2 = Persona("Santiago", 14, 800)

var1.datos()
var1.mayor()
var1.bono()
print("****")
var2.datos()
var2.mayor()
var2.bono()