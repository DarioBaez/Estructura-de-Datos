class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self.cima = None

    def esta_vacia(self):
        return self.cima is None

    def apilar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cima
        self.cima = nuevo_nodo

    def desapilar(self):
        if self.esta_vacia():
            return None
        dato = self.cima.dato
        self.cima = self.cima.siguiente
        return dato
    
pila = Pila()

# Verificar si la pila está vacía
print(pila.esta_vacia()) # True

# Apilar algunos datos
pila.apilar('avion')
pila.apilar('pelota')
pila.apilar('camisa')

# Verificar si la pila está vacía después de apilar datos
print(pila.esta_vacia()) # False

# Desapilar los datos
print(pila.desapilar()) # 'avion'
print(pila.desapilar()) # 'pelota'
print(pila.desapilar()) # 'camisa'

# Verificar si la pila está vacía después de desapilar todos los datos
print(pila.esta_vacia()) # True