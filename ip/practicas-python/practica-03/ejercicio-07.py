#Hacer todos los ejercicios anteriores de nuevo, pero esta vez utilizando la sentencia while en lugar de for. De haberlos hecho con while, rehacerlos utilizando for.

#------------------------------------------------------------------------------------------------------#
#Ejerciccio 1
    #a) Hacer unprograma que muestre, mediante un ciclo, los primeros 5 números naturales (1, 2,3,4 y 5).

    #b) Hacer un programa que permita al usuario elegir un número n y luego muestre los primeros n números naturales (1,2,··· ,n).

#a
print('--------------------------------------')
print('Ejercicio 1, a)')
i = 1
while i <= 5:
    print(i)
    i += 1

#b
print('--------------------------------------')
print('Ejercicio 1, b)')
i = 1
n = int(input('Introduce un numero: '))
while i <= n:
    print(i)
    i += 1
#------------------------------------------------------------------------------------------------------#
#Ejercicio 2
    #a) Hacer un programa que muestre, mediante un ciclo, los números desde el 4 hasta el 7 (4,5,6 y 7).

    #b) Hacer un programa que permita al usuario elegir un número m y un n y luego muestre todos los naturales entre m y n (m,m+1,m+2,··· ,n−1,n). ¿Qué pasa si n es menor que m?

#a
print('--------------------------------------')
print('Ejercicio 2, a)')
i = 4
while i <= 7:
    print(i)
    i += 1

#b
print('--------------------------------------')
print('Ejercicio 2, b)')
m = int(input('Introduce un numero: '))
n = int(input('Introduce otro numero: '))
i = m
while i <= n:
    print(i)
    i += 1
#------------------------------------------------------------------------------------------------------#
#Ejercicio 3
    #a) Hacer un programa que muestre, mediante un ciclo, los 5 números naturales que le siguen al 10 (11,12,··· ,15).

    #b)  Hacer un programa que permita al usuario elegir un número n y luego muestre los 5 números naturales que le siguen a n (n +1,n+2,··· ,n+5).

    #c)  Hacer un programa que permita al usuario elegir un número n y un número c, y luego muestre los c números naturales que le siguen a n (n + 1,n +2,··· ,n+c).

#a
print('--------------------------------------')
print('Ejercicio 3, a)')
i = 10
while i <= 15:
    print(i)
    i += 1

#b
print('--------------------------------------')
print('Ejercicio 3, b)')
n = int(input('Introduce un numero: '))
i = n
while i <= n+5:
    print(i)
    i += 1

#c
print('--------------------------------------')
print('Ejercicio 3, c)')
n = int(input('Introduce un numero: '))
c = int(input('Introduce otro numero: '))
i = n
while i <= n+c:
    print(i)
    i += 1

#------------------------------------------------------------------------------------------------------#
#Ejercicio 4
    #a) Hacer un programa que muestre, mediante un ciclo, los números desde el 5 hasta el 11 salteando de a 2 elementos (5,7,9 y 11)

    #b)  Hacer un programa que permita al usuario elegir un número m y un n y luego muestre todos los naturales entre m y n, pero salteando de a 3. Por ejemplo, si el usuario ingresara un n igual a 2 y un m igual a 14, el programa deberá mostrar 2, 5, 8, 11, 14.

   #c) Hacer un programa que permita al usuario elegir un número n, un m y un p y luego muestre todos los naturales entre m y n, pero salteando de a p números. Por ejemplo, si el usuario ingresara un n igual a 2 y un m igual a 14, y un p igual a 4, el programa deberá mostrar 2, 6, 10, 14.

#a
print('--------------------------------------')
print('Ejercicio 4, a)')
x = 5
z = 11
while x <= z:
    print(x)
    x += 2

#b
print('--------------------------------------')
print('Ejercicio 4, b)')
m = int(input('Introduce un numero: '))
n = int(input('Introduce otro numero: '))
i = m
while i <= n:
    print(i)
    i += 3

#c
print('--------------------------------------')
print('Ejercicio 4, c)')
m = int(input('Introduce un numero: '))
n = int(input('Introduce otro numero: '))
p = int(input('Introduce el ultimo numero: '))
i = m
while i <= n:
    print(i)
    i += p

#------------------------------------------------------------------------------------------------------#
#Ejercicio 5
    #a) Hacer un programa que muestre, mediante un ciclo, los números desde el 8 hasta el 3 (8,7,6,5,4,3).

print('--------------------------------------')
print('Ejercicio 5, a)')
i = 8
while i >= 3:
    print(i)
    i -= 1

#------------------------------------------------------------------------------------------------------#
#Ejercicio 6
    #a) Hacer un programa que muestre, mediante un ciclo, los números desde el 15 hasta el 6 pero salteando de a tres (15,12,9,6).

print('--------------------------------------')
print('Ejercicio 6, a)')
i = 15
while i >= 6:
    print(i)
    i -= 3
print('--------------------------------------')