#Hacer un programa que permita al usuario elegir un número positivo n y luego muestre en pantalla el producto (es decir, la multiplicación) de los numeros entre 1 y n.

n = int(input('Ingrese un numero: '))
for i in range(1,n+1):
    print(f'Producto {i * n}')