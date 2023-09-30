def ImprimirTodo(desordenada):  #<------ Ordenamiento
    Lista_Ordenada = desordenada
    for I in range(0,(len(Lista_Ordenada)**2)):
        for J in range(0,len(Lista_Ordenada)):
            try:
                if Lista_Ordenada[J] < Lista_Ordenada[J+1]:
                    pass
                elif Lista_Ordenada[J] > Lista_Ordenada[J+1]:
                    aux = Lista_Ordenada[J]
                    aux2 = Lista_Ordenada[J+1]
                    Lista_Ordenada[J] = aux2
                    Lista_Ordenada[J+1] = aux
                
                
            except:
                pass
    
    return(Lista_Ordenada)


#lista = [9,8,7,6,5]
#lista = ["A", "B", "D", "C"]
#print(lista)
#ImprimirTodo(lista)
