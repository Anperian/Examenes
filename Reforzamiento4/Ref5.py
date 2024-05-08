import Mod1
def main():
    usuario = input("Ingresa tu usuario: ")
    result = Mod1.nombre(usuario)
    if result == True:
        print(f"Tu nombre de usuario es {usuario}")
    else:
        print(result)
        main()

if __name__ == "__main__":
    main()