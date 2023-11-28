def bubble(Lista):
    intercambio = True;
    while intercambio:
        intercambio = False;
        for I in range(len(Lista)-1):
            if Lista[I] > Lista[I + 1]:
                Lista[I], Lista[I+1]= Lista[I+1], Lista[I]
                intercambio = True;

ListaN = [5,2,1,8,4]
print(ListaN)
bubble(ListaN)
print(ListaN)