#EJERCICIO 18
'''
Escribir un programa en Python que pida al usuario una cantidad de segundos y muestre en pantalla la cantidad de días, minutos y segundos que representa. Por ejemplo, si el usuario ingresa 86461 segundos el programa debe mostrar por pantalla: 1 día 0 horas 1 minuto 1 segundo.'''
tiempo = 86461

s = 1
m = 60 * s
hs = 60 * m
dia = 24 * hs

t1 = tiempo // dia
t1_1 = tiempo % dia

t2 = t1_1 // hs
t2_1 = t1_1 % hs

t3 = t2_1 // m
t3_1 = t2_1 % m

t4 = t3_1 // s

print('Cantidad de tiempo ingresado:',tiempo,'\n -Total:',t1,'dia,',t2,'hora,',t3,'minutos,',t4,'segundos')