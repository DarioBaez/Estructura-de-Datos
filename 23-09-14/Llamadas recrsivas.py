def jugar(intento = 1):
    respuesta = input("De que color es una naranja? ")

    if respuesta != "Naranja":
        if intento < 3:
            print("Fallaste, Intentalo de nuevo")
            intento += 1
            jugar(intento)    #<-- ESTA ES LA LLAMADA RECURSIVA QUE EJECUTARA SU PROPIA FUNCION

        else:
            print("PERDISTE")
    else:
        print("GANASTE")

jugar()