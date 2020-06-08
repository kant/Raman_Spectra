'''Esta versión grafica el .txt y nos da su ajuste polinómico.
Update:
Se optimizaron las funciones.
Se ingresa el grado manualmente.

By Edgar Lara
28-may-2020
'''
#limpiar terminal
import os
os.system("clear")
import numpy# as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
#import math

x=[]
y=[]
file_name = '0_340_Subt2_01.txt'

def file_to_matrix (name):
	#open file
	f = open(name,'r')
	#save .txt into matrix
	matrix = []
	matrix = [line.split() for line in f]
	f.close()
	return matrix

def list_to_float (matrix,X_,Y_):
	X_ = []
	Y_ = []
	T=0
	while (T < len(matrix)):
		X_.append(float(matrix[T][0]))
		Y_.append(float(matrix[T][1]))
		T+=1
	return X_,Y_		

def plotting (X_, Y_, order_):	
	plt.title("Ajuste polinomico\n" + file_name)
	plt.xlabel('Wave lenght')
	plt.ylabel('Intensity')
	#print("r^2 = " + str(r2_score(Y_, ajuste(X_))))	
	plt.plot(X_, Y_, "-")
	plt.scatter(X_, Y_)
	#polynomial regression
	ajuste = numpy.poly1d(numpy.polyfit(X_, Y_, order_))
	plt.plot(X_, ajuste(X_))
	plt.show()
	print(ajuste)
	print("\n\n")
	print("r^2 = " + str(r2_score(Y_, ajuste(X_))))
	#print("r = " + str(math.sqrt(r2_score(Y_, ajuste(X_)))))



order = int(input("Grado polinomico: "))
matrix_data = file_to_matrix(file_name)
x, y = list_to_float(matrix_data,x,y)
plotting(x,y, order)
input()