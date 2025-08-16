def suma_pares(inicio, fin): 
    suma = sum(numero for numero in range(inicio, fin + 1) if numero % 2 == 0)
    return suma


print(suma_pares(1,10))
        