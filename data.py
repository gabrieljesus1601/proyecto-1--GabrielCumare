# proyecto-GabrielCumare 
#ejercicio 2 del proyecto de programacion
"""programa que calcula la media, la mediana, el rango y la desviacion estandar de minimo 20 datos ingresados por el usuario, mostrando en pantalla la data introducida """
import math #libreria
cantidad = int(input("Ingrese la cantidad de datos a calcular (minimo 20 datos): "))
while(cantidad<20):
    cantidad=input("La cantidad mimina es 20 datos. Ingrese la cantidad de datos a calcular: ")
    cantidad= int(cantidad)
    numeros = []
for i in range(cantidad):
    #  range comenzará desde 0, así que imprimimos el número solicitado pero sumando 1
    numero = input(f"Ingresa el numero {i + 1}: ")
    # Convertir a float, porque input regresa una cadena
    numero = float(numero)
    # Lo agregamos al arreglo con append
    numeros.append(numero)
print("La data ingresada es: ")
print(numeros)   


def obtener_media(arreglo):
    sumatoria = 0
    for valor in arreglo:
        sumatoria += valor
    longitud = len(arreglo)
    return sumatoria / longitud


def obtener_mediana(arreglo):
    # Primero se ordena
    arreglo.sort()
    # Obtener longitud
    longitud = len(arreglo)
    mitad = int(longitud / 2)
    # Si la longitud es par, promediar elementos centrales
    if longitud % 2 == 0:
        mediana = (arreglo[mitad - 1]+arreglo[mitad]) / 2
    else:
        # Si no, es la del centro
        mediana = arreglo[mitad]
    return mediana


def range(arreglo):
    return max(arreglo)-min(arreglo)


def desviacion_estandar(arreglo):
    mean = sum(arreglo) / len(arreglo)
    var = sum((l-mean)**2 for l in arreglo) / len(arreglo)
    st_dev = math.sqrt(var)
    return st_dev

print("La Media es:")
print(obtener_media(numeros))

print("La Mediana es:")
print(obtener_mediana(numeros))

print("El rango es:")
print(range(numeros))

print("La desviacion estandar:")
print(desviacion_estandar(numeros))
