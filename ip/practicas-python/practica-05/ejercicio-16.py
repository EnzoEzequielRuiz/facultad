#Definir una función llamada diferencia que tome dos listas sin repetidos y devuelva una nueva lista que contenga los elementos la primera que no estén en la segunda.

lista1 = [7,8,5,9,4]
lista2 = [3,4,5,6,7]

lista_sin_repetidos = []

for i in lista1:
    if i not in lista2:
        lista_sin_repetidos.append(i)
print(lista_sin_repetidos)