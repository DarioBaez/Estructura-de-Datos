#Este escript busca "Buscar" a los alumnos
from BBDDs import Select
from Listar import Listar

#Esta funcion recibira un parametro por el cual hara la busqueda de los archivos 

def BuscarAlu(Opc):
    
    if Opc == 1:
        #Busqueda por Nombre
        Valor = input("Ingrese el Nombre: ")
        ValorAdquirido = Select("Nombre", Valor)
    elif Opc == 2:
        #Busqueda por Carrera
        Valor = input("Ingrese la Carrera: ")
        ValorAdquirido = Select("Carrera", Valor)
    elif Opc == 3:
        #Busqueda por Semestre
        Valor = input("Ingrese el Semestre: ")
        ValorAdquirido = Select("Semestre", Valor)
    elif Opc == 4:
        #Busqueda por Numero de control
        Valor = input("Ingrese el N0 Control: ")
        ValorAdquirido = Select("NControl", Valor)
    elif Opc == 5:
        #Busqueda por RFC
        Valor = input("Ingrese el RFC: ")
        ValorAdquirido = Select("Rfc", Valor)
    else:
        print("No existe esa opcion")

    Listar(ValorAdquirido)
