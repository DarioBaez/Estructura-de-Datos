import time
import random

lista = [random.random() for _ in range(10**7)]

# Inserción al principio de la lista
inicio = time.time()
lista.insert(0, 'nuevo_elemento')
fin = time.time()
print(f"Tiempo de inserción al principio: {fin - inicio} segundos")

# Inserción al final de la lista
inicio = time.time()
lista.append('nuevo_elemento')
fin = time.time()
print(f"Tiempo de inserción al final: {fin - inicio} segundos")                 
