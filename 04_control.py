'''Programa que calcula:
El maximo de intensidades dentro de un rango Delta Lambda dado de n-numero de archivos

By Edgar Lara
25-may-2020
'''
#limpiar terminal
import os

import numpy as np
import matplotlib.pyplot as plt
os.system("clear")
#############################################################	Declaracion de variables	################################
a_picos= [0,0,0,0,0,]
a_rango = [0,0]
sum_maximos_rangos=[0,0,0,0,0]
prom_maximos_rangos=[0,0,0,0,0]
count = 0
Y=0
separador = ", "
datos_control = [0,0,"",0,""]
cad_1 = "0_340_Subt2_0"
cad_2 = "0_340_Subt2_"		#strings para abrir archivos de datos
cad_3 = ".txt"
cad_0 = ""
X=[]
Y=[]

#############################################################	Ciclo archivo de control	################################
f = open('control.txt','r')
while(count <= 4):
	linea = f.readline()
	#print(linea)
	if(count==0):
		n_archivos=int(linea)
	elif(count==1):
		n_picos=int(linea)
	elif(count==2):
		s_picos = linea.split(", ") #de esta manera lo guarda en un list
	elif(count==3):
		delta = float(linea)
	elif(count==4):
		s_rango = linea.split(", ")
	elif not linea:
		break
	count += 1
f.close()

#ciclo para convertir a flotantes ciertos strings
count=0
while (count <= 4):
	a_picos[count] = float(s_picos[count])
	if (count <= 1):
		a_rango[count] = float(s_rango[count])
	count += 1

print("Numero de archivos: " + str(n_archivos))
print("Picos " + str(n_picos))
#print(s_picos)
print("Los picos son: " + str(a_picos))
print("Delta lambda: " + str(delta))
#print(s_rango)
print("Rango: " + str(a_rango) + "\n\n")


###########################################################	Concatenar nombre de archivos	################################
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


############################################################################################################################
def maximo_int (nombre_cadena):
	f = open(nombre_cadena,'r')
	matriz_datos = []
	matriz_datos = [line.split() for line in f]
	total_datos = len(matriz_datos) #Tamaño de los vectores columna
	maximos_rangos = [0,0,0,0,0]
	contador = 0 #contador para barrer toda la matriz
	cl = 0 #contador para cambiar entre vector lambdas
	j = 0 #contador para poder inicializar

	#ciclo para barrer toda la matriz
	while (contador < total_datos):
		if (cl > 4): #cuando se llene nuestro vector de maximos, termina
			break
		#Compara si la longitud actual estra dentro del rango	
		if (float(matriz_datos[contador][0]) >= (a_picos[cl]-delta)) and (float(matriz_datos[contador][0]) <= (a_picos[cl]+delta)):
			#print("Si esta dentro")
			if (j == 0): #inicializa la posicion del maximo de esa intensidad
				maximos_rangos[cl] = float(matriz_datos[contador][1])
				j+=1
				#Compara para seleccionar nuevo maximo
			elif (float(matriz_datos[contador][1])>maximos_rangos[cl]):
				maximos_rangos[cl] = float(matriz_datos[contador][1])
		#Comparador para cambiar a nuevo espacio del vector de maximos		
		if (float(matriz_datos[contador][0]) > (a_picos[cl]+delta)):
			j = 0
			cl+=1	
		contador += 1 ##siguiente elemento de la matriz
		#return maximos_rangos[]
	
	f.close()
	#Imprime los datos de interes
	x=0
	while (x <  n_picos):
		print("Longitud: " + str("{0:.2f}".format(a_picos[x])) + " Maximo intensidad: " + str("{0:.2f}".format(maximos_rangos[x])))
		sum_maximos_rangos[x]+=maximos_rangos[x]
		x+=1
	print("\n")
m=1	
while (m <= n_archivos):
		if (m >= 10):
			CA = cad_2
		else:
			CA = cad_1
		CA = CA + str(m) + cad_3
		print(CA)
		f = open(CA,'r')

		#declarar matriz y guardar el .txt en esta
		matriz_datos = []
		matriz_datos = [line.split() for line in f]
		f.close()
		total_datos = len(matriz_datos)
		#print(total_datos)


		T=0
		while (T < total_datos):
			X.append(float(matriz_datos[T][0]))
			Y.append(float(matriz_datos[T][1]))
			T+=1

		plt.plot(X, Y, "*")
		plt.title(CA)
		plt.xlabel('Wave lenght')
		plt.ylabel('Intensity')
		plt.show()
		m+=1

nombres_archivos(cad_0, cad_1, cad_2, cad_3, n_archivos)

x=0
while (x < n_picos):
	prom_maximos_rangos[x]=(sum_maximos_rangos[x])/n_archivos
	print("El promedio del pico " + str(x+1)+": " + str("{0:.2f}".format(prom_maximos_rangos[x])))
	x+=1

#print(prom_maximos_rangos)
input()