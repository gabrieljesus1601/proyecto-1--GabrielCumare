#proyecto-GabrielCumare
#ejercicio 3 del proyecto 
""" programa que simula un cajero automatico que solicita al usuario el monto en dolares que desea retirar con la cantidad minima de billetes """
try:
    money = int(input("introduzca el monto que desea retirar: "))
    cashList = [] #lista donde que ira descontando y dando los billetes
    if money < 0: 
        print("este monto no es posible de retirar") # el monto a retirar no puede ser negativo
    else:
        while money > 0: 
#condicionales para que se use la menor cantidad de billetes
            if (money >= 100):
                cashList.append(100) 
                money -= 100
            elif (money >= 50):
                cashList.append(50)
                money -= 50
            elif (money >= 20):
                cashList.append(20)
                money -= 20
            elif (money >= 10):
                cashList.append(10)
                money -= 10
            elif (money >= 5):
                cashList.append(5)
                money -= 5
            elif (money >= 1):
                cashList.append(1)
                money -= 1
                
        print("denominacion del billete a entregar : billetes a etregar") 
# crear un diccionario que cuenta  la cantidad de veces que aparecen los billetes
        result = dict((cash, cashList.count(cash)) for cash in cashList)
        print(result)
except:
    print("este valor no es valido") # el monto a retirar no puede ser de otro tipo que no sea entero
