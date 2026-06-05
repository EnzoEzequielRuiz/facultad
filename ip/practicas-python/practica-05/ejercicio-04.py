#Definir una función llamada laMasCorta que tome dos listas y devuelva la que tenga menos elementos. Si tienen igual cantidad, deberá devolver la primera.

lista1 = [1,2,3,4,5]
lista2 = [1,2,3]

if lista1 > lista2:
    print(f'La lista mas corta es {lista2}')
elif lista1 < lista2:
    print(f'La lista mas corta es: lista {lista1}')
else:
    print(f'Las lista son iguales: {lista1}')