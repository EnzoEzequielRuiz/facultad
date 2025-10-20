#EJERCICIO 17
''' 
La empresa que administra los cajeros automáticos lo contrata para que programen la entrega de
billetes, el usuario ingresa la cantidad de dinero que desea y usted debe indicar cuantos billetes de cada denominación se debe entregar. Es importante entregar siempre la menor cantidad de billetes. 

Ayuda: El operador % da el resto de la división a/b, y el operador // da la parte entera del cociente de a/b.'''

dinero = int(input('Ingrese la cantidad de dienro a retirar: '))

d1 = dinero // 20000
d1_1 = dinero % 20000

d2 = d1_1 // 10000
d2_2 = d1_1 % 10000

d3 = d2_2 // 2000
d3_1 = d2_2  % 2000

d4 = d3_1 // 1000
d4_1 = d3_1 % 1000

d5 = d4_1 // 500
d5_1 = d4_1 % 500

d6 = d5_1 // 200
d6_1 = d5_1 % 200

d7 = d6_1 // 100
d7_1 = d6_1 % 100

print('Retirado: $',dinero,'\n -cantidad de billetes de $20.000:',d1,'\n -cantidad de billetes de $10.000:',d2,'\n -cantidad de billetes de $2.000:',d3,'\n -cantidad de billetes de $1.000:',d4,'\n -cantidad de billetes de $500:',d5,'\n -cantidad de billetes de $200:',d6,'\n -cantidad de billetes de $100:',d7,'\n --Resto en cuenta: $',d7_1)