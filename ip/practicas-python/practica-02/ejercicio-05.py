'''
Escribir en papel un programa que pida una nota y que en el caso de que sea menor a cuatro muestre“Debe recuperar”. Luego pasarlo a Python.
'''

nota = int(input('Ingrese la nota: '))

if nota < 4:
    print('Debes recursar.')
else:
    print('No debes recursar.')
