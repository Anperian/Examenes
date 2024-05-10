list = [5, 2, 1, 4, 8, 3, 6, 7, 9, 10]
print("Lista original: ", list)
cubos = [números ** 3 for números in list]
print("Lista de cubos: ", cubos)
cuadrados = [números ** 2 for números in list]
print("Lista de cuadrados: ", cuadrados)
list2 = cubos + cuadrados
print("Lista de suma de ambas listas: ", list2)
list2.reverse()
print("Lista de suma invertida de ambas listas: ", list2)