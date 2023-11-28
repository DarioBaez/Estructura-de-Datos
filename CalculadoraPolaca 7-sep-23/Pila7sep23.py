class Pila():
    #Representa una pila con operaciones de apilar, desapilar y verificar

    def __init__(self):
        self.items = []

    def apilar(self, x):
        self.items.append(x)

    def desapilar(self):

        try:
            return self.items.pop()
        except:
            print("La pila esta vacia")
        
        
    def es_vacia(self):
        return self.items == []
    
    def imprimir(self):
        for I in self.items:
            print(I)
    
P = Pila()
print(P.es_vacia()) #true
print(P.apilar(1))
print(P.es_vacia()) #false
print(P.apilar(5))
print(P.apilar("+"))
print(P.apilar(22))
print(P.desapilar()) #22
#print(P)

#Q = Pila()
#Q.desapilar()

    