var1 = int(input("Ingresa un número: "))
def suma(dígitos):
    return sum(int(a) for a in str(dígitos))

sum = suma(var1)
print(f"La suma de los dígitos es {sum}")