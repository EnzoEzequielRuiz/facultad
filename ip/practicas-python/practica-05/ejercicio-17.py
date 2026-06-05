#Definir una función llamada mcd que tome dos enteros positivos y devuelva el máximo común divisor usando funciones de los ejercicios anteriores.

a = int(input('Introduce un numero para saber su MCD: '))
b = int(input('Introduce otro numero para saber su MCD: '))

div_a = []
div_b = []

for i in range(1,a):
    if a % i == 0:
        div_a.append(i)

for j in range(1,b):
    if b % j == 0:
        div_b.append(j)
        
for i in div_a:
    mcd = 0   
    for j in div_b:
        if i == j:
            mcd = i

print(f'El Mayor Comun Divisor de {a} y {b} es {mcd}')