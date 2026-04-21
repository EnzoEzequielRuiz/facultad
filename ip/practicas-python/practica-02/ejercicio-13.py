'''
Escribir un programa que pida al usuario dos enteros y que luego muestre si el primero es
mayor que el segundo o viceversa.
'''

num1 = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese otro numero: '))

if num1 > num2:
    print(f'{num1} es mayor que {num2}')
elif num1 < num2:
    print(f'{num2} es mayor que {num1}')
else:
    print(f'{num1} y {num2} son iguales.')