suma = 0
contador = 0
flag = True

while suma < 100:
    
    dato = input("Introduce un numero entero y positivo:\n")

    if dato.isdigit() and int(dato) > 0:
        suma += int(dato)
        contador = contador + 1 
        if suma < 100:
            print(f"La suma es: {suma}")
        else:
            break
    else: 
        print(f"Dato incorrecto.\n")
    

print(f"La suma total es de {suma} y se introdujeron {contador} numeros")