#a) Escribir una función que reciba dos números reales como parámetros y retorne su promedio.

#b) Hacer un programa que pida al usuario dos números reales y muestre por pantalla el resultado de llamar a la función del primer inciso.

#c) Idem de los dos anteriores pero con tres números. Escribir la función en el mismo archivo donde se escribió la del item a.

def promedio(num1,num2):
    promedio = (num1 + num2) / 2
    return promedio

def promedio_tres(num1,num2,num3):
    promedio = (num1 + num2 + num3) / 3
    return promedio

a = float(input('Introduce un numero: '))
b = float(input('Introduce otro numero: '))
c = float(input('Introduce otro numero mas: '))

print(promedio(a,b))
print(promedio_tres(a,b,c))