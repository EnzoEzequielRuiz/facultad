#a) Definir una función que tome una lista de números s y un número decimal x y devuelva la cantidad de elementos de s que sean menores que x.

s = [2,23,12,19,6,8,11]
x = 15.5
nueva_lista = []
for i in s:
    if i <= x:
        nueva_lista.append(i)
print(nueva_lista)

#b) Si se pone como condición que s siempre esté ordenada de mayor a menor, ¿cómo podría modificarse el programa para que haga menos iteraciones?

s = [23,19,12,11,8,6,2]
x = 10.33
nueva_lista = []
for i in s[4:]:
    if i <= x:
        nueva_lista.append(i)
print(nueva_lista)
