class Arbol(object):
    def __init__(self):
        self.derecha = None
        self.izquierda = None
        self.dato = None


raiz = Arbol()
raiz.dato = "Raiz"
raiz.izquierda = Arbol()
raiz.izquierda.dato = "Izquierda"
raiz.derecha = Arbol()
raiz.derecha.dato = "Derecha"

raiz.izquierda.izquierda = Arbol()
raiz.izquierda.izquierda.dato = "Izquierda 2"
raiz.izquierda.derecha = Arbol()
raiz.izquierda.derecha.dato = "Izquierda - Derecha"

print(raiz.izquierda.dato)
print(raiz.izquierda.derecha.dato)