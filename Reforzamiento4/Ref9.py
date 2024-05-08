def mult():
    while True:
        try:
            num = int(input("Introduce un número entero entre 1 y 20: "))
            if 1 <= num <= 20:
                break
            else:
                print("Debe estar entre 1 y 20")
        except ValueError:
            print("Debe ser un número entero")

    with open("tabla.txt", "w") as archivo:
        for i in range(0, 11):
            resultado = num * i
            archivo.write(f"{num} x {i} = {resultado}\n")
    print(f"Se ha guardado el resultado en 'tabla.txt'.")

mult()