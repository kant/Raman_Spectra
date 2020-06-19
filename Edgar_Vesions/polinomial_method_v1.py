'''Programa que calcula que calcule el ajuste polinomico
de un archivo de datos en formato .txt

By Edgar Lara
28-may-2020
'''
#limpiar terminal
import os
os.system("clear")
import numpy# as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

x=[]
y=[]
A=[]
file_name = '0_340_Subt2_01.txt'
#abrir archivo
f = open(file_name,'r')

#declarar matriz y guardar el .txt en esta
matriz_datos = []
matriz_datos = [line.split() for line in f]
f.close()
total_datos = len(matriz_datos)
#print(total_datos)

T=0
while (T < total_datos):
	x.append(float(matriz_datos[T][0]))
	y.append(float(matriz_datos[T][1]))
	T+=1

plt.plot(x, y, "*")
plt.title("Ajuste polinomico\n" + file_name)
plt.xlabel('Wave lenght')
plt.ylabel('Intensity')
############################################################################################
#Ajuste polinomico
ajuste = numpy.poly1d(numpy.polyfit(x, y, 52))
#myline = numpy.linspace(1, 22, 100)
plt.scatter(x, y)
#plt.plot(myline, ajuste(myline))
plt.plot(x, ajuste(x))
plt.show()
print(ajuste)
print("\n\n")
print("r^2 = " + str(r2_score(y, ajuste(x))))