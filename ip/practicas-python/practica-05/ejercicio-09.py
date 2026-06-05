#Escribir una función llamada maximo que tome una lista de números y devuelva el valor del máximo elemento.

lista_numeros = [12,13,8,22,9,1]

for i in lista_numeros:
    acum = 0
    for j in lista_numeros:
        if i >= j:
            acum += 1
    if acum == len(lista_numeros):
        print(f'{i} es el mayor de todos.')
