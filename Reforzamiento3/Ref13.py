class Persona:
    def __init__(self):
        self.nombre = input("Ingresa tu nombre: ")
        self.edad = int(input("Ingresa tu edad: "))

class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo = int(input("Ingresa tu sueldo: "))

    def impuesto(self):
        if self.sueldo > 4000:
            impuesto = self.sueldo * 0.10
            print("El impuesto a pagar es:", impuesto)
        else:
            print("No se debe pagar impuesto.")

empleado = Empleado()
print("Nombre:", empleado.nombre)
print("Edad:", empleado.edad)
print("Sueldo:", empleado.sueldo)
empleado.impuesto()