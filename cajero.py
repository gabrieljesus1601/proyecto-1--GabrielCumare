#proyecto-GabrielCumare
#ejercicio 3 del proyecto 
""" programa que simula un cajero automatico que solicita al usuario el monto en dolares que desea retirar con la cantidad minima de billetes """
try:
    dinero = int(input("introduzca el monto que desea retirar: "))
    lista_dinero = [] #lista donde que ira descontando y dando los billetes
    if dinero < 0: 
        print("este monto no es posible de retirar") # el monto a retirar no puede ser negativo
    else:
        while dinero > 0: 
#condicionales para que se use la menor cantidad de billetes
            if (dinero >= 100):
                lista_dinero.append(100) 
                dinero -= 100
            elif (dinero >= 50):
                lista_dinero.append(50)
                dinero -= 50
            elif (dinero >= 20):
                lista_dinero.append(20)
                dinero -= 20
            elif (dinero >= 10):
                lista_dinero.append(10)
                dinero -= 10
            elif (dinero >= 5):
                lista_dinero.append(5)
                dinero -= 5
            elif (dinero >= 1):
                lista_dinero.append(1)
                dinero -= 1
                
        print("billete de : billetes a etregar") 
# crear un diccionario que cuenta  la cantidad de veces que aparecen los billetes
        result = dict((dinero, lista_dinero.count(dinero)) for dinero in lista_dinero)
        print(result)
except:
    print("este valor no es valido") # el monto a retirar no puede ser de otro tipo que no sea entero
