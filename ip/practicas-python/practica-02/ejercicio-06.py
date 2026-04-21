'''
a) Escribir en papel un programa que pida al usuario dos números, y que muestre en pantalla al mayor de ambos. Luego hacer 3 corridas de escritorio, luego pasarlo a Python y por último correr el programa con los valores iniciales de las corridas y verificar que funciona como se esperaba.

b) Ídem anterior pero para encontrar el menor
'''
a = float(input('Ingrese un numero: '))
b = float(input('Ingrese otro numero: '))

if a > b:
    print(f'El mayor de ambos es, {a}')
else:
    print(f'El mayor de ambos es, {b}')

if a < b:
    print(f'El menor de ambos es, {a}')
else:
    print(f'El menor de ambos es, {b}')



