import math
def entero():
    try:
        var1 = int(input("Ingresa un entero: "))
        return var1
    except ValueError:
        print("Debes ingresar un entero válido.")
        return entero()
def raiz(num):
    raiz = math.sqrt(num)
    print(f"La raíz cuadrada de {num} es {raiz}")

def operaciones(num):
    cuadrado = num ** 2
    cubo = num ** 3
    print(f"{num} al cuadrado es {cuadrado}")
    print(f"{num} al cubo es {cubo}")
