'''
Un año es bisiesto si es múltiplo de 4. Pero no siempre, las excepciones son los años múltiplos
de 100 que no son múltiplos de 400 (1900 no es bisiesto pero 2000, sí). Escribir en papel un
programa que diga si un año ingresado por el usuario es bisiesto, realizar varias pruebas de
escritorio, luego pasarlo a Python y verificar los resutlados.
'''

introduce_el_anio = int(input('Introduce el anio para saber si es biciesto: '))

if introduce_el_anio % 4 == 0:
    #exepciones
    if introduce_el_anio % 100 == 0 and introduce_el_anio % 400 != 0:
        print('No es biciesto.')
    else:
        print('Es biciesto.')
else:
    print('No es biciesto.')