#Auxilio Mecánico
#En una empresa de auxilio mecánico existen dos coberturas para los clientes, Oro y Plata. Los clientes con cobertura Oro tienen más beneficios que los de cobertura Plata y pagan mensualmente un abono mayor. Por ejemplo los clientes Oro tienen usos ilimitados y los clientes Plata sólo hasta 5. El sistema ya está funcionando y tenemos que implementar una función particular que devuelva el costo para un cliente de un servicio particular. Se cuenta con las siguientes funciones y sus valores de retorno:

# cobertura(cliente): retorna un string con los valores "Oro" o "Plata", correspondiente al tipo de cobertura del cliente.

# usados(cliente): retorna un entero que representa la cantidad de servicios que ya utilizó el cliente.

#  radioDeCobertura(cliente, localidad): devuelve True si el cliente se encuentra dentro del radio de cobertura cubierto por la empresa.

#Al recibir un llamado el operador telefónico solicita el número de cliente, la localidad para la que solicita la asistencia y le informa el costo del servicio teniendo en cuenta que el servicio no tendrá costo para los clientes Oro que estén dentro del área de cobertura y para los clientes Plata que les quedaran servicios para usar y estuvieran dentro dicha área. Pagarán $50, los clientes Plata dentro del área de cobertura pero ya sin servicios gratis. Pagarán $30 extra los clientes que estén fuera del área de cobertura. Observación, los dos últimos montos pueden ser acumulativos. Hacer una función llamada pagara que dado un cliente y una localidad devuelva el costo del servicio para el cliente.

def cobertura(cliente):
    if cliente == '44556550':
        return 'Oro'
    return 'Plata'

def usados(cliente):
    if cliente == '44838034':
        return True
    return False

def radioDeCobertura(cliente, localidad):
    if cliente == '44556550' and localidad == 'san miguel':
        return True
    elif not cliente == '44556550' and localidad == 'san miguel':
        return True
    elif cliente == '44556550' and not localidad == 'san miguel':
        return False
    elif not cliente == '44556550' and not localidad == 'san miguel':
        return False



def pagara(num_cliente, localidad):
    #COBERTURA ORO
    if cobertura(num_cliente) == 'Oro':
        if radioDeCobertura(num_cliente,localidad):
            return ('Estas dentro de la cobertura, no tiene costo, Sos cliente ORO!!')
        elif not radioDeCobertura(num_cliente,localidad):
            return ('Sos cliente ORO!!, Pero no estas dentro de la cobertura, seria un costo de $30.')

    #COBERTURA PLATA
    else:
        if usados(num_cliente) and radioDeCobertura(num_cliente,localidad):
            return ('Todavia tiene usos para el servicio, de cliente Plata, no tiene costo.')
            
        elif usados(num_cliente) and not radioDeCobertura(num_cliente,localidad):
            return ('Todavia tienes usos de servicio de cliente Plata, pero no estas en el radio de cobertura se abonara $30.')
            
        elif not usados(num_cliente) and radioDeCobertura(num_cliente,localidad):
            return ('Costo por servicio por extra de usos por ser cliente Plata, es de $50, estas dentro de la cobertura y eso no tiene costo.')
        else:
            return ('Costo por servicio por extra de usos por ser cliente Plata, es de $50 mas $30 por no estar dentro de la cobertura. Total $80.')


llamar_operador = input('Llamar al operador?: Escribir, SI o NO: ')
llamar_operador.lower()

if llamar_operador == 'si':
    num_cliente = input('Ingrese su numero de cliente: ')
    localidad = input('Ingrese su localidad: ')
    print(pagara(num_cliente,localidad))



















