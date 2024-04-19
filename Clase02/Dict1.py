dict = {"Nombre": "Andrés", "Edad": 34, "Salario": 2000, "Edad del empleado": 23}
lista = list(dict.items())
print(type(lista))
dict["DNI"] = "44223355"
print("Salario:", dict["Salario"])
del dict["Edad"]
print(type(lista[0]))
print(type(lista[1]))
print(type(lista[2]))
print(type(lista[3]))