import random
import math


def tamaño(archivo):
    lista = int(input("Ingresa cuántos elementos tendrá la lista: "))
    lista1 = [random.randint(1, 100) for i in range(lista)]
    with open(archivo, "a") as texto:
        for num in lista1:
            texto.write(str(num) + "\n")
        texto.close()
    return lista1


def cuadrados(lista, archivo):
    raices = [math.sqrt(num) for num in lista]
    with open(archivo, "a") as texto:
        for raiz in raices:
            texto.write(str(raiz) + "\n")
        texto.close()
