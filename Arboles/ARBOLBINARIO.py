#Clase llamada nodo
class Nodo:
#Constructor con los argumentos
    def __init__(self, value=None, izq=None, der=None):
#Punteros
        self.value = value
        self.izq = izq
        self.der = der
#Retornar el valor
    def __str__(self):
        return self.value
    


#Clase del arbol binario
class aBinarios:
#metodo constructor y el atributo raiz
    def __init__(self):
        self.raiz = None
#creamos la funcion agregar
    def agregar(self, elemento):
        if self.raiz == None:
            self.raiz = elemento
        else:
            aux = self.raiz
            padre = None
            while aux != None:
                padre = aux
                if int(elemento.value) >= int(aux.value):
                    aux = aux.der
                else:
                    aux = aux.izq
            if int(elemento.value) >= int(padre.value):
                padre.der = elemento
            else:
                padre.izq = elemento
#se crea metodo mostrar el preorden
    def preorden(self, elemento):
        if elemento != None:
            print(elemento)
            self.preorden(elemento.izq)
            self.preorden(elemento.der)
#se crea metodo mostrar el posrden (recursividad)
    def postorden(self, elemento):
        if elemento != None:
            self.postorden(elemento.izq)
            self.postorden(elemento.der)
            print(elemento)
#se crea metodo mostrar el inorden
    def inorden(self, elemento):
        if elemento != None:
            self.inorden(elemento.izq)
            print(elemento)
            self.inorden(elemento.der)
#se crea funcion que permite obtener la reiz
    def getRaiz(self):
        return self.raiz
    

#llamamos el objeto de arbol binario
nodos = Nodo(value=10, izq="nodeizq", der="nodeder")
ab = aBinarios(nodos)



