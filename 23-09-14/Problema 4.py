def imprimir(x):
    if x>0:
        imprimir(x-1)
        print(x)
        
imprimir(5)