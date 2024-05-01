import Modulo14

nombre, apellido = Modulo14.nombre()
seguro = Modulo14.seguro()
edad = Modulo14.edad()

print(f"Tu nombre es {nombre} {apellido}")
if edad:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
print(f"Tu tipo de seguro es {seguro}")