#Hacer un programa que reciba un número m y determine el primer n para el cual la suma 1+2+...+n > m. Por ejemplo, si el usuario ingresa 11 se deberá retornar 5 ya que 1+2+3+4 = 10 < 11 y 1 + 2 + 3 + 4 + 5 = 15 > 11

m = int(input('Introduce el valor de m: '))
acumulador = 0
contador = 1
for i in range(1,m+1):
    acumulador += i
    if acumulador < m:
        contador += 1
print(contador)