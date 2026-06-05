#Hacer una función (no pura) que reciba una palabra y la imprima recuadrada por asteriscos.
#Por ejemplo si la cadena fuera sobrevivir, la función debería imprimir

#  **************
#  * sobrevivir *
#  **************

def decoracion(cadena):
    mas = len(cadena)+4
    print('*'*mas,'\n*',cadena,'*','\n','*'*mas)

cadena = 'sobrevivir'
print(decoracion(cadena))