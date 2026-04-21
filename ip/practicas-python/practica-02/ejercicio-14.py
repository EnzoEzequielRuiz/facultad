'''
Escribir un programa que pida al usuario dos enteros y los guarde en dos variables. Si el
primero de los valores fuera menor que el segundo, el programa deberá además intercambiar los
valores de las variables y mostrarlos de mayor a menor.
'''

num1 = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese otro numero: '))
aux = 0

if num1 > num2:
    print(f'{num1} es mayor que {num2}')
elif num1 < num2:
    aux = num1
    num1 = num2
    num2 = aux
    print(f'{num1} es mayor que {num2}')
else:
    print(f'{num1} es igual a {num2}')