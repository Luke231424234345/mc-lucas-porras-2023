import math

def aproximacion_serie(x, n):
    resultado = 0.0
    error_anterior = 0.0
    
    for i in range(n):
        termino = (-1) ** i * (x ** i) / math.factorial(i)
        resultado += termino
        if i > 0:
            epsilon = abs((resultado - error_anterior) / resultado) * 100
            print(f"Iteración {i}: {resultado:.8f}, εa = {epsilon:.8f}%")
            if epsilon < 0.000001:  
                break
        error_anterior = resultado
    
    return resultado

x = -0.75
n = 100  
resultado = aproximacion_serie(x, n)
print(f"Resultado final: {resultado:.8f}")
