#¿Para qué números enteros distintos de cero es cierto que A + B + C = A x B x C ? (lo curioso es que sólo hay una solución)
'''print('Introducir 3 valores distintos.')
a = int(input('Introduce un valor para A: '))
b = int(input('Introduce un valor para B: '))
c = int(input('Introduce un valor para C: '))

if a != b and a != c and b != c:
    for i in range(1,10):
        if '''

for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            suma = a + b + c
            multp = a * b * c
            if suma == multp:
                print(f'La unica combinacion posible para que sea correcta, A + B + C y tambien A * B * C es: {a,b,c} = {suma}')