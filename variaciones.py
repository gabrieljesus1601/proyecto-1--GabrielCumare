# proyecto-GabrielCumare
#ejercio 1 proyecto programacion

#Creo una función que reconoce los máximos y mínimos.
def checkTuple(temp):
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

    dayCount = 0
    errorCount = 0
    menosCien = 0 
    masCien = 0
    minimum = 50 
    maximum = 0
    
    #Creo un ciclo que me recorrerá los días, y estudiarán los datos.
    
    for element in lista:
        dayCount += 1
        #Verifico que el dato no sea un error de entrada.
        if checkTuple(element) == False:
            errorCount += 1
        #Hago el conteo de los -100 y 100
        if element[0] < -100:
            menosCien += 1
        elif element[0] > 100:
            masCien += 1
        if element[1] < -100:
            menosCien += 1
        elif element[1] > 100:
            masCien += 1

        #Verifico que los elementos estén entre 0 y 50, para los máximos y mínimos.
        if 0 <= element[0] <= 50 and 0 <= element[1] <= 50:
            if element[0] > maximum:
                maximum = element[0]
            elif element[1] > maximum:
                maximum = element[1]
            
            if element[0] < minimum:
                minimum = element[0]
            elif element[1] < minimum:
                minimum = element[1]
                
        #Imprimo los valores en pantalla
print('Total dias: {}'.format(dayCount))
print('Total errores: {}'.format(errorCount))
print('Total errores < -100 (menores a 100) : {}'.format( menosCien))
print('Total errores > 100 (mayores a 100): {}'.format(masCien))
print('Total errores variaciones de 100: {}'.format(menosCien + masCien))
print('Minimo: {}'.format(minimum))
print('Maximo: {}'.format(maximum))
            
