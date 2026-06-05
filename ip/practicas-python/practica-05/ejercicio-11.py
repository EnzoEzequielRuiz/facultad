#Escribir una función llamada maximoEntre que tome una lista de números y dos enteros a y b menores que la longitud de la lista y devuelva el índice del máximo elemento considerando solo los que están entre el índice a y el índice b.

a = int(input('Introduce un valor para A: '))
b = int(input('Introduce un valor para B: '))

lista_numeros = [12,13,8,22,9,1]

for i in range(len(lista_numeros[a:b+1])):
    acum = 0
    for j in lista_numeros[a:b+1]:
        if lista_numeros[i] >= j:
            acum += 1
    if acum == len(lista_numeros)-2:
        print(f'{i} es el indice del mayor de todos.')
