from Pila7sep23 import Pila

pila = Pila()
def Menu():
    while True:
        print("############### MENU ################\n 1)Apilar\n 2)Desapilar\n 3)Es_Vacia")
        Opc = int(input("Ingrese una opcion... "))
        if Opc == 4:
            break
        elif Opc == 1:
            M = input("Ingrese un valor para apilar: ")
            pila.apilar(M)
            pila.imprimir()
        elif Opc == 2:
            pila.desapilar()
            pila.imprimir()
        elif Opc == 3:
            print(pila.es_vacia())
            pila.imprimir()


Menu()