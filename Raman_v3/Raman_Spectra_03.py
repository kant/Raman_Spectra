'''Program for analisis of spectra
Updates:
	*	

By Edgar Lara
Created: Aug 08, 2020
'''
import os
os.system("clear")
import numpy# as np
import matplotlib.pyplot as plt
from tkinter import  *
import plotly.graph_objects as go

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
#This function is for plot the spectra
def plotting (X_, Y_, X2_, Y2_, order_):
	#This is for graphic interface
	root = Tk()
	root.title('Raman Spectra V8.1')
	root.geometry('600x400')
	root.configure(background='#212F3C')
	option_plot = 0
	#This funcion is for choose between different graphs.
	def spectra_plot(option_plot):
		plt.clf()
		plt.xlabel('Wave lenght (nm)')
		plt.ylabel('Intensity')
		plt.axhline(y=0, color='r', linestyle='-') #linea cte en y=0
		ajuste = numpy.poly1d(numpy.polyfit(X_, Y_, order_))
		ajuste2 = numpy.poly1d(numpy.polyfit(X2_, Y2_, order_))
		Xsmoth = numpy.arange(min(X_), max(X_), 0.5)
		Ysmoth = ajuste(Xsmoth)
		Ysmoth2= ajuste2(Xsmoth)
		Yflat_ = []
		Yflat_2_ = []
		#########################################################################
		#Loop for obtain Flat spectra 
		T = 0
		for T in range(0, len(Y_)):
			Yflat_.append(Y_[T] - ajuste2(X_[T]))	
		#Loop for absolute min Y vale
		T = 0; Ymin_ = max(Yflat_)
		for T in range(0, len(Yflat_)):
			if (Yflat_[T] <= Ymin_):
				Ymin_ = Yflat_[T]
		#print(Ymin_)
		#For rise all the flat spectra with the min
		T = 0
		for T in range(0, len(Yflat_)):
			Yflat_2_.append(Yflat_[T] - Ymin_)
		######################################################################### 
		Lambdas_ = [550.910, 561.289, 568.153, 573.301, 580.701]
		Max_X = [0,0,0,0,0]; Max_Y = [0,0,0,0,0]; Positions_X = [0,0,0,0,0]; Delta_Lambda_ = 1.0
		T = 0; T1 = 0
		#Looop: Find Max Y in Flat Spectra
		while (T < len(X_)):
			if (T1 > 4): #End when vector Max is full of values
				break
			if (X_[T] >= (Lambdas_[T1] - Delta_Lambda_)) and (X_[T] <= (Lambdas_[T1] + Delta_Lambda_)):
				if (Yflat_2_[T] > Max_Y[T1]):
					Max_X[T1] = X_[T]
					Max_Y[T1] = Yflat_2_[T]
					Positions_X[T1] = T
			if (X_[T] > (Lambdas_[T1] + Delta_Lambda_)):
				T1 += 1	
			T += 1
		######################################################################### 	
		Limits_ = [[0,0],[0,0],[0,0],[0,0],[0,0]] #Area delimitations 
		T = 0
		while (T < len(Positions_X)):
			U = Positions_X[T]
			while (Yflat_2_[U] > Yflat_2_[U+1]):
				Limits_[T][0] += 1
				U += 1
			#print("Right" +str(T+1) +": " + str(Limits_[T][0]))

			U = Positions_X[T]
			while (Yflat_2_[U] > Yflat_2_[U-1]):
				Limits_[T][1] -= 1
				U -= 1
			#print("Left" +str(T+1) +": " + str(Limits_[T][1]))
			#print("\n")
			T += 1
		#Area under specific points
		def area_points ():
			A = []; N = [0,0,0,0,0]; f = [0,0,0,0,0]; DeltA = [0,0,0,0,0]
			for T in range(0, len(Max_Y)):
				f_ = 0; Delta_X_ = 0
				for W in range(0, Limits_[T][0]):
					f_ += Yflat_2_[Positions_X[T]+(W+1)]
				for W in range(0, abs(Limits_[T][1])):
					f_ += Yflat_2_[Positions_X[T]-W-1]
				f_ += Yflat_2_[Positions_X[T]]
				f[T] = f_
				A.append(f_)
				Delta_X_ = (X_[Positions_X[T]+Limits_[T][0]])-(X_[Positions_X[T]+Limits_[T][1]])
				DeltA[T] = Delta_X_
				N[T] = (Limits_[T][0]-Limits_[T][1]+1)
				A[T] = (f[T]/N[T])*DeltA[T]
			return A
		Area_poits = area_points()
		#This if else sequence is for every button in graphic interface
		#########################################################################
		if (option_plot >= 1) and (option_plot < 10):
			#Flat spectra fixed, max intensities
			if (option_plot == 1):
				plt.title("Flat spectra\n" + file_name)
				#ajuste2 = numpy.poly1d(numpy.polyfit(X2_, Y2_, order_))
				plt.plot(X_, Yflat_2_, "b-", label="Flat Spectra Fixed") #Grafica spectro aplanado
				plt.axhline(y=0, color='r', linestyle='-') #linea cte en y=0
				T = 0
				for T in range(0, len(Max_X)):
					plt.plot(Max_X[T], Max_Y[T], 'r*')
					plt.annotate(str("{0:.2f}".format(Max_Y[T])),xy=(Max_X[T],Max_Y[T]),xytext=(Max_X[T], Max_Y[T]))
			#Espectro final de Raman
			elif (option_plot == 2):
				plt.title("Flat spectra\n" + file_name)
				plt.plot(X_, Yflat_2_, "b-", label="Flat Spectra Fixed") #Grafica spectro aplanado
				plt.axhline(y=0, color='r', linestyle='-') #linea cte en y=0
				T = 0 #This is for plot separation between interest points
				for T in range (0, len(Area_poits)):
					plt.annotate(str("{0:.2f}".format(Area_poits[T])),xy=(Max_X[T],Max_Y[T]),xytext=(Max_X[T], Max_Y[T]))
			leg = plt.legend()
			plt.show()
		elif (option_plot == 10):
			fig = go.Figure(data=[go.Table(header=dict(values=['Longitud de onda', 'Intensidad', 'Area']), cells=dict(values=[Max_X, Max_Y, Area_poits]))])
			fig.show()
	def close_window(): 
	    root.destroy()
	    exit()
	    
	#Graphic interface buttons
	#########################################################################
	my_button_flat_spec_inten = Button(root, text="Espectro - máximos intensidades", bg = '#00838F', fg='white', command=lambda: spectra_plot(1))
	my_button_flat_spec_inten.pack()
	my_button_final_spectra = Button(root, text="Espectro - Area picos", bg = '#00838F', fg='white', command=lambda: spectra_plot(2))
	my_button_final_spectra.pack()
	my_button_table_data = Button(root, text="Tabla de resultados", bg = '#00838F', fg='white', command=lambda: spectra_plot(10))
	my_button_table_data.pack()
	my_button_close = Button(root, text="Close", bg ='red', fg='white', command=close_window)
	my_button_close.pack()    
	root.mainloop()
#Calling the functions defined above
#########################################################################
matrix_data = file_to_matrix(file_name)
x, y = list_to_float(matrix_data)
#rango = [min(x), max(x)-3]
rango = [540, 600]
Xaux, Yaux = range1_to_range2(x, y, rango[0],rango[1])
Xaux2, Yaux2 = mins_in_spectra(x, y, rango[0],rango[1])
order = 8
plotting(Xaux, Yaux, Xaux2, Yaux2, order)