#¿Es verdad que las únicas soluciones de x^(x+2)(x+3) = 1 son x = 1 x = −2 y x = −3?. 
# Hacer un programa que encuentre todas las soluciones de una o dos cifras tanto negativas como positivas.

for x in range(-99,100):
    exp = (x+2)*(x+3)
    pot = x**exp

    if pot > 0.999 and pot < 1.001:
        print(f'{x} es solucion.\n')
