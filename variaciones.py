# proyecto-GabrielCumare
#ejercio 1 proyecto programacion
"""programa que registra variaciones gravimetricas diarias en tuplas para valores maximos y minimos introducidos por el usuario, indicando cuantos dias duro la salida, cantidad de errores y la variacion media minima y maxima   """
def checkTuple(temp):
    """ funcion que reconoce los maximos y minimos"""
    if temp[0] < 0 or temp[0] > 50:
        return 0
    elif temp[1] < 0 or temp[1] > 50:
        return 0
    else:
        return 1

if __name__ == '__main__':
    #Creo una lista que contendrá dos datos que se refieren a los días.
    lista = []
    #Creo un bucle para los días, cuando el valor ingresado sea (0,0), se detendrá el bucle.
    while 1:
        temp = (int(input("Ingrese el primer dato: ")), int(input("Ingrese el segundo dato: ")))
        
        if temp != (0, 0):
            #Si los valores dados son distintos de condicional, se agrega a la lista.
            lista.append(temp)
        else:
            break
    #Defino los contadores y variables

    dia_contador = 0
    error_contador = 0
    menos_cien = 0 
    mas_cien = 0
    minimo = 50 
    maximo = 0
    
    #Creo un ciclo que me recorrerá los días, y estudiarán los datos.
    
    for elemento in lista:
        dia_contador += 1
        #Verifico que el dato no sea un error de entrada.
        if checkTuple(elemento) == False:
            error_contador += 1
        #Hago el conteo de los -100 y 100
        if elemento[0] < -100:
            menos_cien += 1
        elif elemento[0] > 100:
            mas_cien += 1
        if elemento[1] < -100:
            menos_cien += 1
        elif elemento[1] > 100:
            mas_cien += 1

        #Verifico que los elementos estén entre 0 y 50, para los máximos y mínimos.
        if 0 <= elemento[0] <= 50 and 0 <= elemento[1] <= 50:
            if elemento[0] > maximo:
                maximo = elemento[0]
            elif elemento[1] > maximo:
                maximo = elemento[1]
            
            if elemento[0] < minimo:
                minimo = elemento[0]
            elif elemento[1] < minimo:
                minimo = elemento[1]
                
        #Imprimo los valores en pantalla
print('Total dias: {}'.format(dia_contador))
print('Total errores: {}'.format(error_contador))
print('Total errores < -100 (menores a 100) : {}'.format( menos_cien))
print('Total errores > 100 (mayores a 100): {}'.format(mas_cien))
print('Total errores variaciones de 100: {}'.format(menos_cien + mas_cien))
print('Minimo: {}'.format(minimo))
print('Maximo: {}'.format(maximo))
            
