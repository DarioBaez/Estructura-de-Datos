def factorial (fact):
    if fact > 0:
        Valor = fact * factorial(fact - 1)
        return Valor
    else:
        return 1;

print(f"El factorial de 7 es {factorial(2)}")