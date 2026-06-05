#Modificar el programa del ejercicio anterior para que muestre visualmente los resultados, repitiendo asteriscos. Ej: Palabra ingresada: "conocido"
#c : **
#o : ***
#n : *
#i : *
#d : *

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
    print(f'{i} : {'*'*acum}')