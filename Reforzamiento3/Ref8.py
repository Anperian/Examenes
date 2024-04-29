class Sujeto:
    def __init__(self):
        self.data = {}
    def datos(self):
        nombre = input("Ingresa tu nombre: ")
        apellido = input("Ingresa tu apellido: ")
        self.data["nombre"] = nombre
        self.data["apellido"] = apellido
    def edad(self):
        edad = input("Ingresa tu edad: ")
        self.data["edad"] = edad
    def total(self):
        nombre = self.data["nombre"]
        apellido = self.data["apellido"]
        edad = self.data["edad"]
        print(f"Eres {nombre} {apellido} de {edad} años")

persona = Sujeto()
persona.datos()
persona.edad()
persona.total()