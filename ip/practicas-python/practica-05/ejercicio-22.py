#Escribir un programa que pida al usuario una cadena, y luego escriba en pantalla la cantidad de veces que aparece cada letra (sin mostrar las que no aparecen). Ej
#Palabra ingresada: "conocido"

#c : 2
#o : 3
#n : 1
#i : 1
#d : 1

cadena = input('Introduce una palabra: ')
nueva_cadena = []




#Sacar letras repetidas
for carac in cadena:
    if carac not in nueva_cadena:
        nueva_cadena.append(carac)

#Contar apariciones
for i in nueva_cadena:
    acum = 0
    for j in cadena:
        if i == j:
            acum += 1
    print(f'{i} : {acum}')

