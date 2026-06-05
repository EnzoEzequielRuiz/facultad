#Definir una función llamada dondeAparece que tome una lista de enteros y un entero como parámetros, y devuelva el primer índice donde aparece en la lista, si lo hace, y -1 en caso contrario.

n = int(input('Introduce un numero: '))
lista_enteros = [1,2,3,4,5,6,7,8,9,10]
entero_encontrado = ''

if n in lista_enteros:
    i = 0
    while i <= len(lista_enteros)-1:
        if lista_enteros[i] == n:
            print(i)
        i += 1

else:
    print('-1')