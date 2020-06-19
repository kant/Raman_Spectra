'''Esta versión grafica el .txt y nos da su ajuste polinómico.
Update: Con funciones

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

def file_to_matrix (name):
	#abrir archivo
	f = open(name,'r')
	#declarar matriz y guardar el .txt en esta
	matrix = []
	matrix = [line.split() for line in f]
	f.close()
	return matrix
	#print(total_datos)

def plotting (X_, Y_):
	plt.plot(X_, Y_, "*")
	plt.title("Ajuste polinomico\n" + file_name)
	plt.xlabel('Wave lenght')
	plt.ylabel('Intensity')
	#Ajuste polinomico
	ajuste = numpy.poly1d(numpy.polyfit(X_, Y_, 52))
	#myline = numpy.linspace(1, 22, 100)
	plt.scatter(X_, Y_)
	#plt.plot(myline, ajuste(myline))
	plt.plot(X_, ajuste(X_))
	plt.show()
	print(ajuste)
	print("\n\n")
	print("r^2 = " + str(r2_score(Y_, ajuste(X_))))	

matrix_data = file_to_matrix(file_name)

T=0
while (T < len(matrix_data)):
	x.append(float(matrix_data[T][0]))
	y.append(float(matrix_data[T][1]))
	T+=1

plotting(x,y)