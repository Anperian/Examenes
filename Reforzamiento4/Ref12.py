def decorador(saludo):
    def mensaje(*args, **kwargs):
        print("Buenos días")
        result = saludo(*args, **kwargs)
        print("Soy", result)
        print("Hasta luego")
        return result
    return mensaje
@decorador
def nombre(var1):
    return var1

var1 = input("Ingresa tu nombre: ")
mensaje_resultado = nombre(var1)