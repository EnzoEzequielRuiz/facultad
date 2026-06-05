#Definir una función que tome una lista de números s y un número decimal x y cambie todos los elementos menores que x por 0. Ej: Para

s = [1, 4.1, 6.3, 2, 3.2, 8]
x = 3

#el la lista debe pasar a ser:
#s = [0, 4.1, 6.3, 0, 3.2, 8]

def menores_a_cero(list_num,decimal):
    nueva_lista = list_num
    for i in range(len(list_num)):
        if list_num[i] < decimal:
            list_num[i] = 0
    return nueva_lista

print(menores_a_cero(s,x))