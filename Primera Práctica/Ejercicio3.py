nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = int(input("Ingresa tu edad: "))
dni = input("Ingresa tu DNI: ")

dict = {
    "Nombre": nombre,
    "Apellido": apellido,
    "Edad": edad,
    "DNI": dni
}

dict["Edad"] += 10
print(dict["Nombre"], dict["Apellido"], dict["Edad"], dict["DNI"])

profesion = input("¡Olvidé preguntar tu profesión!: ")
dict["Profesión"] = profesion

del dict["DNI"]
print(dict)