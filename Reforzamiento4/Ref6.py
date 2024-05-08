import operaciones
def sumar():
    num1 = operaciones.numero()
    num2 = operaciones.numero()
    resultado = operaciones.suma(num1, num2)
    print(f"La suma es: {resultado}")

if __name__ == "__main__":
    sumar()