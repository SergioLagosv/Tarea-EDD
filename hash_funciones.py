def funcion(llave_str, size):
    resp = sum([ord(c) for c in llave_str]) % size
    return resp

class contacto:
    def __init__(self, nombre, apellido, telefono, mail):
        self.apellido = apellido
        self.nombre = nombre
        self.mail = mail
        self.telefono = telefono

class tabla_hash:
    def __init__(self, tam):
        self.size = 0
        self.tam = tam
        self.data = [[] for _ in range(tam)]
        self.keys = []

    def set(self, llave, obj):
        def find_result_func(encontrado, tabla_hash_table_cell):
            if encontrado:
                encontrado[1] = obj
            else:
                tabla_hash_table_cell.append([llave, obj])
                self.size += 1
                self.keys.append(llave)

        self.encontrar_por_llave(llave, find_result_func)
        return self

    def get(self, llave):
        def find_result_func(encontrado, _):
            if encontrado:
                return encontrado[1]
            else:
                print("error")

        return self.encontrar_por_llave(llave, find_result_func)

    def encontrar_por_llave(self, llave, find_result_func):
        index = funcion(llave, self.tam)
        tabla_hash_table_cell = self.data[index]
        encontrado = None
        for item in tabla_hash_table_cell:
            if item[0] == llave:
                encontrado = item
                break
        return find_result_func(encontrado, tabla_hash_table_cell)

    def remove(self, llave):
        def find_result_func(encontrado, tabla_hash_table_cell):
            if encontrado:
                tabla_hash_table_cell.remove(encontrado)
                self.keys.remove(llave)
                self.size -= 1
                return encontrado[1]
            else:
                print("error")

        return self.encontrar_por_llave(llave, find_result_func)

    def llaves(self):
        return self.keys

    def __setitem__(self, llave, value):
        self.set(llave, value)

    def __getitem__(self, llave):
        return self.get(llave)
