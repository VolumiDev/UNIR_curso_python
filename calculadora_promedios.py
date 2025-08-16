def ingresar_calificaciones():
    materias = []
    notas = []
    totalFlag = True
    while(totalFlag):
        materia = input("Introduce una materia:\n")
        nota_flag = True
        while(nota_flag):
            try:
                nota = float(input("Introduce la nota:\n"))
                if 0 <= nota <= 10:
                    materias.append(materia)
                    notas.append(nota)
                    nota_flag = False; 
                else:
                    print("Nota introducida incorrecta. Valores entre 0 y 10")  
            except ValueError:
                print("Formato de numero incorrecto")
            
        print(f"Notas: {notas}")
        print(f"Materias: {materias}")

        opt_flag = True
        while opt_flag:
            opt = input("Desea introducir más materias (S/N)\n")
            match opt.lower():
                case "n":
                    opt_flag = False
                    totalFlag = False
                case "s":
                    opt_flag = False
                case _:
                    print("Introduce S o N")
    return materias, notas


def calcular_promedio(calificaciones):
    suma = 0
    for cal in calificaciones:
        suma += cal

    return suma / len(calificaciones)


def determinar_estado(calificaciones, umbral=5):
    aprobadas = []
    reprobadas = []
    for i, cal in enumerate(calificaciones):
        if cal < umbral:
            reprobadas.append(i)
        else :
            aprobadas.append(i)

    return reprobadas, aprobadas

def encontrar_extremos(calificaciones):
    maximo = max(calificaciones)
    minimo = min(calificaciones)
    indices_maximos = [ i for i, v in enumerate(calificaciones) if v == maximo ]
    indices_minimos = [ i for i, v in enumerate(calificaciones) if v == minimo ]

    return indices_minimos, indices_maximos

def mostrar_calificaciones(calificaciones, materias):
    for i, mat in enumerate(materias):
        print(f"{mat} ->> {calificaciones[i]}")

def mostrar_estado(materias, indices, mensaje):
    if len(indices) == 0:
        return
    print(mensaje)
    for i in indices:
        print(f"\t{materias[i]}")

def mostrar_min_max(materias, calificaciones, indices, mensaje):
    print(mensaje)
    for i in indices:
        print(f"\t{materias[i]} con un {calificaciones[i]}")


if __name__ == "__main__":
          
    materias, calificaciones = ingresar_calificaciones()
    
    promedio = calcular_promedio(calificaciones)
    reprobadas, aprobadas = determinar_estado(calificaciones)
    minimas, maximas = encontrar_extremos(calificaciones)

    print(f"########## RESUMEN ##########\n")
    mostrar_calificaciones(calificaciones, materias)
    print(f"El promedio de todas las calificaciones es de {calcular_promedio(calificaciones)}")
    # MATERIAS APROBADAS
    mostrar_estado(materias, aprobadas, "Las materias aprobadas son:")
    mostrar_estado(materias, reprobadas, "Las materias suspendidas son:")
    mostrar_min_max(materias, calificaciones, minimas, "Las materias con minima nota son:")
    mostrar_min_max(materias, calificaciones, maximas, "Las materias con maxima nota son:")

    

