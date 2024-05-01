def nombre():
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    return nombre, apellido
def seguro():
    seguro = input("Ingresa tu tipo de seguro: ")
    return seguro
def edad():
    edad = int(input("Ingresa tu edad: "))
    if edad >= 18:
        return True
    else:
        return False