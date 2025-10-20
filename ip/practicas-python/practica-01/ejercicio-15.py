#EJERCICIO 15
'''
Un vendedor recibe un sueldo base de $42000 más un 10% extra del total de sus ventas, el vendedor desea saber cuánto dinero obtendrá en total en el mes si ha logrado realizar 3 ventas este mes. Tenga en cuenta el sueldo básico y la comisión por las ventas. Hacer un programa que solicite el monto de cada una de las ventas del mes e indique cuál será el sueldo nal del vendedor. Por ejemplo, si realizó una venta de $12000, otra de $6000 y una tercera de $22000 su sueldo será de $46000
'''

sueldo = 42000
comision = 0.10

venta_01 = 12000
venta_02 = 6000
venta_03 = 22000

print('Total ganado $:',((venta_01 + venta_02 + venta_03 ) * comision) + sueldo)
