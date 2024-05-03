def datos():
    try:
        var1 = float(input("Ingresa un número: "))
        var2 = float(input("Ingresa otro número: "))
        return var1, var2
    except ValueError:
        print("Ingresa datos numéricos")
        return datos()

def cero():
    try:
        var1, var2 = datos()
        result = var1 / var2
        print("La división es:", result)
    except ZeroDivisionError:
        print("¡No hay división entre cero!")
        cero()

def suma():
    try:
        var1, var2 = datos()
        result = var1 + var2
        print("La suma es ", result)
    except ValueError:
        print("Ingresa datos numéricos")
        return suma()

def lista():
    list = []
    try:
        var1 = float(input("Ingresa un primer número: "))
        var2 = float(input("Ingresa un segundo número: "))
        var3 = float(input("Ingresa un tercer número: "))
        list.append(var1)
        list.append(var2)
    except ValueError:
        print("Ingresa valores numéricos")
        return lista()
    return list

def indice(lista):
    try:
        ind = int(input("Ingresa el índice: "))
        print("El valor es ", lista[ind])
    except IndexError:
        print("No hay valor en ese índice")
    except ValueError:
        print("Ingresa valores numéricos")
        return indice(lista)

cero()
suma()
list = lista()
indice(list)