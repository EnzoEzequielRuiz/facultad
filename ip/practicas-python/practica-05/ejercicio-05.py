#Definir una función llamada sonDivisores que tome un entero n y una lista de enteros, y devuelva True si los números de la lista son divisores de n

#Lo hice mas divertido xd
import random
n = int(input('Introduce un numero para saber sus divisores: '))
lista_divisores = []

for i in range(11):
    num_random = random.randint(1,5)
    lista_divisores.append(num_random)

for i in range(11):
    if n % i == 0 and i in lista_divisores:
        print(True)
        print(lista_divisores)