from collections import deque

class Grafo():
    def __init__(self):
        self.relaciones = {}
    def __str__(self):
        return str(self.relaciones)
    
def agregar(grafo, elemento):
    grafo.relaciones.update({elemento:[]})
    
def relacionarUnilateral(grafo, origen, destino):
    grafo.relaciones[origen].append(destino)

def relacionar(grafo, elemento_1, elemento_2):
    relacionarUnilateral(grafo, elemento_1, elemento_2)
    relacionarUnilateral(grafo, elemento_2, elemento_1)

buenosAires = "Buenos Aires"; sanPedro = "San Pedro"; rosario = "Rosario"; cordoba = "Cordoba"; 
sanLuis = "San Luis"; mendoza = "Mendoza"; bahiaBlanca = "Bahia Blanca"; villaMaria = "Villa Maria"



Grafo = Grafo()
agregar(Grafo, buenosAires)
agregar(Grafo, sanPedro)
agregar(Grafo, sanLuis)
agregar(Grafo, rosario)
agregar(Grafo, cordoba)
agregar(Grafo, villaMaria)
agregar(Grafo, bahiaBlanca)
agregar(Grafo, mendoza)

relacionar(Grafo, buenosAires, sanPedro)
relacionar(Grafo, buenosAires, sanLuis)
relacionar(Grafo, buenosAires, bahiaBlanca)
relacionar(Grafo, buenosAires, sanLuis)

relacionar(Grafo, sanLuis, mendoza)
relacionar(Grafo, sanLuis, villaMaria)
relacionar(Grafo, sanLuis, bahiaBlanca)    

relacionar(Grafo, villaMaria, cordoba)
relacionar(Grafo, villaMaria, rosario)

relacionar(Grafo, rosario, sanPedro)

#=================================================== PROFUNDIDAD PRIMERO============================================
def profundidadPrimero(grafo, elementoInicial, funcion, elementos_recorridos = []):
    if elementoInicial in elementos_recorridos:
        return
    funcion(elementoInicial)
    elementos_recorridos.append(elementoInicial)
    for vecino in grafo.relaciones[elementoInicial]:
        profundidadPrimero(grafo, vecino, funcion, elementos_recorridos)

def imprimir(elemento):
    print(elemento)

#profundidadPrimero(Grafo, buenosAires, imprimir)

#================================================ ANCHO PRIMERO ====================================================

def anchoPrimero(grafo, elementoInicial, funcion, cola = deque(), elementosRecorridos = []):
    if not elementoInicial in elementosRecorridos:
        funcion(elementoInicial)
        elementosRecorridos.append(elementoInicial)
        if(len(grafo.relaciones[elementoInicial]) > 0):
            cola.extend(grafo.relaciones[elementoInicial])
    if len(cola) != 0:
        anchoPrimero(grafo, cola.popleft(), funcion, cola, elementosRecorridos)

anchoPrimero(Grafo, buenosAires, imprimir)
