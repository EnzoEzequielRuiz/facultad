#a) Escribir una función que tome un parámetro de tipo entero y devuelva la cantidad de divisores positivos de ese número.

def divisores(num1):
    acum = 0
    for i in range(1,num1+1):
        if num1 % i == 0:
            acum += 1
    return acum

#b) Escribir una función que tome un parámetro de tipo entero y devuelva el valor True si se la llama con un número primo y False en caso contrario.

def es_primo(num1):
    verif = False
    for i in range(2,num1):
        if num1 % i == 0:
            return False
        return True

#c) ¿Cuál es el número primo más grande que encontraste?

#d) Hacer una función (no pura) que reciba un entero e imprima sus factores primos. Por ejemplo para a = 20 la función debe mostrar 2 y 5.

#Nota: Los números primos son aquellos cuyos únicos divisores positivos son ellos mismos y el 1.

