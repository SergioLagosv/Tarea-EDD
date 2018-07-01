class contacto:
    def __init__(self, nombre_nuevo, apellido_nuevo, telefono_nuevo, mail_nuevo):
        self.apellido = apellido_nuevo
        self.nombre = nombre_nuevo
        self.mail = mail_nuevo
        self.telefono = telefono_nuevo
        self.izquierda = None
        self.derecha = None

class avl():
    def __init__(self):
        self.root = None 
        self.h = -1  
        self.balance = 0

    def geth(self):
        if self.head: 
            return self.root.h
        else: 
            return 0 
    
    def es_hoja(self):
        return (self.h == 0) 
    
    def agregar(self, nombre, apellido, telefono, mail):                   #agregar
        tree = self.root

        new_contacto = contacto(nombre,apellido,telefono,mail)
        
        if tree == None:
            self.root = new_contacto 
            self.root.izquierda = avl() 
            self.root.derecha = avl()
        
            
        elif apellido > tree.apellido: 
            self.root.derecha.agregar(nombre,apellido,telefono,mail)
            
        else: 
            self.root.izquierda.agregar(nombre,apellido,telefono,mail)
        self.balancear() 
        
    def balancear(self):
        self.update_hs(False)
        self.rebalancear(False)
        while self.balance < -1 or self.balance > 1: 
            if self.balance > 1:
                if self.root.izquierda.balance < 0:  
                    self.root.izquierda.corregir_izq()
                    self.update_hs()
                    self.rebalancear()
                self.corregir_der()
                self.update_hs()
                self.rebalancear()
                
            if self.balance < -1:
                if self.root.derecha.balance > 0:  
                    self.root.derecha.corregir_der()
                    self.update_hs()
                    self.rebalancear()
                self.corregir_izq()
                self.update_hs()
                self.rebalancear()

    def update_hs(self, recurse=True):
        if not self.root == None: 
            if recurse: 
                if self.root.izquierda != None: 
                    self.root.izquierda.update_hs()
                if self.root.derecha != None:
                    self.root.derecha.update_hs()
            
            self.h = max(self.root.izquierda.h,
                              self.root.derecha.h) + 1 
        else: 
            self.h = -1 
            
    def rebalancear(self, recurse=True):
        if not self.root == None: 
            if recurse: 
                if self.root.izquierda != None: 
                    self.root.izquierda.rebalancear()
                if self.root.derecha != None:
                    self.root.derecha.rebalancear()

            self.balance = self.root.izquierda.h - self.root.derecha.h 
        else: 
            self.balance = 0 

    def eliminar(self, dato):                                                   #ELIMINAR POR APELLIDO
        if self.root != None: 
            if self.root.apellido == dato: 
                if self.root.izquierda.root == None and self.root.derecha.root == None: #ELIMINAR HOJAS 
                    self.root = None  
                elif self.root.derecha.root == None: 
                    self.root = self.root.izquierda.root
                elif self.root.izquierda.root == None: 
                    self.root = self.root.derecha.root
                else:  
                    reemplazo = self.sucesor(self.root)
                    if reemplazo != None:
                        self.root.apellido = reemplazo.apellido  
                        self.root.derecha.eliminar(reemplazo.apellido)              
                self.balancear()
                return  
            elif dato <= self.root.apellido: 
                self.root.izquierda.eliminar(dato)  
            elif dato > self.root.apellido: 
                self.root.derecha.eliminar(dato)
                        
            self.balancear()
        else: 
            return 
    
    def sucesor(self, aux):
        aux = aux.derecha.root  
        if aux != None:
            while aux.izquierda != None:
                if aux.izquierda.root == None: 
                    return aux 
                else: 
                    aux = aux.izquierda.root  
        return aux
        
    def corregir_der(self): 
        base = self.root 
        izq = self.root.izquierda.root 
        der = izq.derecha.root 
        self.root = izq 
        izq.derecha.root = base
        base.izquierda.root = der 

    
    def corregir_izq(self):
        base = self.root 
        der = self.root.derecha.root 
        izq = der.izquierda.root 
        self.root = der 
        der.izquierda.root = base 
        base.derecha.root = izq 

    def imprimir(self):                                                 
        self.update_hs()
        self.rebalancear()
        if(self.root != None): 
            self.root.izquierda.imprimir()
            print (self.root.apellido)  
            self.root.derecha.imprimir()

    def buscar(self,dato):                                                          
        if(self.root != None):
            if self.root.apellido == dato:
                print(True)
                return True
            self.root.izquierda.buscar(dato)
            self.root.derecha.buscar(dato)
        return

# temp = avl()
 
# temp.agregar(1,2,3,4)
# temp.agregar(2,3,3,4)
# temp.agregar(3,6,3,4)
# temp.agregar(4,8,3,4)
# temp.agregar(5,1,3,4)
# temp.agregar(1,2,3,4)
# temp.agregar(2,4,5,7)
# temp.agregar(3,1,3,4)
# temp.agregar(4,7,5,4)
# temp.agregar(5,5,3,4)
# temp.agregar(6,8,3,4)

# temp.imprimir()

# print("----------------------")

# temp.buscar(8)

# temp.eliminar(8)
# temp.eliminar(4)
# temp.eliminar(5)
# temp.eliminar(3)

# print("----------------------")

# temp.imprimir()
