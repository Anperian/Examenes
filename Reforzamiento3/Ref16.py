import Impuesto

nombre = input("Ingresa tu nombre: ")
sueldo = float(input("Ingresa tu sueldo: "))

sueldo = sueldo
nombre = nombre
impuesto = Impuesto.impuesto(sueldo)
saludo = Impuesto.saludo(nombre)

print(saludo)
print("El impuesto que tienes que pagar es de ", round(impuesto,2))
print("Tu sueldo neto será ", round(sueldo - impuesto,2))