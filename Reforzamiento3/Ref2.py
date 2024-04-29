var1 = int(input("Ingresa un número: "))
var2 = int(input("Ingresa otro número: "))
def cuadrados(var1, var2):
    if var1 < var2:
        menor = var1
        mayor = var2
    else:
        menor = var2
        mayor = var1

    for a in range(menor+1, mayor):
        cuadrado = a ** 2
        print(f"El cuadrado de {a} es: {cuadrado}")

cuadrados(var1, var2)