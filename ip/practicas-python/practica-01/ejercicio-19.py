#EJERCICIO 19
'''
Escribir en Python un programa que pida al usuario que ingrese dos valores y los guarde en dos variables, x e y. El programa deberá intercambiar los valores de x e y y luego mostrar en pantalla:

-El valor de x es: <x>
-El valor de y es: <y>

donde en lugar de <x> e <y> deberá mostrarse el valor de las respectivas variables.
'''
x = float(input('Ingrese un valor para x:'))
y = float(input('Ingrese un valor para y:'))

print('-Valor de x:',x,'\n-Valor de y:',y)

aux = x
x = y
y = aux

print('procesando..\nValores intercambiados:\n -Valor de x:',x,'\n -Valor de y:',y)