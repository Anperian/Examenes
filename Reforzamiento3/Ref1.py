var1 = int(input("Ingresa un primer número: "))
var2 = int(input("Ingresa un segundo número: "))

def suma(digitos):
    return sum(int(a) for a in str(digitos))

sum1 = suma(var1)
sum2 = suma(var2)

if sum1 > sum2:
        print(f"El número con una suma de dígitos mayor es: {var1}")
elif sum2 > sum1:
        print(f"El número con una suma de dígitos  mayor es: {var2}")
else:
        print("La suma de dígitos de ambos números es igual")

if sum1 < 10:
    print(f"{var1} tiene una suma de dígitos menor que 10")
else:
    print(f"{var1} tiene una suma de dígitos mayor que 10")
if sum2 < 10:
    print(f"{var2} tiene una suma de dígitos menor que 10.")
else:
    print(f"{var2} tiene una suma de dígitos mayor que 10")