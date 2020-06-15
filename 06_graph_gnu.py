'''Programa que:
Lee 2 archivos, uno con la direccion de la carpeta de interés y otro con los comandos para plotear.
Con concatenaciones de direcciones ejecuta un comando en la terminal para llamar a gnuplot.
Le dice que se ubique en la direccion de interes.
Plotea con los comandos proporcionados.
El ploteo lo guarda en un PNG.
'''

#By Edgar Lara
#26-may-2020

import os
os.system("clear") #For clear te screen

i=0
cad_0 = "C:/Gnuplot/gnuplot/bin/gnuplot.exe "
cad_1 = "-p "
cad_2 = "/nombre.gnu"
#print(cad_1)

#Abirmos el prueba.txt y obtenemos la direccion que tiene guardada
f = open('prueba.txt','r')
cad_3 = list(f.read()) #Se tiene que pasar a lista para poder cambiar un caracter de esta, en string no se puede
print(cad_0)
f.close()
len_cadena = len(cad_3)
#print("longitud: " +str(len_cadena))

#Intercambio de un caracter en la cadena
while (i < len_cadena):
	if (cad_3[i]=="\\"):
		cad_3[i]="/"
	i += 1
cad_3="".join(cad_3) #ya intercambiado el caracter pasamos la lista de nuevo a str
cad_0 += cad_1 + cad_3 + cad_2		#concatenación


#print(cad_0)
#print(type(cad_0))
os.system(cad_0)
print(cad_0)
input()