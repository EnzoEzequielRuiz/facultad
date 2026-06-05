#Definir una función llamada interseccion que tome dos listas sin repetidos y devuelva una nueva lista que contenga sólamente aquellos elementos que estén ambas listas.

lista1 = [1,23,41,22,2,8,12,26]
lista2 = [4,27,21,23,6,7,41,13]

lista_nueva = []

for i in lista1:
    for j in lista2:
        if i == j:
            lista_nueva.append(i)

print(lista_nueva)