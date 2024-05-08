def calc(var2, var3):
    return (var2 + var3) / 2
def aprobar(var1, prom):
    if prom >= 11:
        print(f"{var1} aprobó")
    else:
        print(f"{var1} desaprobó")
def calificacion(var1, var2, var3):
    prom = calc(var2, var3)
    with open("calificaciones.txt", "a") as archivo:
        archivo.write(f"{var1} obtuvo {var2} y {var3}. Su promedio fue {prom}\n")
    aprobar(var1, prom)

calificacion("Santiago", 14, 17)
calificacion("Ricardo", 11, 7)
