#Definir una función que tome un entero n y devuelva los primeros n primos.

n = int(input('Saber sus anteriores primos: '))
cont = 0
primer_numero = 2

#saber si es primo
def es_primo(n):
    if n < 2:
        return False

    for i in range(2,n):
        es_primo = False
        if n % i == 0: #si el resto es 0, encontramos un divisor no es primo
            return False
    return True #Si termino el ciclo sin encontrar divisores, es primo

while cont <= n:
    if es_primo(primer_numero):
        print(primer_numero)
        cont += 1
    primer_numero += 1

    
