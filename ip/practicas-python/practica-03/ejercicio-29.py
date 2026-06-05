#Escribir un programa que pida al usuario una cadena e indique si esta posee un diptongo (dos vocales unidas).

palabra = input('Introduce una palabra para saber si es diptongo: ')

#Vocales cerradas
vc_1 = 'ae'
vc_1_1 = 'ea'
vc_2 = 'eo'
vc_2_2 = 'oe'
vc_3 = 'ao'
vc_3_3 = 'oa'

#Vocales abiertas
va_1 = 'iu'
va_2 = 'ui'

if vc_1 in palabra:
    print(f'{palabra} es un diptongo con vocales cerradas.')
elif vc_1_1 in palabra:
    print(f'{palabra} es un diptongo con vocales cerradas.')
elif vc_2 in palabra:
    print(f'{palabra} es un diptongo con vocales cerradas.')
elif vc_2_2 in palabra:
    print(f'{palabra} es un diptongo con vocales cerradas.')
elif vc_3 in palabra:
    print(f'{palabra} es un diptongo con vocales cerradas.')
elif vc_3_3 in palabra:
    print(f'{palabra} es un diptongo con vocales cerradas.')


elif va_1 in palabra:
    print(f'{palabra} es un diptongo con vocales abiertas.')
elif va_2 in palabra:
    print(f'{palabra} es un diptongo con vocales abiertas.')