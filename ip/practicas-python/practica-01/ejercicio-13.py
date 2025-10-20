#EJERCICIO 13
''' Suponga que una persona desea invertir su capital en un banco y quiere saber cuánto dinero tendrá en su cuenta si el banco incrementa el 6% mensual(no acumulativo). Se le debe pedir al usuario el capital a invertir y la cantidad de meses. Por ejemplo, si invierte 500 mil pesos por 4 meses el banco debería devolverle 620 mil pesos.'''

capital = int(input('Ingrese su capital: $'))
meses = int(input('Ingrese los meses a invertir:'))
interes_mensual = 0.06

print('-Saldo ingresado: $',capital,'\n-Meses a invertir:',meses,'\n-Interes mensual no acumulativo:',interes_mensual,'\n-Total de ganancias estimadas: $',((capital * interes_mensual)*meses) + capital)