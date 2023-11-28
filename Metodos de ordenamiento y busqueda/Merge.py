def Merge(LeftLista, RightLista):
    Lista_ordenada = []
    LeftListaIndice = RightListaIndice = 0
    LeftListaLen, RightListaLen  = len(LeftLista), len(RightLista)

    for _ in range(LeftListaLen + RightListaLen):
        if LeftListaIndice < LeftListaLen and RightListaIndice < RightListaLen:
            if LeftLista[LeftListaIndice] <= RightLista[RightListaIndice]:
                Lista_ordenada.append(LeftLista[LeftListaIndice])
                LeftListaIndice +=1
            else:
                Lista_ordenada.append(RightLista[RightListaIndice])
                RightListaIndice += 1

        elif LeftListaIndice == LeftListaLen:
            Lista_ordenada.append(RightLista[RightListaIndice])
            RightListaIndice += 1
        
        elif RightListaIndice == RightListaLen:
            Lista_ordenada.append(LeftLista[LeftListaIndice])
            LeftListaIndice += 1

        

    return Lista_ordenada

def MergeSort(Lista):
    if len(Lista) <= 1:
        return Lista
    Mid = len(Lista)// 2

    LeftLista = MergeSort(Lista[:Mid])
    RightLista = MergeSort(Lista[:Mid])

    return Merge(LeftLista, RightLista)

ListaN = [5,2,1,8,4]
print("Lista sin ordenar: ", ListaN)
ListaN = MergeSort(ListaN)
print("Lista ordenada: ", ListaN)