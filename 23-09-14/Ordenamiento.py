def ordenar(lista, cant):
    if cant > 1:
        for f in range(0, cant-1):
            if lista[f]> lista[f+1]:
                aux = lista[f]
                lista[f] = lista[f+1]
                lista[f+1] = aux
            ordenar(lista, cant - 1)

datos = [60,44,22,33,2]
print(datos)
ordenar(datos, len(datos))
print(datos)
