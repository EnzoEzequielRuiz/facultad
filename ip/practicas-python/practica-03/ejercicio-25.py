#a) Escribir un programa que pida al usuario un número n y muestre una línea de n asteriscos. Ejemplo, para n = 8, el programa deberá mostrar:

#  ********

n = int(input('Ingresa la cantidad de * que desea imprimir: '))
print("*"*n)

#b)  Escribir un programa que pida al usuario un número n y muestre n líneas de 1, 2,3,...n asteriscos respectivamente. Ejemplo, para n = 5, el programa deberá mostrar:

#*
#**
#***
#****
#*****

n = int(input('Ingresa la cantidad de * que desea imprimir: '))
for i in range(n+1):
    print("*"*i)

#c) Escribir un programa que pida al usuario un número n y muestre n líneas de 2*n−1 asteriscos respectivamente. Ejemplo, para n = 5, el programa deberá mostrar:

#*
#***
#*****
#*******
#*********

n = int(input('Ingresa la cantidad de * que desea imprimir: '))
for i in range(n+1):
    print("*"*(2*i-1))