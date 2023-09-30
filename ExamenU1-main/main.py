#Este script ejecuta el programa
from matriz import matrices

def Menu():
    print("1) Matriz(orden ascendente)","\n2) Matriz(orden descendente)", "\n3) Matriz(caracol)")
    OPc = int(input())
    if OPc == 1:
        M1 = matrices(4,3)
        M1.hacerMatriz()
        M1.llenarMatriz1()
        print(M1.getLista())
        M1.ImprimirMatriz()
        Menu()
    elif OPc == 2:
        M2 = matrices(4,3) 
        M2.hacerMatriz()
        M2.llenarMatriz2(12) 
        print(M2.getLista())
        M2.ImprimirMatriz()
        Menu()
    elif OPc == 3:
        M3 = matrices(4,3)
        M3.hacerMatriz()
        M3.llenarMatriz3(12)
        print(M3.getLista())
        M3.ImprimirMatriz()
        Menu()
    else:
        print("fin de la ejecucion")
Menu()