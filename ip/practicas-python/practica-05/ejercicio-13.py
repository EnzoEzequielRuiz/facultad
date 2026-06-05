#Escribir una función llamada frecuencia que tome una lista de enteros s y otro entero n como parametros y devuelva la cantidad de veces que aparece n en s

s = [1,2,2,3,4,5,2]
n = int(input('Valor de N: '))
acum = 0

for i in s:
    if i == n:
        acum += 1

print(f'{n} aparecio {acum} veces en la lista.')