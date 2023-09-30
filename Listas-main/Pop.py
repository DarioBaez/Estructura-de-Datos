#Este método devuelve el último elemento de la lista, y lo borra de la misma. 
versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6] 
print(versiones_plone.pop()) 
print(versiones_plone) 

#Opcionalmente puede recibir un argumento numérico, que funciona como 
#índice del elemento (por defecto, -1) 
versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6] 
print(versiones_plone.pop(2)) 
print(versiones_plone) 
