def imprimir(x):
    if x>0:
        print(x)
        imprimir(x-1)

imprimir(5)