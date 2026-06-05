#Escribir una función (y probarla en un programa) para cada una de las siguientes descripciones:

#a) una función que se llame tieneRepetidas que tome una cadena como parámetro y devuelva True si esa cadena tiene alguna letra que aparece más de una vez y False en caso contrario.

#def tiene_repetidas(cadena):
cadena = 'eucalipto'
nueva_cadena = ''
cont = 0
for i in cadena:
    print(i)
    print(nueva_cadena)
    print(cont)
    for j in nueva_cadena:
        
        if j in nueva_cadena:
            cont += 1
        nueva_cadena += j
if cont > 1:
    print(True)
else:
    print(False)

#b) una función que se llame aparece que tome dos parámetros, una letra y una cadena, y devuelva True si la letra aparece en la cadena y False en caso contrario.

def aparece(cadena,letra):
    if letra in cadena:
        return True
    else:
        return False

#c) una función que se llame dameRepetida que tome una cadena como parámetro y retorne la primer letra que aparece repetida en la cadena

def dame_repetida(cadena):
    paso = True
    cont = 0
    while paso:
        for i in cadena:
            for j in cadena:
                if i == j:
                    cont += 1
                if cont == 2:
                    paso = False
                    return i

#d) una función que se llame quitarRepeticiones que tome dos parámetros, una cadena y una letra, y devuelva otra cadena igual a la anterior pero sin las repeticiones de esa letra. Por ejemplo, un programa que llame a la función así: quitarRepeticiones(“mate cocido”, “c”), deberá retornar la cadena “mate coido”

def quitar_repeticiones(cadena,letra):
    nueva_cadena = ''
    cont = 0
    for i in cadena:
        if letra == i:
            cont += 1
        elif not cont == 2:
            nueva_cadena += i
    return nueva_cadena


cadena = 'banana'
cadena2 = 'eucalipto'
