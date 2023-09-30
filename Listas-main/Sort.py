#Este método ordena los elementos de una lista. 
versiones_plone = [4, 2.5, 5, 3.6, 2.1, 6] 
print(versiones_plone) 

versiones_plone.sort() 
print(versiones_plone) 

#El método sort() admite la opción reverse, por defecto, con valor False. 
#De tener valor True, el ordenamiento se hace en sentido inverso. 
versiones_plone.sort(reverse = True) 
print(versiones_plone)