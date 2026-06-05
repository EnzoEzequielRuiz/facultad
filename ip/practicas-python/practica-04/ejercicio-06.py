#a) Escribir una función con el siguiente encabezado: def exclamar(unaCadena): que retorne la misma cadena entre símbolos de exclamación (¡!)

#b) Escribir una función con el siguiente encabezado: def gritar(unaCadena): que retorne la misma cadena entre 3 símbolos de exclamación (¡¡¡!!!)

#c) De no haberlo hecho en el punto anterior, escribir de nuevo la función gritar utilizando solo la función exclamar.

#Nota: gritar(“Ouch”) deberá devolver la cadena “¡¡¡Ouch!!!”
#Ayuda: Recordar que + utilizado entre cadenas las concatena.

def exclamar(unaCadena):
    nueva_cadena = '¡' + unaCadena + '!'
    return nueva_cadena

def gritar(unaCadena):
    nueva_cadena = '¡¡¡' + unaCadena + '!!!'
    return nueva_cadena

cadena1 = 'Ouch'
cadena2 = 'AHHHHHHHHHHHHH'
print(exclamar(cadena1))
print(gritar(cadena2))