#Este método recibe como argumento un elemento, y borra su primera aparición en la lista. 
versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6] 
print(versiones_plone)
versiones_plone.remove(2.5) 
print(versiones_plone)

#El método devuelve un excepción ValueError si el elemento no se encuentra en la lista. 
versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6] 
print(versiones_plone)
versiones_plone.remove(7) 