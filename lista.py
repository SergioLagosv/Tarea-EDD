class contacto:
    def __init__(self, nombre_nuevo, apellido_nuevo, telefono_nuevo, mail_nuevo):
        self.mail = mail_nuevo
        self.apellido = apellido_nuevo
        self.nombre = nombre_nuevo
        self.telefono = telefono_nuevo
        self.siguiente = None

class lista:
	def __init__(self):
		self.root = None

	def agregar(self, nombre, apellido, telefono, mail):
		temp = self.root
		prev = None
		stop = False
		while temp != None and not stop:
		    if temp.apellido > apellido:
		        stop = True
		    else:
		        prev = temp
		        temp = temp.siguiente

		nuevo = contacto(nombre,apellido,telefono,mail)		

		if prev == None:
		    nuevo.siguiente = self.root
		    self.root = nuevo
		else:
		    nuevo.siguiente = temp
		    prev.siguiente = nuevo

	def eliminar(self,dato):								
		if self.root == None:
			return

		temp = self.root
		prev = temp

		if temp.apellido == dato:
			self.root = temp.siguiente

		while temp != None:
			if temp.apellido == dato:
				prev.siguiente = temp.siguiente
				return
			else:
				prev = temp
				temp = temp.siguiente

	def imprimir(self):
		temp = self.root
		while temp:
			print temp.apellido
			temp = temp.siguiente

	def buscar(self,dato):								
		temp = self.root
		while temp:
			if temp.nombre == dato or temp.apellido == dato or temp.telefono == dato or temp.mail == dato:
				return True
			else:
				temp = temp.siguiente
		return False


temp = lista()
temp.agregar("a","a",123123,"hola@gogel.com")
temp.agregar("b","ba",123123,"hola@gogel.com")
temp.agregar("b","b",123123,"hola@gogel.com")

temp.agregar("b","b",123123,"hola@gogel.com")
temp.agregar("c","c",123123,"hola@gogel.com")
temp.agregar("d","d",123123,"hola@gogel.com")
temp.imprimir()
temp.eliminar("c")
print("---------------")
temp.imprimir()
