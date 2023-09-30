
#LISTA
factura = ['pan', 'huevos', 100, 1234] 
print(factura)

#Indice negativo
print(factura[-1])

#Usando la funcion len
print(factura[-len(factura)])

#Cambiando el valor en la ubicacion marcada por el indice
factura[1] = "carne"
print(factura)