def contacto():
    var1 = input("Ingresa tu nombre: ")
    var2 = input("Ingresa tu apellido: ")
    var3 = int(input("Ingresa tu edad: "))

    with open("agenda.txt", "a") as archivo:
        archivo.write(f"{var1}, {var2}, {var3}\n")

contacto()