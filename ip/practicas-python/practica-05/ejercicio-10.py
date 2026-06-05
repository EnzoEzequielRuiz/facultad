#Escribir una función llamada maximoIndice que tome una lista de números y devuelva el índice del máximo elemento.

lista_numeros = [12,13,8,22,9,1]

for i in range(len(lista_numeros)):
    acum = 0
    for j in lista_numeros:
        if lista_numeros[i] >= j:
            acum += 1
    if acum == len(lista_numeros):
        print(f'{i} es el indice del mayor de todos.')
