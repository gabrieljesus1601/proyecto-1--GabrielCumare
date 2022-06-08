# proyecto-GabrielCumare
#problema 4 proyecto programacion
"""programaque dibuja la bandera de inglaterra utilizando con una longitud y altura introducida por el usuario, utilizando los caracteres + y 0 para dibujar dicha bandera """
from numpy import array #libreria numpy
#definiendo la funcion
def dim():
"""regresa dos valores validados, largo y altura"""

	datos = [] # creo ua matriz vacia para los 2 datos
  # ciclo que valida los datos
	while True:
		longitud = input(" ingrese el largo de la bandera: ")
		try:
			longitud_1 = int(longitud)
			if (2 < longitud_1 < 20):
				if ((longitud_1) % 2 != 0):
					datos.append(longitud_1)
					break
				else:
					True
			else:
				print("debe ingresar un valor mayor a 2 y menor a 20")
				
		except:
			print("solo debe ingresar valores numericos enteros positivos")
	while True:
		altura = input("ingrese la altura de la bandera: ")
		try:
			altura_1 = int(altura)
			if (2 < altura_1 < 20):
				if((altura_1) % 2 != 0):
					datos.append(altura_1)
					break
				else:
					True
			else:
				print("debe ingresar un valor mayor a 2 y menor a 20")
				
		except:
			print("debe ingresar valores numericos enteros positivos")
		return(datos)
def bandera(largo_2,altura_2):
	"""regresa la bandera de inglaterra dibujada en el cmd """
	flag = [] #crear una matriz vacia para la bandera
	largo_mitad = (largo_2 + 1)/2
	altura_mitad = (altura_2 + 1)/2
	for i in range(altura_2):
		aux_1 = [] #lista auxiliar para las columnas de la matriz
		for j in range(largo):
			if (j == largo_mitad - 1) or (i == altura_mitad - 1):
				aux_1.append("+")
			else:
				aux_1.append(0)
		flag.append(aux_1)
	return(array(flag)) # se usa array para ordenar la matriz

dim_1 = dim()
largo_2 = dim_1[0]
altura_2 = dim_1[1]
bandera_final = bandera(largo_2,altura_2)
print(bandera_final) 
