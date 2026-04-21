'''
Se tiene la siguiente lista con DNIs depersonas.
    
    -30612453
    -23763290
    -21448503
    -34582048
    -15364857

Dado otro número de DNI cualquiera, se desea construir un programa que determine si es alguno de los existentes en el listado. Escribir el programa en papel y luego pasarlo a Python.
'''

dni = int(input('Ingrese su DNI: '))

dni1, dni2, dni3, dni4, dni5 = 30612453, 23763290, 21448503, 34582048, 15364857

if dni == dni1:
    print(f'El DNI {dni} esta en la lista.')
elif dni == dni2:
    print(f'El DNI {dni} esta en la lista.')
elif dni == dni3:
    print(f'El DNI {dni} esta en la lista.')
elif dni == dni4:
    print(f'El DNI {dni} esta en la lista.')
elif dni == dni5:
    print(f'El DNI {dni} esta en la lista.')
else:
    print('No estas en la lista.')