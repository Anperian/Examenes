def suma():
    try:
        suma = 80 + "Hola Pythonista"
        return suma
    except TypeError:
        print("Error: No se puede sumar números con cadenas")


suma()
