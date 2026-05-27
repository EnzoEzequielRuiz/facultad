#Hacer un programa que simule el juego de la quiniela. El usuario debe elegir un número del 0 al 99 y un monto a apostar, si acierta el número gana 70 veces lo apostado. (El número de la suerte debe ser elegido al azar)
import random

num_usuario = int(input('Ingrese un numero para apostar del 0 al 99: '))
monto_apostado = float(input('Ingrese el monto que desea apostar: $'))

quinela = random.randint(0,99)

if num_usuario >= 0 and num_usuario <= 99:
    
    paso = True
    
    
    while paso:
        if quinela == num_usuario:
            monto_apostado *= 70
            print(f'Felicitaciones Ganaste!, ${monto_apostado} y su numero de la suerte: {quinela}')
            paso = False
        else:
           print('Suerte para la proxima.')
           num_usuario = int(input('Ingrese un numero para apostar del 0 al 99: ')) 
    
    


else:
    print('Elija un numero del 0 al 99.')