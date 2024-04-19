dict = {"Departamento 1": "Tumbes", "Departamento 2": "Lambayeque", "Departamento 3": "Chiclayo", "Departamento 4": "Cajamarca", "Departamento 5": "Lima", "Departamento 6": "Arequipa"}
print(dict)
del dict["Departamento 1"]
print(dict)
if "Tumbes" not in dict:
    print("Tumbes no está en la lista")
else:
    print("Tumbes está en la lista")

dict["Carrera"] = "Psicología"
print(dict)
print(type(dict))