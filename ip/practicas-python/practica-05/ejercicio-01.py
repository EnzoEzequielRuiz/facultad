#Hacer un programa que guarde la siguiente lista en una variable: [“elefante”, “jirafa”,“mono”], luego pida el nombre de otro animal, lo agregue a la lista e imprima en pantalla el cuarto animal de la lista.

lista = ["elefante", "jirafa","mono"]
nuevo_animal = input('Introduce un nombre de un animal: ')
lista.append(nuevo_animal)

print(lista)