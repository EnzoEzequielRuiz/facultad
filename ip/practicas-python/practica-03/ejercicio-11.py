#a) Hacer un programa que permita al usuario elegir un número positivo n y luego muestre en pantalla todos los divisores de n.
print('-----------------------------------')
n = int(input('Ingrese un numero positivo, para saber sus divisores: '))
if n > 0:
    print(f'Los divisores de {n} son:')
    for i in range(1,n+1):
        if n % i == 0:
            print(f'-> {i}')
else:
    print('Ingrese un valor mayor a 0.')


#b) Hacer un programa que permita al usuario elegir un número positivo n y luego muestre en pantalla todos los divisores pares de n.
print('-----------------------------------')
if n > 0:
    print(f'Los divisores pares de {n} son:')
    for i in range(1,n+1):
        if n % i == 0 and i % 2 == 0:
            print(f'-> {i}')
else:
    print('Ingrese un valor mayor a 0.')


#c) Hacer un programa que permita al usuario elegir un número positivo n y luego muestre en pantalla la cantidad de divisores de n.
print('-----------------------------------')
acumulador = 0
if n > 0:
    for i in range(1,n+1):
        if n % i == 0:
            acumulador += 1
else:
    print('Ingrese un valor mayor a 0.')
print(f'La cantidad de divisores de {n} son: {acumulador}')

#d) Hacer un programa que permita al usuario elegir un número positivo n y luego muestre en pantalla la suma de los divisores de n.
print('-----------------------------------')
acumulador = 0
if n > 0:
    for i in range(1,n+1):
        if n % i == 0:
            acumulador += i
else:
    print('Ingrese un valor mayor a 0.')
print(f'La suma de los divisores de {n} son: {acumulador}')

#e)  Hacer un programa que permita al usuario elegir dos números positivos c y n y luego muestre en pantalla los primeros c divisores de n.
print('-----------------------------------')
c = int(input('Ingrese el otro numero: '))
print(f'Dividendo {n}')
print(f'Divisor {c}')
if n > 0:
    print(f'Los primero {c} divisores de {n} son:')
    acumulador = 0
    for i in range(1,n+1):
        if n % i == 0 and acumulador < c:
            print(f'-> {i}')
            acumulador += 1
else:
    print('Ingrese un mayor a 0 del divisor o dividendo.')

#f)  Hacer un programa que permita al usuario elegir dos números positivos c y n y luego muestre en pantalla los últimos c divisores de n.
print('-----------------------------------')
print(f'Dividendo {n}')
print(f'Divisor {c}')
if n > 0:
    print(f'Los ultimos {c} divisores de {n} son:')
    acumulador = 0
    for i in range(n+1,1,-1):
        if n % i == 0 and acumulador < c:
            print(f'-> {i}')
            acumulador += 1
else:
    print('Ingrese un mayor a 0 del divisor o dividendo.')
print('-----------------------------------')