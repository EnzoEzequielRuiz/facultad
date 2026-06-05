#Hacer una función que automatice el control vehicular en rutas nacionales. Hacer el control para la Ruta Nacional 8 durante un día completo, se debe controlar que los automóviles no superen 100 km/h y en caso de hacerlo se les enviará una multa a sus hogares, si es reincidente la multa se duplica. Para ello cuenta con las siguientes funciones.

#darPatentes(ruta): Dada una ruta nacional devuelve una lista con todas las patentes de los autos que pasaron en el día.

#controlVelocidad(patente): Recibe un número de patente y devuelve la velocidad a la que cruzó el radar dicho automóvil.

#reincidente(patente): Devuelve True en caso de que la patente ya tenga multas por exceso de velocidad.

#costoActual(): No recibe parámetros y devuelve el costo por superar la velocidad permitida.

#enviarMulta(patente, costo): Manda una multa al domicilio del propietario del automóvil con el costo.

def darPatentes(ruta):
    patentes = ['ada234', 'foe352', 'rti238']
    if ruta == 8:
        return patentes
    return False

def controlVelocidad(patente):
    patentes = ['ada234', 'foe352', 'rti238']
    velocidad = ['120','70','30']
    if patente in patentes:
        for i in range(len(patentes)):
            if patentes[i] == patente:
                return velocidad[i]

def reincidente(patente):    
    patentes_con_multas = ['ada234', 'foe352', 'rti238']
    if patente == patentes_con_multas[0]:
        return True
    else:
        return False
    
def costoActual():
    return ('$430.000')

def enviarMulta(patente, costo):
    return('Multa por exceso de velocidad: ',patente,'\nCosto $',costo)
#===========================#
#Control de RUTA nacional 8
costo = costoActual()

ruta = 8

multa = ''
enviar_multa = ''

if darPatentes(ruta):
    lista_patentes = darPatentes(ruta)
    for i in lista_patentes:
        if controlVelocidad(i):
            print(i,' = ',controlVelocidad(i),' km/s')
            if reincidente(i):
                multa = i
                enviar_multa = enviarMulta(i,costo)
                print(enviar_multa)