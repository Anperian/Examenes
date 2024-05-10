class Persona:
    def __init__(self):
        self._saldo = 0

    def saldo(self):
        return self._saldo

    def transferencia(self, empleado, monto):
        if self._saldo > monto:
            self._saldo = self._saldo - monto
            empleado._saldo = empleado._saldo + monto
            print(f"S/. {monto} transferidos a {empleado.nombre}")
        else:
            print("Saldo insuficiente")

class Empleado(Persona):
    def __init__(self, nombre, edad, saldo=0):
        super().__init__()
        self.nombre = nombre
        self.edad = edad
        self._saldo = saldo

var1 = Empleado("Ricardo", 20, 15)
var2 = Empleado("Santiago", 20, 30)

print(f"Saldo de {var1.nombre}: S/. {var1.saldo()}")
print(f"Saldo de {var2.nombre}: S/. {var2.saldo()}")

var1.transferencia(var2, 10)

print(f"Saldo de {var1.nombre}: S/. {var1.saldo()}")
print(f"Saldo de {var2.nombre}: S/. {var2.saldo()}")