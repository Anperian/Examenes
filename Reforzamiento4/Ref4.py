def mensaje():
    try:
        string = "Hello Pythonista"
        print(string / 0)
        return mensaje()
    except TypeError:
        print("Error: No puedes dividir por cero. Y menos una cadena")

mensaje()