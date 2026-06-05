#Hacer un programa que dada una palabra y una letra, imprima la cantidad de apariciones de esa letra.

palabra = input('Introduce una palabra: ')
letra = input('Introduce una letra: ')
contador = 0

for i in palabra:
    if letra == i:
        contador += 1

print(f'La cantidad de apariciones {letra} en {palabra} es: {contador}')