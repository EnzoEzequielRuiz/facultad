#a) Escribir una función que reciba como parámetro una cadena y la muestre en pantalla 3 veces.

#b) Guardar esta definición de función en un archivo.

#c) Hacer un programa que le pida al usuario una cadena y que la muestre en pantalla 3 veces utilizando la función definida anteriormente.

def cadena_por_tres(cadena):
    return (cadena*3)

cadena = input('Introduce una palabra: ')
print(cadena_por_tres(cadena))