from collections import Counter 


def analizar_texto(cadena):
    total_caracteres = len(cadena)
    total_sin_espacios = len(cadena.replace(" ", ""))

    cadena_sin_espacios = cadena.replace(" ", "")
    contador = Counter(cadena_sin_espacios)
    mas_comunes = contador.most_common(3)

    return{
        "caracteres_mas_comunes": mas_comunes,
        "total_caracteres": total_caracteres,
        "total_sin_espacios": total_sin_espacios
    }

print(analizar_texto("tralara que mas dara"))
