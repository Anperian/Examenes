class Agenda:
    def __init__(self):
        self.contactos = []

    def añadir_contacto(self, nombre, telefono, email, DNI):
        contacto = {'Nombre': nombre, 'Teléfono': telefono, 'Email': email, 'DNI': DNI}
        self.contactos.append(contacto)
    def mostrar_contactos(self):
        for contacto in self.contactos:
            print("Nombre:", contacto['Nombre'])
            print("Teléfono:", contacto['Teléfono'])
            print("Email:", contacto['Email'])
            print("DNI:", contacto['DNI'])

agenda = Agenda()
agenda.añadir_contacto("Santiago", "9777XXX", "santiago@hotmail.com", "123123123")
agenda.añadir_contacto("Roberto", "9677XXX", "roberto@hotmail.com", "123321231")
agenda.mostrar_contactos()