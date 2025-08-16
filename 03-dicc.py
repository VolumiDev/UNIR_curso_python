# Caché para la secuencia de Fibonacci
cache_fibonacci = {}

def fibonacci(n):
    # Si ya calculamos este valor, lo devolvemos directamente
    if n in cache_fibonacci:
        return cache_fibonacci[n]
    
    # Calculamos el valor para n
    if n <= 1:
        resultado = n
    else:
        resultado = fibonacci(n-1) + fibonacci(n-2)
    
    # Guardamos en caché antes de devolver
    cache_fibonacci[n] = resultado
    return resultado

# Ahora las llamadas repetidas son instantáneas
print(fibonacci(30))  # Rápido incluso para valores grandes