def decorador(mult):
    def m(*args, **kwargs):
        print("Está por ejecutarse la función")
        result = mult(*args, **kwargs)
        print("La multiplicación es", result)
        print("La función ha sido ejecutada correctamente")
        return result
    return m
@decorador
def mult(*args, **kwargs):
    result = 1
    for arg in args:
        result = result * arg
    for i in kwargs.values():
        result *= i
    return result

result = mult(1, 2, 3, 4)