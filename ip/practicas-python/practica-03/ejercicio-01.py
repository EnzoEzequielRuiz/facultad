#a) Hacer unprograma que muestre, mediante un ciclo, los primeros 5 números naturales (1, 2,3,4 y 5).

#b) Hacer un programa que permita al usuario elegir un número n y luego muestre los primeros n números naturales (1,2,··· ,n).

#a
for i in range(1,6):
    print(i)

#b
n = int(input('Ingrese un numero: '))
for i in range(1,n+1):
    print(i)