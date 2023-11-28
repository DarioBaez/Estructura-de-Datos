class ArbolBinarioBusqueda():
    def __init__(self):
        self.raiz = None
        self.tamano = 0

    def longitud(self):
        return self.tamano
    def __len__(self):
        return self.tamano
    def __iter__(self):
        return self.raiz.__iter__()
    
    def agregar(self,clave,valor):
        if self.raiz:
            self._agregar(clave,valor,self.raiz)
        else:
            self.raiz = NdoArbol(clave,valor)
        self.tamano = self.tamano + 1

    def _agregar(self,clave,valor,nodoActual):
        if clave < nodoActual.clave:
            if nodoActual.tieneHijoIzquierdo():
                self.agregar(clave,valor,nodoActual.hijoIzquierdo)
            else:
                nodoActual.hijoIzquierdo = NdoArbol(clave,valor,padre = nodoActual)
        else:
            if nodoActual.tieneHijoDerecho():
                self._agregar(clave,valor,nodoActual.hijoDerecho)
            else:
                nodoActual.hijoDerecho = NdoArbol(clave,valor,padre = nodoActual)


class NdoArbol():
    def __init__(self,clave, valor,izquierdo = None, derecho=None, padre= None):
        self.clave = clave
        self.Cargautil = valor
        self.hijoIzquierdo = izquierdo
        self.hijoDerecho = derecho
        self.padre = padre

    def tieneHijoIzquierdo(self):
        return self.hijoIzquierdo
    def tieneHijoDerecho(self):
        return self.hijoDerecho
    def esHijoIzquierdo(self):
        return self.padre and self.padre.hijoIzquierdo == self
    def esHijoDerecho(self):
        return self.padre and self.padre.hijoDerecho == self
    def esRaiz(self):
        return not self.padre
    def esHoja(self):
        return not (self.hijoDerecho or self.hijoIzquierdo)
    def tieneAlgunHijo(self):
        return self.hijoDerecho or self.hijoIzquierdo
    def tieneAmbosHijos(self):
        return self.hijoDerecho and self.hijoIzquierdo
    def reemplazarDatoDeNodo(self,clave,valor,hizq,hder):
        self.clave = clave
        self.Cargautil = valor
        self.hijoIzquierdo = hizq
        self.hijoDerecho =hder

        if self.tieneHijoIzquierdo(): 
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho(): 
            self.hijoDerecho.padre = self    
