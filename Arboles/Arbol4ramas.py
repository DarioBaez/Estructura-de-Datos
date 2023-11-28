class Arbol4(object):
    def __init__(self):
       
        self.derecha1 = None
        self.izquierda1 = None

        self.derecha2 = None
        self.izquierda2 = None

raiz = Arbol4()
raiz.derecha1 = "derecha1"

raiz.derecha2 = "derecha2"

raiz.izquierda1 = "izquierda1"

raiz.izquierda2 = "izquierda2"

print(raiz.izquierda1)