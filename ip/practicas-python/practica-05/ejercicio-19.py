#Definir una función que tome un entero n y devuelva la lista de los primos que aparecen al factorear n. Ejemplo, para 24, la lista debe ser: [2, 2, 2, 3]

def factorizar_n(n):
    factores = []
    divisor = 2
    
    # Copiamos n para no perder el valor original si fuera necesario
    temp = n
    
    # Un número n no puede tener factores primos mayores a n
    while temp > 1:
        while temp % divisor == 0:
            factores.append(divisor)
            temp //= divisor # División entera para reducir el número
        divisor += 1
        
    return factores

# Ejemplo de uso:
numero = 24
print(f"Los factores primos de {numero} son: {factorizar_n(numero)}")
# Salida: [2, 2, 2, 3]
    
    