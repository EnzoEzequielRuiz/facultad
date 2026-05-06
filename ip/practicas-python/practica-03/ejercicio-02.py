#a) Hacer un programa que muestre, mediante un ciclo, los números desde el 4 hasta el 7 (4,5,6 y 7).

#b) Hacer un programa que permita al usuario elegir un número m y un n y luego muestre todos los naturales entre m y n (m,m+1,m+2,··· ,n−1,n). ¿Qué pasa si n es menor que m?

#a
for i in range(3,8):
    print(i)

#b
m = int(input('Introduce un numero: '))
n = int(input('Introduce otro numero: '))

if n >= 0:
    if m < n:
        for i in range(m,n+1):
            print(i)
    else:
        print(f'{m}, debe ser menor a {n}')
else:
    print('Introduce un numero mayor a 0 para n')