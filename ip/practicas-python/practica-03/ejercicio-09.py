#Hacer un programa que solicite un número x, en caso de ser par se realiza x/2 y en caso contrario 3x + 1 y repite el procedimiento hasta obtener el número 1. El programa debe indicar cuantas veces se tuvo que realizar el procedimiento. Por ejemplo, si se ingresa el número 10 el programa devuelve 6, porque 10 es par entonces lo divide por 2 y da 5, como es impar lo multiplica por 3 y le suma 1 obteniendo 16. Luego da 8, 4, 2 y 1. Otro ejemplo, si se ingresa 27 debe devolver 111.

x = int(input('Introduce un numero: '))
acumulador = x
contador = 0

while acumulador != 1:
    if acumulador % 2 == 0:
        acumulador = (acumulador / 2)
        contador += 1
    else:
        acumulador = (3 * acumulador + 1)
        contador += 1

print(f'Ingresaste {x}, y cantidad de procedimiento hasta llegar a {acumulador} es {contador}.')



