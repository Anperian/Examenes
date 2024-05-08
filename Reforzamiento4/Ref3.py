def profesion():
    try:
        persona = {'nombre':'Xavier', 'apellido':'Rodriguez', 'dni':'63325345'}
        persona['profesion']
        return profesion()
    except KeyError:
        print("Error: No existe la clave 'Profesión'")

profesion()