#EJERCICIO 14
'''
Una empresa telefónica desea un programa para calcular el importe de sus clientes. Sabiendo que el costo por comunicación es de $12 y por cada segundo se cobra $1,5 hacer dicho programa. Se deben ingresar la cantidad de llamadas realizadas y el tiempo total de comunicación, el programa debe devolver el precio a cobrar. Por ejemplo, si realizó 10 llamadas con un total de 4000 segundos el importe a pagar sería de $6120
'''

costo_por_comunicacion = 12
costo_por_segundos = 1.5

cantidad_de_llamadas = float(input('Ingrese la cantidad de llamadas: '))
cantidad_de_segundos_total = float(input('Ingresa la cantidad de segundos total de llamadas: '))

print('-Costo por comunicacion: $',costo_por_comunicacion,'\n-Costo por segundos de llamada: $',costo_por_segundos,'\n-Cantidad de llamas realizadas:',cantidad_de_llamadas,'\n-Cantidad de segundos en llamada:',cantidad_de_segundos_total,'\n-Total: $',(costo_por_comunicacion * cantidad_de_llamadas) + (costo_por_segundos * cantidad_de_segundos_total))