def lista():
    try:
        lista = [2, 6, 10, 4, 5, 23, 1]
        lista[10]
        return lista
    except IndexError:
        print("Error: No existe dicho índice")

lista()