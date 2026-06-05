#Definir una función llamada divisores que tome un entero y devuelva la lista de divisores de ese entero.

entero = int(input('Introduce un numero para saber sus divisores: '))
lista_divisores = []

for i in range(1,entero+1):
    if entero % i == 0:
        lista_divisores.append(i)
print(lista_divisores)