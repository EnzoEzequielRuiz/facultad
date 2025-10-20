#EJERCICIO 20
'''
Escribir en Python un programa que pida al usuario que ingrese tres valores y los guarde en tres variables, x, y, y z. El programa deberá intercambiar circularmente los valores de x, y y z, es decir, x debe tomar el valor de y, y el de z y z el de x. Y luego mostrarlos en pantalla:

-El valor de x es: <x>
-El valor de y es: <y>
-El valor de z es: <z>
 
donde en lugar de <x>, <y> y <z> deberá mostrarse el valor de las respectivas variables
'''

x = float(input('Ingrese un valor para x:'))
y = float(input('Ingrese un valor para y:'))
z = float(input('Ingrese un valor para z:'))

print('-Valor de x:',x,'\n-Valor de y:',y,'\n-Valor de z:',z)

aux = x
x = y
y = z
z = aux

print('procesando..\nValores intercambiados:\n -Valor de x:',x,'\n -Valor de y:',y,'\n -Valor de z:',z)