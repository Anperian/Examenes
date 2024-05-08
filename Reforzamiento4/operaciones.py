def numero():
    try:
        num = int(input("Ingresa un entero: "))
        return num
    except ValueError:
        print("Debes ingresar un entero")
        return numero()
def suma(var1, var2):
    suma = var1 + var2
    return suma