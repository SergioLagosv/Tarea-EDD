from lista import *
from abb import *
from arbol_avl import *
from hash import *
import random
from time import time

if __name__ == '__main__':

#agregar

	print("LISTA ORDENADA ------------------------------------")
	
	temp10 = lista()
	temp20 = lista()
	temp100 = lista()
	temp1000 = lista()

	start_time = time()											

	for x in xrange(1,11):
		temp10.agregar(x,x,"telefono","mail")

	elapsed_time = time() - start_time 						

	print("tiempo agregar 10 contactos: ")
	print(elapsed_time)

	start_time = time()											

	for x in xrange(1,21):
		temp20.agregar(x,x,"telefono","mail")

	elapsed_time = time() - start_time 						

	print("tiempo agregar 20 contactos: ")
	print(elapsed_time)	

	start_time = time()											

	for x in xrange(1,101):
		temp100.agregar(x,x,"telefono","mail")

	elapsed_time = time() - start_time 						

	print("tiempo agregar 100 contactos: ")
	print(elapsed_time)	

	start_time = time()											

	for x in xrange(1,1001):
		temp1000.agregar(x,x,"telefono","mail")

	elapsed_time = time() - start_time 						

	print("tiempo agregar 1000 contactos: ")
	print(elapsed_time)

	print("ARBOL BINARIO DE BUSQUEDA--------------------------")
	
	temp10 = abb()
	temp20 = abb()
	temp100 = abb()
	temp1000 = abb()

	start_time = time()											

	for x in xrange(1,11):
		temp10.agregar(x,x,"telefono","mail")

	elapsed_time = time() - start_time 						

	print("tiempo agregar 10 contactos: ")
	print(elapsed_time)

	start_time = time()											

	for x in xrange(1,21):
		temp20.agregar(x,x,"telefono","mail")

	elapsed_time = time() - start_time 						

	print("tiempo agregar 20 contactos: ")
	print(elapsed_time)	

	start_time = time()											

	for x in xrange(1,101):
		temp100.agregar(x,x,"telefono","mail")

	elapsed_time = time() - start_time 						

	print("tiempo agregar 100 contactos: ")
	print(elapsed_time)	

	start_time = time()											

	# for x in xrange(1,1001):
	# 	temp1000.agregar(x,x,"telefono","mail")

	elapsed_time = time() - start_time 						

	print("tiempo agregar 1000 contactos: ")
	print(">>> maxima profundidad de recursion excedida <<<")
	print(elapsed_time)

	print("ARBOL AVL------------------------------------------")
	
	temp10 = avl()
	temp20 = avl()
	temp100 = avl()
	temp1000 = avl()

	start_time = time()											

	for x in xrange(1,11):
		temp10.agregar(x,x,"telefono","mail")

	elapsed_time = time() - start_time 						

	print("tiempo agregar 10 contactos: ")
	print(elapsed_time)

	start_time = time()											

	for x in xrange(1,21):
		temp20.agregar(x,x,"telefono","mail")

	elapsed_time = time() - start_time 						

	print("tiempo agregar 20 contactos: ")
	print(elapsed_time)	

	start_time = time()											

	for x in xrange(1,101):
		temp100.agregar(x,x,"telefono","mail")

	elapsed_time = time() - start_time 						

	print("tiempo agregar 100 contactos: ")
	print(elapsed_time)	

	start_time = time()											

	for x in xrange(1,1001):
		temp1000.agregar(x,x,"telefono","mail")

	elapsed_time = time() - start_time 						

	print("tiempo agregar 1000 contactos: ")
	print(elapsed_time)

	print("TABLA HASH ----------------------------------------")
	temp10 = hash(10)
	temp20 = hash(20)
	temp100 = hash(100)
	temp1000 = hash(1000)

	start_time = time()											

	for x in xrange(1,11):
		temp10.agregar(x,str(x),"telefono","mail")

	elapsed_time = time() - start_time 						

	print("tiempo agregar 10 contactos: ")
	print(elapsed_time)

	start_time = time()											

	for x in xrange(1,21):
		temp20.agregar(x,str(x),"telefono","mail")

	elapsed_time = time() - start_time 						

	print("tiempo agregar 20 contactos: ")
	print(elapsed_time)	

	start_time = time()											

	for x in xrange(1,101):
		temp100.agregar(x,str(x),"telefono","mail")

	elapsed_time = time() - start_time 						

	print("tiempo agregar 100 contactos: ")
	print(elapsed_time)	

	start_time = time()											

	for x in xrange(1,1001):
		temp1000.agregar(x,str(x),"telefono","mail")

	elapsed_time = time() - start_time 						

	print("tiempo agregar 1000 contactos: ")
	print(elapsed_time)


	