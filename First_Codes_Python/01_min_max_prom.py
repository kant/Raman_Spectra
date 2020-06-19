'''Programa que calcula:
Promedio de lambas e intensidades
Minimo y máximo absoluto de intensidades
Minimo y máximo de intensidades en un rango dado de lambdas
Numero de valores en ese rango
Rango = (540,600)


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
#print(matriz_datos[0][2])


#Algoritmo para minimo y máximo
total_datos = len(matriz_datos) #Tamaño de los vectores columna
#print(total_datos)
contador=0
suma_lambdas = 0
suma_intensidades = 0
minimo = float(matriz_datos[0][1]) #Con esto inicializamos en
maximo = float(matriz_datos[0][1])	#el primer valor de la Intensidad

while (contador < total_datos):
	if (float(matriz_datos[contador][1]) < minimo):
		minimo = float(matriz_datos[contador][1])
	elif (float(matriz_datos[contador][1])>maximo):
		maximo = float(matriz_datos[contador][1])
	suma_lambdas=suma_lambdas+float(matriz_datos[contador][0])
	suma_intensidades=suma_intensidades+float(matriz_datos[contador][1])	
	contador += 1


#########################################################################	
contador=0
minimo_rango=maximo
maximo_rango=minimo
valores_rango=0
while (contador < total_datos):
	if (float(matriz_datos[contador][0]) > 540) and (float(matriz_datos[contador][0]) < 600):
		if (float(matriz_datos[contador][1]) < minimo_rango):
			minimo_rango = float(matriz_datos[contador][1])
		elif (float(matriz_datos[contador][1])>maximo_rango):
			maximo_rango = float(matriz_datos[contador][1])
		valores_rango +=1
	contador += 1

promedio_lambdas=suma_lambdas/total_datos
promedio_intensidades=suma_intensidades/total_datos
#print(contador)
print("El minimo absoluto es: " + str("{0:.2f}".format(minimo)))
print("El maximo absoluto es: " + str("{0:.2f}".format(maximo)))
print("Promedio de longitudes de onda: " + str("{0:.2f}".format(promedio_lambdas)))
print("Promedio de intensidades: " + str("{0:.2f}".format(promedio_intensidades)))
print("Minimo local en el rango: " + str("{0:.2f}".format(minimo_rango)))
print("Maximo local en el rango: " + str("{0:.2f}".format(maximo_rango)))
print("Valores dentro del rango: " + str("{0:.2f}".format(valores_rango)))

input()