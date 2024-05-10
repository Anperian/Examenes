import funciones


def Ejercicio2():
    archivo = "notas.txt"
    with open(archivo, "a"):
        pass
    lista1 = funciones.tamaño(archivo)
    funciones.cuadrados(lista1, archivo)


if __name__ == "__main__":
    Ejercicio2()
