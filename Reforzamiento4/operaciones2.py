import random

def numeros():
    num = [random.randint(0, 100) for i in range(30)]
    return num
def orden(num):
    lista = sorted(num)
    print(lista)
    return lista