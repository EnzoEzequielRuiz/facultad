#Hacer una programa que, dada una palabra, la escriba recuadrada por asteriscos. Por ejempleo, si la palabra es "Ganaste", el programa debería escribir:

#***********
#* Ganaste *
#***********

palabra = input('Escriba una palabra para encuadrarla: ')
size_palabra = len(palabra)
print('*'*(size_palabra+4))
print(f'* {palabra} *')
print('*'*(size_palabra+4))