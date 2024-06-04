from Objetos.Contacto import Contacto
class ListaContactos:
    def __init__(self):
        self.contactos = {}  # crear un diccionario vacio, donde luego pondras tus contactos

    def agregarContacto(self, nombre, contacto):
        self.contactos[nombre] = contacto

    def buscarContacto(self, nombre):
        return self.contactos.get(nombre)

    def editarContacto(self, nombre, nuevoTelefono, nuevoCorreo):
        contacto = self.buscarContacto(nombre)
        if contacto:
            contacto.telefono = nuevoTelefono
            contacto.correo = nuevoCorreo
        print("Contacto editado")

    def mostrarLista(self):
        return list(self.contactos.values())

    def eliminarContacto(self, nombre):
        if nombre in self.contactos:
            del self.contactos[nombre]
