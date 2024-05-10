import random


def numeros():
    nums = []
    for i in range(10):
        numero = random.randint(1, 100)
        nums.append(numero)
    print(nums)
    return nums


def numeros1(lista):
    nums_repetidos = set(lista)
    print(nums_repetidos)
    return list(nums_repetidos)


def ordenar_mayor(lista):
    lista.reverse()
    lista_ordenada = sorted(lista, reverse=True)

    return lista_ordenada


def ordenar_menor(lista):
    lista_ordenada = sorted(lista)
    return lista_ordenada


def mayor(lista):
    par = max((i for i in lista if i % 2 == 0))
    return par
