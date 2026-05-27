#a) Escribir un programa que permita al usuario elegir un número 'm' y un 'n' y muestre todos los pares de numeros que se pueden formar con los números que están entre ellos. Por ej. si el usuario ingresara 4 y 6, el programa deberá mostrar:

#4 4
#4 5
#4 6
#5 4
#5 5
#5 6
#6 4
#6 5
#6 6

#b) Cambiar el programa para que use sólo un ciclo en vez de dos.

m = int(input("Ingrese un valor para m: "))
n = int(input("Ingrese un valor para n: "))

for i in range(m,n+1):
    for j in range(m,n+1):
        print(i,j)