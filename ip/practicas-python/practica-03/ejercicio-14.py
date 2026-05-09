#a) Hacer un programa que permita al usuario elegir un número positivo n y luego muestre en pantalla los n primeros términos de la sucesión an = 2n. Es decir 2, 4, 6...

n = int(input('Introduce un numero: '))
for i in range(1,n+1):
    print(f'an = 2n ({2*i})')
print('----------------')

#b) Idem anterior para la sucesión an = 2n − 1.

for i in range(1,n+1):
    print(f'2n - 1 ({(2*i) - 1})')
print('----------------')

#c) Idem anterior para la sucesión an = n^2.

for i in range(1,n+1):
    print(f'an = n^2 ({i**2})')
print('----------------')

#d) Idem anterior para la sucesión an = n^3 − n^2.

for i in range(1,n+1):
    print(f'an = n^3 - n^2 ({(i**3) - (i**2)})')
print('----------------')

#e) Idem anterior para la sucesión an = 1/n^2 .

for i in range(1,n+1):
    print(f'an = 1/n^2 ({1 / (i**2)})')
print('----------------')