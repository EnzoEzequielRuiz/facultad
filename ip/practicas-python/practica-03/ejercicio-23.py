#Hacer un programa que permita al usuario jugar al piedra, papel o tijera contra la computadora. Se debe jugar al mejor de 5, es decir, si uno de los participantes consigue 3 victorias el juego termina.

#PIEDRA PAPEL o TIJERAS
import random

#Puntos
bot = 0
tu = 0


#1. Piedra | 2. Papel | 3. Tijeras
for i in range(1,4):
    p_p_t = random.randint(1,3)
    #Reasignar el valor de n, para cambiar entre piedra, papel o tijeras.
    print('###########################')
    n = int(input('Introduce que desea elejir:\n-1. Piedra\n-2. Papel\n-3 Tijeras\n-> '))
    print('###########################')

    #Condicionales
    if p_p_t == 1:
        
        print('----------------------------------')
        print(f'Bot {bot} vs Tu {tu}')
        print('Bot eligio, Piedra')
        
        if n == 1:
            print('Tu elijiste Piedra es un Empate.')
            print('----------------------------------')
            print(f'Bot {bot} vs Tu {tu}')
        
        elif n == 2:
            print('Elijiste Papel, Ganaste')
            print('----------------------------------')
            tu += 1
            print(f'Bot {bot} vs Tu {tu}')
        
        else:
            print('Elijiste Tijeras, Perdiste.')
            print('----------------------------------')
            bot += 1
            print(f'Bot {bot} vs Tu {tu}')

    elif p_p_t == 2:
        print('----------------------------------')
        print(f'Bot {bot} vs Tu {tu}')
        print('Bot jugo, Papel')
        if n == 1:
            print('Elijiste Piedra, Perdiste.')
            print('----------------------------------')
            bot += 1
            print(f'Bot {bot} vs Tu {tu}')

        elif n == 2:
            print('Elijiste Papel es un Empate.')
            print('----------------------------------')
            print(f'Bot {bot} vs Tu {tu}')

        else:
            print('Elijiste Tijeras, Ganaste.')
            print('----------------------------------')
            tu += 1
            print(f'Bot {bot} vs Tu {tu}')

    elif p_p_t == 3:
        print('----------------------------------')
        print(f'Bot {bot} vs Tu {tu}')
        print('Bot eligio, Tijeras.')
        if n == 1:
            print('Tu elijiste Piedra, Ganaste.')
            print('----------------------------------')
            tu += 1
            print(f'Bot {bot} vs Tu {tu}')

        elif n == 2:
            print('Tu elijiste Papel, Perdiste.')
            print('----------------------------------')
            bot += 1
            print(f'Bot {bot} vs Tu {tu}')

        else:
            print('Tu elijiste Tijeras es un Empate.')
            print('----------------------------------')
            print(f'Bot {bot} vs Tu {tu}')

print('Fin del juego.\n----------------------------------')

#Declaracion del ganador
if bot > tu:
    print(f'Bot ganador {bot} a {tu}.')
elif tu > bot:
    print(f'Tu ganaste {tu} a {bot}')
else:
    print(f'Es un empate!')