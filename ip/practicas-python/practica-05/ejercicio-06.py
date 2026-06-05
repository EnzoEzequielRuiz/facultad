#Definir una funcion que tome una lista y devuelva True si tiene al menos un elemento repetido, y False en caso contrario.

lista = [1,2,3,4,5]
lista_repetida = [1,3,3,4,5]

lista_modificada = []
verificacion = ''
for i in lista:
    if i not in lista_modificada:
        verificacion = False
    lista_modificada.append(i)
print(f'La lista {lista} esta repetida?: {verificacion}')

lista_modificada = []
verificacion = ''
for i in lista_repetida:
    if i in lista_modificada:
        verificacion = True
    lista_modificada.append(i)
print(f'La lista {lista_repetida} esta repetida?: {verificacion}')