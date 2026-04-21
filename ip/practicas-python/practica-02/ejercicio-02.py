'''
Un ciudadano argentino está exento de votar, puede ir pero no está obligado, en estos casos:
    
    -Tiene más de 70 años
    -Tiene menos de 18 años pero al menos 16 años
    
    -Tiene entre 18 y 70 años pero se encuentra a más de 500 km del centro de votación.
Suponiendo que las variables edad y distancia representan la edad y la distancia del ciuda
dano, escribir la expresión lógica que representa esta situación.
'''

edad = int(input('Introduce tu edad: '))
km = float(input('Introduce la distancia del centro de votacion: '))

if edad >= 18 and edad <= 70:
    if km >= 500:
        print('Estas muy lejos del centro de votacion.')
    else:
        print('Puedes votar.')
else:
    if edad < 18:
        print('Sos muy joven.')
    else:
        print('Sos muy anciano.') 