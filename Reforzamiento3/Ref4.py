var1 = input("Ingresa una oración con 3 palabras o más: ")
def palabra(var1):
    palabras = var1.split()
    return len(palabras)

if palabra(var1) < 3:
    print("La oración debe contener 3 palabras o más")
else:
    num = palabra(var1)
    print(f"La oración tiene {num} palabras")