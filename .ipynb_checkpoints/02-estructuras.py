
# #LISTAS
# numeros = [1,2,3,4,5,6]
# mix_list = ['Hola',3, True, 3.14]

# print(numeros)
# print(mix_list)

# #USANDO EL CONSTRUCTOR LIST CON OTRO ITERABLE
# list_desde_tupla = list((1,'adios', False))
# print(list_desde_tupla)

# #CONSTRUCCION DE LISTA MEDIANTE LA COMPRENSION DE LISTAS
# cuadrados = [x**2 for x in range(10)]
# print(cuadrados)
# print( cuadrados[0] )

# pares = [x for x in range(11) if x%2 == 0]
# print(pares)

# original = [1, 2, 3]
# copia_incorrecta = original

# copia_correcta = list(original)
# copia_copy = original.copy()

# print(copia_incorrecta)
# copia_incorrecta[0] = 99

# print(original)

# print('Esta son las copias correctas:')
# print('Copia correcta: ' + str(copia_correcta))
# print('Copia con copy: ' + str(copia_copy))

numeros = [ 10, 20, 30, 40, 50]
numeros.append(60)
numeros.insert(1, 15)
numeros.remove(30)

suma = 0
for num in numeros:
    suma += num

promedio = suma / len(numeros)

print(numeros)
print(suma)
print(promedio)

