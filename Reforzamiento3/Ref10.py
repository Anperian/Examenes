class Alumno:
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota
    def registro(self):
            print("Nombre:", self.nombre)
            print("Edad:", self.edad)
            print("Nota:", self.nota)
    def resultado(self):
        if self.nota > 10:
            print(f"El alumno {self.nombre} ha aprobado con una nota de {self.nota}.")
        else:
            print(f"El alumno {self.nombre} ha desaprobado con una nota de {self.nota}.")

alumno1 = Alumno("Renato", 17, 11)
alumno2 = Alumno("Santiago",14, 12)
alumno3 = Alumno("Arturo",15, 10)

alumno1.resultado()
alumno2.resultado()
alumno3.resultado()