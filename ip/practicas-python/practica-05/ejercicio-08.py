#Hacer una función que tome una lista de números decimales y devuelva el promedio de los elementos

lista_numeros_decimales = [2.3,1.4,5.2,1.33,3.1]
acum = 0

for i in lista_numeros_decimales:
    acum += i

promedio = acum / len(lista_numeros_decimales)

print(promedio)