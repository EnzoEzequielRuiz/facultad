#a) Hacer una función que sume los divisores propios de un número.

def suma_divisores(num1):
    acum = 0
    for i in range(1,num1+1):
        if num1 % i == 0:
            acum += i
    return acum

#b) Hacer una función que indique si un número es perfecto. Número perfecto: A es perfecto si la suma de sus divisores propios es igual a A.

def es_perfecto(num1):
    verif = suma_divisores(num1)
    if verif == num1:
        return ('Es perfecto')
    return ('No es perfecto')

#c) Hacer una función que determine si un número ingresado por el usuario es un número abundante. Número abundante: todo número natural que cumple que la suma de sus divisores propios es mayor que el propio número. Por ejemplo, 12 es abundante ya que sus divisores son 1, 2, 3, 4 y 6 y se cumple que 1+2+3+4+6=16, que es mayor al propio 12.

def es_abundante(num1):
    verif = suma_divisores(num1)
    if verif > num1:
        return ('Es abundante')
    return ('No es abundante')

num1 = 12

print(f'Suma de divisores de {num1} es: {suma_divisores(num1)}')

print(f'{num1} es numero perfecto?: {es_perfecto(num1)}')

print(f'{num1} es numero abundante?: {es_abundante(num1)}')