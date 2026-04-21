'''
Escribir en papel un programa que pida al usuario dos números de punto flotante y muestre supromedio Además, si el promedio es mayor que 7 el programa debe mostrar en pantalla “Aprobado” y sino, debe mostrar“Desaprobado”.Después de hacerlo en papel, pasarlo a Python.
'''

a = float(input('Ingrese el valor de, a:'))
b = float(input('Ingrese el valor de, b:'))

if (a + b) / 2 > 7:
    print(f'Tu nota promedio final es {(a+b)/2}, Aprobaste!')
else: 
    print(f'Tu nota promedio final es {(a+b)/2}, Desaprobaste :c')