'''Programa que calcula:
El maximo de intensidades dentro de un rango Delta Lambda dado de n-numero de archivos

By Edgar Lara
25-may-2020
'''
#limpiar terminal
import os
os.system("clear")


contador = 1 #contador
n = 3 #Numero de archivos totales que tenemos +1
cad_1 = "0_340_Subt2_0"
cad_2 = "0_340_Subt2_"		#strings para abrir archivos
cad_3 = ".txt"
cad_0 = ""

#Funci0n que se encraga de abrir los archivos y calcular los maximos en los deltas dados 
#########################################################################################################
def maximo_int (nombre_cadena):
	f = open(nombre_cadena,'r')
	matriz_datos = []
	matriz_datos = [line.split() for line in f]
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
		contador += 1 ##siguiente elemento de la matriz
		#return maximos_rangos[]
	f.close()
	#Imprime los datos de interes
	print("Archivo:" + nombre_cadena)
	x=0
	while (x < 4):
		print("Longitud: " + str("{0:.2f}".format(lambdas[x])) + " Maximo intensidad: " + str("{0:.2f}".format(maximos_rangos[x])))
		x+=1
	print("\n")


		
#########################################################################################################
#while que concatena strings para formar nombres de archivos
def nombres_archivos(cadena_0, cadena_1, cadena_2, cadena_3, n_archivos):
	m=1
	while (m <= n_archivos):
		if (m >= 10):
			cadena_0 = cadena_2
		else:
			cadena_0 = cadena_1
		cadena_0 = cadena_0 + str(m) + cadena_3
		#print(cad_0)
		#return cadena_0
		maximo_int(cadena_0) #Llama a la funcion que hace magia
		m += 1



nombres_archivos(cad_0, cad_1, cad_2, cad_3, n)
input()