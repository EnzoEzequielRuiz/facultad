#Hacer un programa que solicite dos cadenas, nombre y apellido y el dni del usuario y arme el legajo de estudiantes de la universidad de la siguiente manera:
#Los 3 primeros números del legajo coinciden con los primeros del dni luego "_", luego las 3 primeras letras del apellido y por ultimo la primera y ultima del nombre. Por ejemplo:

#JavierRodriguez 38946702
#Legajo: 389_rodjr

dni = int(input('Introduce tu DNI: '))
dni = str(dni)
nombre = input('Introduce tu Nombre: ')
apellido = input('Introduce tu Apellido: ')

legajo = ''

cont = 0
for d in dni:
    if cont < 3:
        legajo += d
        cont += 1

legajo += '_'

cont = 0
for a in apellido:
    if cont < 3:
        legajo += a
        cont += 1

cont = 0
for n in nombre:
    if n == nombre[0]:
        legajo += n
    elif n == nombre[-1]:
        legajo += n

print(legajo)

