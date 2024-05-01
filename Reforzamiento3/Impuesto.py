def impuesto(sueldo):
    if sueldo > 5000:
        impuesto = sueldo * 0.10
        return impuesto
    else:
        return 0

def saludo(nombre):
    return "Hola" + " " + nombre