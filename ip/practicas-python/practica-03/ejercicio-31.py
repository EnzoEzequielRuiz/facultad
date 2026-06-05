#Hacer un programa que genere una clave provisoria para la gestión online de clientes de una empresa. El programa le pedirá el apellido y generará una clave de 5 caracteres, tomará las primeras 4 consonantes de la palabra ingresada. Cuando las consonantes no alcancen a 4, las faltantes las reemplazará por "*". Ejemplos:

#clemente CLMN
#rivera RVR
#oreo R***
#La clave se completará con 1 dígito generado aleatoriamente entre 0 y 9.
#Ejemplos: CLMN1 RVR*4 R***7
import random

apellido = input('Introduce tu apellido, para una clave provisoria: ')
vocales = 'aeiou'
clave_provisoria = ''

for i in apellido:
    if i not in vocales and len(clave_provisoria) <= 3:
        clave_provisoria += i

cuatro_consonantes = len(clave_provisoria)
while cuatro_consonantes <= 3:
    clave_provisoria += '*'
    cuatro_consonantes += 1

num_random = random.randint(0,9)
clave_provisoria = clave_provisoria + str(num_random)
print(f'Su clave provisoria es: {clave_provisoria.upper()}')