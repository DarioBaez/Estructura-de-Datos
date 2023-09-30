#Este script crea las matrices 
class matrices():
    def __init__(self, alto, largo):
        self.largo = largo
        self.alto = alto
        self.Lista = []

        """    def hacerMatriz(self):
        for J in range(0,self.alto):   #<---- Todo este metodo es el que se sustituira en metodos recursivos
            self.Lista.append([])
            for I in range(0,self.largo):
                self.Lista[J].append(0) """

    def hacerMatriz(self):                             # HacerMatriz, HacerMatrizRecursivo y LLenar Fila 
        self.hacerMatrizRecursivo(0)                   # Estan aplicando la recursividad
                                                       
    def hacerMatrizRecursivo(self, J):                 
        if J < self.alto:                              
            self.Lista.append([])                      
            self.llenarFila(J, 0)                      
            self.hacerMatrizRecursivo(J + 1)           
            
    def llenarFila(self, J, I):                       
        if I < self.largo:
            self.Lista[J].append(0)
            self.llenarFila(J, I + 1)

    def getLista(self):
        return self.Lista
    
    def llenarMatriz1(self):
        self.N = 1

        for I in range(0, len(self.Lista)):

            for J in range(0, len(self.Lista[I])):
                
                self.Lista[I][J] = self.N
                self.N += 1
    
    def llenarMatriz2(self, N):
        self.N = N
        for I in range(0, len(self.Lista)):

            for J in range(0, len(self.Lista[I])):
                
                self.Lista[I][J] = self.N
                self.N -= 1
    
    def llenarMatriz3(self, N):
        self.LNum = []
        self.N = N
        for I in range(1,N+1):
            self.LNum.append(I)
        print(self.LNum)

        N = self.LNum[0]

        for I in range(0, len(self.Lista)):
            
            for J in range(0,len(self.Lista[I])):
                
                self.Lista[I][J] = N

                if (I == 1) and (J <= 1):
                    if J == 1:
                        X = len(self.LNum) - 1
                        self.Lista[I][J] = X

                    if J == 0 :
                        X = len(self.LNum) - 2
                        self.Lista[I][J] = X

                elif (I == 2) and (J <= 1):
                    if J == 1:
                        X = len(self.LNum)
                        self.Lista[I][J] = X

                    if J == 0 :
                        X = len(self.LNum) - 3
                        self.Lista[I][J] = X
                elif (I == 3) and (J<= 1):
                    if J == 1:
                        X = len(self.LNum) - 5
                        self.Lista[I][J] = X

                    if J == 0 :
                        X = len(self.LNum) - 4
                        self.Lista[I][J] = X
                    
                else:
                    N += 1



    def ImprimirMatriz(self):

        for M in range(0,len(self.Lista)):
            print(self.Lista[M])
            

