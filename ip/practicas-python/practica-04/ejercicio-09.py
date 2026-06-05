#a) Hacer una función que reciba dos enteros y retorne el mayor.

def el_mayor(num1,num2):
    if num1 > num2:
        return num1
    else:
        return num2

#b) Hacer una función que reciba tres enteros y retorne el mayor.

def el_mayor_de_tres(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        return num1
    
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3
    
num1 = 12
num2 = 8
num3 = 23


print(f'El mayor de {num1} y {num2} es: {el_mayor(num1,num2)}')

print(f'El mayor de {num1}, {num2} y {num3} es: {el_mayor_de_tres(num1,num2,num3)}')