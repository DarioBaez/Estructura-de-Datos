import Buscador, Capturar, Listar
from Capturar import AlumnosCaptured
from Listar import ListarAlu
from Buscador import BuscarAlu

#Funcion menu
def Menu():
    while True:
        print("\n\n----------------------------------------------\n                 MENU                  \n",
              "1) Capturar alumno\n", "2) Buscar alumno\n", "3) Listar alumnos\n", "4) Salir")
        try:
            Opcion = int(input("Seleccione una opcion... "))
        except ValueError:
            print("Esa opcion no existe")
            break
        
        if Opcion == 1:
            AlumnosCaptured()
        elif Opcion == 2:
            print("Seleccione el parametro por el cual hara la busqueda\n", 
                  "1) Nombre\n", "2) Carrera\n", "3) Semestre\n", "4) N0 Control\n", "5) RFC")
            try:
                BuscarAlu(int(input("Selecciona una opcion... ")))
            except ValueError:
                print("Esa opcion no existe")
                break
        elif Opcion == 3:
            ListarAlu()                     
        else:
            break
    
    print("BYE")


        
Menu()