class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None
        self.tamano = 0

    def longitud(self):
        return self.tamano
    def __len__(self):
        return self.tamano
    def __iter__(self):
        return self.raiz.__iter__()
    

Arbolbinario = ArbolBinarioBusqueda()
print(Arbolbinario.__len__())