#Este método extiende una lista agregando un iterable al final. 
versiones_plone = [2.1, 2.5, 3.6] 
print(versiones_plone) 

versiones_plone.extend([4])
print(versiones_plone )

versiones_plone.extend(range(5,7))
print(versiones_plone) 