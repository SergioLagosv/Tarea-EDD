from hash_funciones import *

class hash:
	def __init__(self, capacidad):
		self.tabla = tabla_hash(capacidad)

	def agregar(self, nombre, apellido, telefono, mail):					#AGREGAR ELEMENTOS
		self.tabla[apellido] = contacto( nombre, apellido, telefono, mail)

	def eliminar(self,apellido_buscado):											#ELIMINAR
		self.tabla.remove(apellido_buscado)

	def buscar(self,apellido_buscado):												#BUSCAR
		return self.tabla[apellido_buscado]