def AgregarAlu(Lista_alumnos):
    
    Alumno = input("Ingresa el nombre del alumno: ")
    Lista_alumnos.append(Alumno)
    
    if Lista_alumnos.count(Alumno) > 1:
        print("El alumno no se ha registrado porque su nombre se repite 2 veces, ingrese otro nombre.")
        Lista_alumnos.pop()
    
    return Lista_alumnos