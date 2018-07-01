from lista import *

class contacto:
    def __init__(self, nombre_nuevo, apellido_nuevo, telefono_nuevo, mail_nuevo):
        self.apellido = apellido_nuevo
        self.nombre = nombre_nuevo
        self.mail = mail_nuevo
        self.telefono = telefono_nuevo
        self.izquierda = None
        self.derecha = None

class abb():
    def __init__(self):
        self.raiz = None
        
    def _agregar(self, a, nombre, apellido, telefono, mail):
        if apellido < a.apellido:
            if a.izquierda == None:
                a.izquierda = (contacto(nombre,apellido,telefono,mail)) 
                return   
            self._agregar(a.izquierda,nombre,apellido,telefono,mail)
        else:
            if a.derecha == None:
                a.derecha =(contacto(nombre,apellido,telefono,mail))
                return
            self._agregar(a.derecha, nombre,apellido,telefono,mail)

    def _buscar(self, a, dato):
        if a == None:
            return None
        else:
            if dato == a.apellido:
                print(True)
                return True
            else:
                self.buscar_dato(a.izquierda,dato)
                self.buscar_dato(a.derecha,dato)

    def _eliminar(self, a, dato, cadena):
        if a == None:
            return None
        else:
            self._eliminar(a.derecha,dato,cadena)
            cadena.agregar(a.nombre,a.apellido,a.telefono,a.mail)
            self._eliminar(a.izquierda,dato,cadena)

    def agregar(self,nombre,apellido,telefono,mail):
        if self.raiz == None:
            self.raiz = contacto(nombre,apellido,telefono,mail)
        self._agregar(self.raiz,nombre,apellido,telefono,mail)

    def inorder(self, dato):
        if dato == None:
            return None
        else:
            self.inorder(dato.izquierda)
            print(dato.apellido)
            self.inorder(dato.derecha)

    def buscar(self,dato):                                         
        if self.buscar_dato(self.raiz,dato):
            return True

    def add_tree(self, a):
        if a != None:
            self.add_tree(a.izquierda)
            self.agregar(a.nombre,a.apellido,a.telefono,a.mail)
            self.add_tree(a.derecha)

    def eliminar(self,dato):
        cadena = lista()
        self._eliminar(self.raiz, dato, cadena)
        cadena.eliminar(dato)
        self.raiz = None
        dato = cadena.getHead()
        while dato != None:
            self.agregar(dato.nombre,dato.apellido,dato.telefono,dato.mail)
            dato = dato.getsiguiente()

    def imprimir(self):
        self.inorder(self.raiz)
















