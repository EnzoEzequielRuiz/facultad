#a) Sabiendo que la pantalla de la consola tiene 80 caracteres de ancho, hacer un programa que, dada una palabra, la escriba en el centro de la pantalla.

palabra = input('Escribe una palabra: ')
size = len(palabra) // 2
print(' ' * (40 - size),palabra,' ' * (40 - size))

#b) Hacer una programa que, dada una palabra, la escriba pegada a la derecha de la pantalla.

palabra = input('Escribe una palabra: ')
size = len(palabra) // 2
print(' ' * (80 - size),palabra)