def insertionSort(Lista):
    for I in range(1, len(Lista)):
        Inserter = Lista[I]

        J = I - 1

        while J >= 0 and Lista[J] > Inserter:
            Lista[J+1] = Lista[J]
            J -= 1
        
        Lista[J + 1] = Inserter

ListaN = [5,2,1,8,4]
print("Lista sin ordenar: ", ListaN)
insertionSort(ListaN)
print("Lista ordenada: ", ListaN)