from Pila7sep23 import Pila
def calculadora_polaca(elementos):
    p = Pila()
    for I in elementos:
        print("Debug:", I)
        try:
            numero = float(I)
            p.apilar(numero)
            print("Debug: apila ", numero)
        except ValueError:
            if I not in "+-*/%" or len(I) != 1:
                raise ValueError("Operando invalido")
            
            try:
                al = p.desapilar()
                print("Debug: desapila ", al)
                
                a2 = p.desapilar()
                print("Debug: desapila ", a2)

            except ValueError:
                print("Debug: error pila faltan operandos")
                raise ValueError("Faltan operandos")
            
            if I == "+":
                resultado = a2 + al
            elif I == "-":
                resultado = a2 - al
            elif I == "*":
                resultado = a2 * al
            elif I == "/":
                resultado = a2 / al
            elif I == "%":
                resultado = a2 % al
            print("Debug: apila ", resultado)
            p.apilar(resultado)

            res = p.desapilar()
            if p.es_vacia():
                return res
            else: 
                print("Debug: error pila sobran operandos")
                raise ValueError("Sobran operandos")

def Main():
    expresion = input("Ingrese la expresion a evaluar: ")
    elementos = expresion.split()
    print(calculadora_polaca(elementos))    
Main()
