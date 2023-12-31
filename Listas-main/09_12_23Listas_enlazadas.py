#Esta clase NODE crea un nodo, requiere de un dato y nodo como argumentos
#de manera predeterminada estos seran NULL
class node():
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

#Esta clase linked_list crea una una lista que recibira un valor y nodo, y conectara mediante nodos
#La lista siguiente por el nodo
class linked_list():
    def __init__(self):
        self.head = None

    #Este metodo agregara al frente, crea el nodo y recibe el valor
    def add_at_front(self, data):
        self.head = node(data = data, next = self.head)
    
    #Este metodo solo verificara si el valor en self.head esta en None o con algun valor
    #retornara un booleano
    def is_empty(self):
        return self.head == None
    
    #Este metodo agregara al final, recibira el dato y creara un nodo
    def add_at_end(self, data):
        if not self.head:
            self.head = node(data = data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node(data = data)

    #Este metodo eliminara los nodos, recibira un argumento llamado key
    def delete_node(self, key):
        curr = self.head()
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    #Este metodo va a obtener el ultimo nodo
    def get_last_node(self):
        temp = self.head
        while(temp.next is not None):
            temp = temp.next
            return temp.data
    #Este metodo imprimira la lista de los nodos
    def print_list(self):
        node = self.head
        while node != None:
            print(node.data, end = " => ")
            node = node.next

#Aqui creamos una instancia de la clase "Linked_list"
s = linked_list()
s.add_at_front(5) #Se llama al metodo add_at_front que agregara valores al principio
s.add_at_end(8) #Se llama al metodo add_at_end que agregara valores al final
s.add_at_front(9) #Se llama al metodo add_at_front que agregara valores al principio
s.print_list() #Se llama al metodo print_list el cual imprimira en secuencia los valores de la lista
