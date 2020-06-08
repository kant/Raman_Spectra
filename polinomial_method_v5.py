'''Esta versión grafica el .txt y nos da su ajuste polinómico.
Update:
Plotea un rango dado.
El ajuste se restringió solo a los mínimos.
Se aplanó el espectro.
Calculo del área bajo el espectro.

By Edgar Lara
07-jun-2020
'''
import os
os.system("clear")
import numpy# as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import math
#from tkinter import *
#from PIL import ImageTK,Image

file_name = '0_340_Subt2_01.txt'

#Save .txt into matrix
def file_to_matrix (name):
	f = open(name,'r')
	matrix = []
	matrix = [line.split() for line in f]
	f.close()
	return matrix
#Split matrix into vector and convert to float each term in vectors
def list_to_float (matrix):
	X_ = []
	Y_ = []
	T=0
	while (T < len(matrix)):
		X_.append(float(matrix[T][0]))
		Y_.append(float(matrix[T][1]))
		T+=1
	return X_,Y_		
#From the entire wavelenght data, now collect in range (540,600)nm
def range1_to_range2(X_, Y_, R1_, R2_):
	T = 0
	Xaux_ = []
	Yaux_ = []
	while (T < len(X_)):
		if (X_[T]>R1_) and (X_[T]<R2_):	#R1=540, R2=600
			Xaux_.append(X_[T])
			Yaux_.append(Y_[T])
		T+=1
	return Xaux_,Yaux_
#In (540, 600)nm gets the minimum every 5 nm	
def mins_in_spectra(X_, Y_, R1_, R2_):
	Xaux2_ = []
	Yaux2_ = []
	i=0
	U=0
	while (U < len(X_)):
		if (X_[U] > R1_) and (X_[U] < R2_):
			miny_=max(Y_)
			while (X_[U] > R1_+i*5) and (X_[U] < R1_+(i+1)*5):
				if (Y_[U] < miny_):
					minx_ = X_[U]
					miny_ = Y_[U]
				U += 1	
			Xaux2_.append(minx_) 
			Yaux2_.append(miny_)
			i += 1
		U += 1
	return Xaux2_, Yaux2_	
#This function is for plot the spectras
def plotting (X_, Y_, X2_, Y2_, order_):	
	plt.title("Polynomial regression\n" + file_name)
	plt.xlabel('Wave lenght')
	plt.ylabel('Intensity')
	#plt.scatter(X_, Y_) #Grafica el espectro como puntos
	plt.plot(X_, Y_, "-") #Une los puntos del espectro
	#Polynomial regression
	ajuste = numpy.poly1d(numpy.polyfit(X_, Y_, order_))
	ajuste2 = numpy.poly1d(numpy.polyfit(X2_, Y2_, order_))
	plt.plot(X_, ajuste(X_)) #Grafica el ajuste de los puntos
	plt.plot(X2_, ajuste2(X2_)) #Grafica el ajuste de los puntos minimos
	plt.plot(X_, Y_ - ajuste2(X_), "b-") #Grafica spectro aplanado
	plt.axhline(y=0, color='r', linestyle='-') #linea cte en y=0
	plt.axvline(x=540, color='r', linestyle='-') #linea cte en x=540
	plt.axvline(x=600, color='r', linestyle='-') #linea cte en x=600
	#plt.plot(X_[len(X_)-1], Y_[len(X_)-1] - ajuste2(X_[len(X_)-1]), 'r*' )
	plt.show()
	#print()
	print("\n\n")
	print(ajuste2)
	print("r^2 = " + str(r2_score(Y_, ajuste(X_))))
	print("r = " + str(math.sqrt(r2_score(Y_, ajuste(X_)))))
	T = 1
	Area = 0
	while (T < len(X_)):
		Area += (Y_[T]-ajuste2(X_[T]))*(X_[T]-X_[T-1])
		T +=1
	#plt.show()
	print("\nArea spectra: " + str("{:.2f}".format(Area)) + "")

matrix_data = file_to_matrix(file_name)
x, y = list_to_float(matrix_data)
#rango = [min(x), max(x)-3]
rango = [540, 600]
Xaux, Yaux = range1_to_range2(x, y, rango[0],rango[1])
Xaux2, Yaux2 = mins_in_spectra(x, y, rango[0],rango[1])
#order = int(input("Polinomial order: "))
order = 8
Ajuste_aplanado = plotting(Xaux, Yaux, Xaux2, Yaux2, order)
input("\n\nClick enter to close")