def decorador(func):
    def argumentos(*args, **kwargs):
        print("La cantidad de argumentos que tiene la función es\n",len(args) + len(kwargs))
        result = func(*args, **kwargs)
        print("La función decoradora terminó de ejecutarse correctamente")
        return result
    return argumentos
@decorador
def tarea(*args, **kwargs):
    pass

tarea(4, 1, 10, 2, 50, 64)