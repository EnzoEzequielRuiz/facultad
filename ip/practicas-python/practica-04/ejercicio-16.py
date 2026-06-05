#El propósito de este ejercicio es tomar el código de un ejercicio anterior y encapsular una parte de él en una función que toma parámetros. Partiendo de la resolución del ejercicio 25 de la práctica de ciclos y cadenas,

#a) escribir una función que tome como parámetros una cadena y una letra, y retorne la cantidad de veces que aparece esa letra en esa cadena.

def cont_letra(cadena,letra):
    cont = 0
    for i in cadena:
        if letra == i:
            cont += 1
    return cont

#b) probarla para asegurarse que funciona bien.

#c) transformar el código del ejercicio 25 para que utilice la nueva función.


#Hacer un programa que dada una palabra y una letra, imprima la cantidad de apariciones de esa letra.

palabra = input('Introduce una palabra: ')
letra = input('Introduce una letra: ')

print(f'La cantidad de apariciones "{letra}" en {palabra} es: {cont_letra(palabra,letra)}')