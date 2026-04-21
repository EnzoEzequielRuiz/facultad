'''
Se desea escribir un programa que pida al usuario tres números y luego muestre el mayor de
ellos. Escribir el programa en papel, realizar 3 pruebas de escritorio y luego pasarlo a Python y
verificar los resutlados.
'''
a = int(input('Ingrese el valor de A: '))
b = int(input('Ingrese el valor de B: '))
c = int(input('Ingrese el valor de C: '))

if a > b and a > c:
    print(f'El mayor de todos es {a}')
elif b > a and b > c:
    print(f'El mayor de todos es {b}')
elif c > a and c > b:
    print(f'El mayor de todos es {c}')
elif a == b and a > c:
    print(f'Dos numeros son iguales y mayores {a} y {b}')
elif a == c and a > b:
    print(f'Dos numeros son iguales y mayores {a} y {c}')
elif b == c and b > a:
    print(f'Dos numeros son iguales y mayores {b} y {c}')
else:
    print(f'Todos son iguales {a},{b} y {c}')