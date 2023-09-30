#Este escript busca capturar a los alumnos en una base de datos

#Importamos SQLITE3 que usaremos para conectarnos a una BBDD de sqlite
from BBDDs import ENVIARBBDD


#Esta funcion solicitara los datos a capturar de los alumnos
def AlumnosCaptured():
    try:
        NControl = int(input("Ingrese el NO.control del alumno: "))
        Nombre = input("Ingrese el nombre del alumno: ")
        Semestre = int(input("Ingrese el semestre del alumno: "))
        Carrera = input("Ingrese la carreara del alumno: ")
        Rfc = input("Ingrese el RFC de alumno: ")

        a = Alumno(NControl, Nombre, Semestre, Carrera, Rfc)
        ENVIARBBDD(a)
    except ValueError:
        print("Has ingresado un valor incorrecto")
    

    


#Objeto alumno
class Alumno():
    def __init__(self, NControl, Nombre, Semestre, Carrera, Rfc):
        self.Name = Nombre
        self.Semestre = Semestre
        self.Carrera = Carrera
        self.Rfc = Rfc
        self.NControl = NControl
    def getNombre(self):
        return self.Name
    def getSemestre(self):
        return self.Semestre
    def getCarrera(self):
        return self.Carrera
    def getRfc(self):
       return self.Rfc
    def getNControl(self):
       return self.NControl
    



