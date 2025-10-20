#EJERCICIO 16

'''-Determinar cuántos segundos tiene una hora, y cuántos tiene un día.'''
segundos = 1
minutos = 60 * segundos
hora = 60 * minutos
dia = 24 * hora
print('Cantidad de segundos que tiene una hora: ',hora)
print('Cantidad de segundos que tiene un dia: ',dia)

'''-Escribir una expresión matemática que transforme un lapso de tiempo expresado en segundos a uno expresado en minutos.'''
tiempo_en_seg = int(input('Introduce una cantidad de tiempo:'))
s = 1
m = 60 * s
total = tiempo_en_seg // m
print('Total en minutos: ',total)

'''-Escribir otra para transformar a horas y una última que transforme a días.'''
hs = 60 * m
total_02 = tiempo_en_seg // hs
print('Total en horas: ',total_02)

dia = 24 * hs
total_03 = tiempo_en_seg // dia
print('Total en dias: ',total_03)