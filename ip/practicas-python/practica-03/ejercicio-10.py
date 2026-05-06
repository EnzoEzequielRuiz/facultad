#a) Hacer un programa que reciba un número n y muestre todas las potencias de 2 menores a n. Por ejemplo, si el usuario ingresa 20, el programa mostrará: 1 2 4 8 16. Ayuda: pensar primero si sería más práctico utilizar la sentencia while o for.

#b) Hacer un programa que reciba un número n (n > 0) y muestre las n primeraspotencias de 2. Por ejemplo, si el usuario ingresa 6, el programa mostrará: 1 2 4 8 16 32.

#c) Hacer un programa que reciba un número n (n > 0) y muestre las n primeras potencias de n. Por ejemplo, si el usuario ingresa 4, el programa mostrará: 1 4 27 256. Es decir, 1^1 2^2 3^3 4^4.

#a
n = int(input('Ingresa un numero: '))
acumulador = 1

while acumulador < n:
    print(acumulador)
    acumulador = (acumulador * 2)

#b
n = int(input('Ingresa un numero: '))
acumulador = 1
if n > 0:
    for i in range(1,n+1):
        print(acumulador)
        acumulador = (acumulador * 2)
else:
    print('Ingrese un numero mayor a 0.')
#c
n = int(input('Ingresa un numero: '))
acumulador = 0
if n > 0:
    for i in range(1,n+1):
        acumulador = (i ** i)
        print(acumulador)
else:
    print('Ingrese un numero mayor a 0.')
