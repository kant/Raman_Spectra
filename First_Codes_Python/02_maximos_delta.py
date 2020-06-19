'''Programa que calcula:
El maximo de intensidades dentro de un rango Delta Lambda dado


By Edgar Lara
23-may-2020
'''
#limpiar terminal
import os
os.system("clear")

#abrir archivo
f = open('0_340_Subt2_03.txt','r')

#declarar matriz y guardar el .txt en esta
matriz_datos = []
matriz_datos = [line.split() for line in f]
f.close()
total_datos = len(matriz_datos) #Tamaño de los vectores columna
maximos_rangos = [0,0,0,0,0]
contador = 0 #contador para barrer toda la matriz
cl = 0 #contador para cambiar entre vector lambdas
j = 0 #contador para poder inicializar
lambdas = [550.910, 561.289, 568.153, 573.301, 580.701]
delta_lambda = 1.0

#ciclo para barrer toda la matriz
while (contador < total_datos):
	if (cl > 4): #cuando se llene nuestro vector de maximos, termina
		break
	#Compara si la longitud actual estra dentro del rango	
	if (float(matriz_datos[contador][0]) >= (lambdas[cl]-delta_lambda)) and (float(matriz_datos[contador][0]) <= (lambdas[cl]+delta_lambda)):
		#print("Si esta dentro")
		if (j == 0): #inicialza la posicion del maximo de esa intensidad
			maximos_rangos[cl] = float(matriz_datos[contador][1])
			j+=1
			#Compara para seleccionar nuevo maximo
		elif (float(matriz_datos[contador][1])>maximos_rangos[cl]):
			maximos_rangos[cl] = float(matriz_datos[contador][1])
	#Comparador para cambiar a nuevo espacio del vector de maximos		
	if (float(matriz_datos[contador][0]) > (lambdas[cl]+delta_lambda)):
		j = 0
		cl+=1	
	contador += 1 #siguiente elemento de la matriz

#Imprime los datos de interes
x=0
while (x < 5):
	print("Longitud: " + str("{0:.2f}".format(lambdas[x])) + " Maximo intensidad: " + str("{0:.2f}".format(maximos_rangos[x])))
	x+=1
input()