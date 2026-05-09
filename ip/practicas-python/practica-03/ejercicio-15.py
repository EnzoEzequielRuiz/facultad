#a) Hacer un programa que permita al usuario elegir un número positivo n y luego muestre en pantalla las n primeras sumas parciales de la sucesión an = 2n. Es decir, 2 6 12 20...

n = int(input('Introduce un numero: '))
acumulador = 0
for i in range(1,n+1):
    print(f'an = 2n ({2*i})')
    acumulador += 2*i
print(acumulador)
print('----------------')

#b) Idem anterior para la sucesión an = n^2

acumulador = 0
for i in range(1,n+1):
    print(f'an = n^2 ({i**2})')
    acumulador += i**2
print(acumulador)
print('----------------')

#c) Idem anterior para la sucesión an = n^3 − n^2.

acumulador = 0
for i in range(1,n+1):
    print(f'an = n^3 - n^2 ({(i**3) - (i**2)})')
    acumulador += (i**3) - (i**2)
print(acumulador)
print('----------------')

#d) Idem anterior para la sucesión an = 1 / n^2 .

acumulador = 0
for i in range(1,n+1):
    print(f'an = 1 / n^2 ({1 / (i**2)})')
    acumulador += 1 / (i**2)
print(acumulador)
print('----------------')