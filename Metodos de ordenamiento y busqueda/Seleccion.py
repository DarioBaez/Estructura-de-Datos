def SelectionSort(Lista):
    for I in range(len(Lista)):
        Valor_mas_chico = I

        for J in range(I+1, len(Lista)):
            if Lista[J] < Lista[Valor_mas_chico]:
                Valor_mas_chico = J

        Lista[I], Lista[Valor_mas_chico] = Lista[Valor_mas_chico], Lista[I]

ListaN = [5,2,1,8,4]
print("Lista sin ordenar: ", ListaN)
SelectionSort(ListaN)
print("Lista ordenada: ", ListaN)