'''
Escribir un programa que pida al usuario tres enteros y los guarde en tres variables a, b y c.
El programa deberá luego hacer que en la variable a quede el menor de los valores recibidos, en
b el intermedio y en c el mayor (es decir, ordenará los valores).
'''

num1 = int(input('Introduce el primer valor: '))
num2 = int(input('Introduce el segundo valor: '))
num3 = int(input('Introduce el tercer valor: '))
aux_1 = 0
aux_2 = 0

if num1 > num2 and num1 > num3:
    #3   2   1
    print(f'Mayor a menor: {num1},{num2},{num3}')

elif num1 > num2 and num2 < num3:
    #3   1   2
    aux_1 = num2
    num2 = num3
    num3 = aux_1
    print(f'Mayor a menor: {num1},{num2},{num3}')

elif num1 > num2 and num1 < num3:
    #2   1   3
    aux_1 = num1
    num1 = num3
    aux_2 = num2
    num2 = aux_1
    num3 = aux_2
    print(f'Mayor a menor: {num1},{num2},{num3}')

elif num1 < num2 and num1 > num3:
    #2   3   1
    aux_1 = num1
    num1 = num2
    aux_2 = num2
    num2 = aux_1
    num3 = num2
    print(f'Mayor a menor: {num1},{num2},{num3}')

elif num1 < num2 and num2 < num3: 
    #1   2   3
    aux_1 = num1
    num1 = num3
    aux_2 = num3
    num3 = aux_1
    print(f'Mayor a menor: {num1},{num2},{num3}')

elif num1 < num2 and num2 > num3 and num3 > num1:
    #1   10   5
    aux_1 = num1
    num1 = num2
    aux_2 = num3
    num3 = num2
    num2 = aux_2
    print(f'Mayor a menor: {num1},{num2},{num3}')

else:
    print('2 o 3 valores son iguales.')


