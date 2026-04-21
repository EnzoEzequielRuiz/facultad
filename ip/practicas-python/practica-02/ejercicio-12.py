'''
Un profesor clasifica las notas de sus alumnos de la siguiente manera:

    -1-3 Reprobado
    -4-6 Debe rendir examen final
    -7-10 Eximido

a) Escribir un programa que indique la clasificación de una nota.

b) Escribir un programa que pida 3 notas, calcule el promedio e indique la clasificación del mismo.
'''

nota1 = int(input('Primera nota: '))
nota2 = int(input('Segunda nota: '))
nota3 = int(input('Tercera nota: '))

promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 1 and promedio <= 3:
    print(f'Su promedio es {promedio} y queda Reprobado.')
elif promedio >= 4 and promedio <= 6:
    print(f'Su promedio {promedio} y debe rendir un examen final.')
elif promedio >= 7 and promedio <= 10:
    print(f'Su promedio final es {promedio} y queda EXIMIDO!, Felicitaciones.')
else:
    print(f'Escribe las notas del del 1 al 10: ({nota1},{nota2},{nota3})')
