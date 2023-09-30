#Este script busca listar por carrera alos alumnos
from BBDDs import Select

def ListarAlu():

    #Se sacan los datos de la BBDD
    resultados = Select(0,0)

    #Esta es una lista de titulos para ordenar los valores en sus respectivas casillas
    print("N0 Control   Nombre       Semestre     Carrera      RFC")

    # Convertir cada elemento de cada Lista a cadena
    Cadena = [[str(I) for I in Lista] for Lista in resultados]

    # Calcular el ancho máximo para cada columna
    Anchos_maximos = [max((len(cadena)+5) for cadena in columna) for columna in zip(*Cadena)]

    # Imprimir cada Lista como una fila de la tabla
    N = 0
    for Lista in Cadena:
        N += 1
        print(f"{N} ", ' '.join(cadena.ljust(ancho) for cadena, ancho in zip(Lista, Anchos_maximos)))


def Listar(Valor):
    if Valor == []:
        print("No existe")
        
    N = 0
    for I in Valor:
        N += 1
        print(f"{N} ‖", ' ‖ '.join(str(J) for J in I))
        










    """promedio = 0
    cuentoM = 0
    for I in resultados:
        for M in I:
            if len(M) < 14:
                E = (14 - len(M))      
                espacio = " " * E

                promedio = promedio + espacio
                cuentoM = cuentoM + 1

        pro = promedio/cuentoM

        C = " ".join(str(J) for J in I)
        print(espacio, C, espacio)
    
        #ListaAlu[I.NControl]
       # ListaAlu[I.Nombre]
       # ListaAlu[I.Semestre]
       # ListaAlu[I.Carrera]
       # ListaAlu[I.Rfc]"""
       




    
