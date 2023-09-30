from imprimir import ImprimirTodo
from filas import AgregarAlu
from Pila import pila  

ListaComida = {1:"Hamburguesa", 2:"Tortas", 3:"Pizza", 4:"Tacos", 5:"Enchiladas", 6:"Nada"}
ListaBebida = {1:"Coca", 2:"Pepsi", 3:"Mirinda", 4:"Nada"}
ListaPedido = []

Lista = []
def Menu():
    global Lista
    print("################## MENU ##################" "\n1) Agregar alumno", "\n2) Agregar pedido", "\n3) Imprimir todo", "\n4) Salir")
    Opc = int(input("Selecciona una opcion... "))
    P = pila()

    if Opc == 1:
        
        Lista = AgregarAlu(Lista)
        Menu()
    elif Opc == 2:
        Nombre = input("Ingresa el nombre del alumno: ")
        for J in Lista:
            if J == Nombre:
                print("Usuario registrado, ingrese el pedido")
                print(ListaComida)
                Comida = int(input("Ingresa el codigo de tu alimento: "))
                print(ListaBebida)
                Bebida = int(input("Ingresa el codigo de tu bebida: "))
                
                P.push({f"{Nombre}":f"{ListaComida[Comida]} {ListaBebida[Bebida]}"})
                P.print_cafe()
            else:
                print("El alumno no esta registrado")
        Menu()
        
        
    elif Opc == 3:
        print("Que quieres imprimir:", "\n1) Alumnos", "\n2) Comidas y Bebidas", "\n3) Pedidos")
        OPCi= int(input("Selecciona una opcion... "))
        if OPCi == 1:
            if Lista == []:
                print("La lista esta vacia")            
            else:
                Lista = ImprimirTodo(Lista)
                print(Lista)
                
        elif OPCi == 2:
            print(ListaComida)
            print(ListaBebida)
        elif OPCi == 3:
            if P.print_cafe() == []:
                print("Aun no se han realizado pedidos")
            else:
                P.print_cafe()
            
                
            
        Menu()
            
    elif Opc == 4:
        print("El programa ha finalizado.")
    
    elif Opc != 4:
        Menu()    #<-------- RECURSIVIDAD

Menu()






















"""AgregarPedido = pila()
        print("Que desas agregar a tu pedido... ")
        print(ListaBebida)
        print(ListaComida)
        Objeto = input("Escribe lo que quieras")
        ListaPedido.append(Objeto)
        AgregarPedido.push(ListaPedido)
        AgregarPedido.print_cafe()
        AgregarPedido.pop()
        Menu()"""