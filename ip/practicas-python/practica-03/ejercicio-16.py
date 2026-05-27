import math
# El logaritmo natural de 2 (ln(2)) se puede aproximar de la siguiente manera:

    # ln(2) = 1 - 1/2 + 1/3 - 1/4 + 1/5 ...

#a) Escribir un programa que le pregunte al usuario la cantidad de términos a sumar y que muestre la aproximación de ln(2) con esa cantidad de términos.

cant_terminos = int(input('Introduce cuantos terminos desea sumar: '))
acumulador = 0

for i in range(1,cant_terminos+1):
    if i % 2 == 0:
        acumulador -= 1/i
    else:
        acumulador += 1/i
print(f'Aproximacion de ln(2) = {math.log(2)} con {cant_terminos} terminos es {acumulador}')

#b) ¿Apartir de cuántos términos el valor alcanzado está a menos de 0.1 del valor que da la calculadora? En python se puede aproximar este valor usando math.log(2)

acumulador = 0
if acumulador < 0.1:
    while acumulador :
        if i % 2 == 0:
            acumulador -= 1/i
        else:
            acumulador += 1/i
print(f'Aproximacion de ln(2) = {math.log(2)} con {cant_terminos} terminos es {acumulador}')

#c) ¿Apartir de cuántos términos el valor alcanzado está a menos de 0.01 del valor que da la calculadora?

#d) Modificar el programa para que en lugar de pedir la cantidad de términos a sumar, pida al usuario un número decimal ϵ (muy chico y calcule la suma hasta que el error comparado con el valor de la calculadora sea menor que ϵ

