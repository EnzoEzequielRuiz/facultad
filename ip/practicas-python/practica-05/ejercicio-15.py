#Definir una función llamada union que tome dos listas sin repetidos y devuelva una nueva lista que contenga los elementos de ambas listas. Ojo, la lista de retorno debe no tener repetidos.

lista1 = [1,2,3,4,5]
lista2 = [3,4,5,6,7]

lista_sin_repetidos = []

for i in lista1:
    for j in lista2:
        if i not in lista_sin_repetidos:
            lista_sin_repetidos.append(i)
        elif j not in lista_sin_repetidos:
            lista_sin_repetidos.append(j)

print(lista_sin_repetidos)