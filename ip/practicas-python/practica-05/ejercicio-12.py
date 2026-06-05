#Escribir una función llamada intercambiar que tome una lista de números s y dos enteros positivos a y b menores que la longitud de la lista y cambie el elemento ubicado en s[a] por el elemento ubicado en s[b]. Ojo, esta función no debe devolver una lista, sino modificar la que toma como parámetro.

a = int(input('Valor para A: '))
b = int(input('Valor para B: '))

s = [2,23,12,6,9,7,18]

auxA = 0
auxB = 0

for i in range(len(s)):
    print(i)
    if i == a:
        auxA = s[i]
    elif i == b:
        auxB = s[i]

s[a] = auxB
s[b] = auxA

print(s)