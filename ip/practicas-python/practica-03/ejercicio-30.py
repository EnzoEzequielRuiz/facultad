#Escribir un programa que pida al usuario una cadena y una letra y reemplace las apariciones de dicha letra por asteriscos. Por ejemplo, si el usuario ingresa:
#"programador"
#"r"
#el programa debe devolver "p ∗ og ∗ amado∗"

palabra = input('Introduce una palabra: ')
letra = input('Introduce una letra: ')
palabra_modificada = ''

for i in palabra:
    if i == letra:
        palabra_modificada += '*'
    else:
        palabra_modificada += i

print(palabra_modificada)

