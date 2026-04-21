'''
Hacer en pseudo codigo y luego un programa que calcule el importe que se le facturará a un cliente por consumo de electricidad sabiendo que la compañía que se la provee cobra una tarifa fija de 980 pesos que incluye los primeros 200 KW consumidos y los KW excedentes se los cobra a 255 pesos el KW, además se agregan $780 de impuestos. Se leen los valores del medidor al comienzo y al fin del período.
'''

kw_consumidos = int(input('Ingrese los kw consumidos: '))

tarifa_fija = 980
exedente = 255

if kw_consumidos > 200:
    kw = kw_consumidos - 200
    tarifa = kw * exedente
    print(f'Total ${tarifa_fija + tarifa}')
else:
    print(f'Total ${tarifa_fija}')
