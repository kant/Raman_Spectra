'''Programa que imprime el codigo ASCII

By Edgar Lara
26-may-2020
'''
#limpiar terminal
import os
os.system("clear")

i=0

#por alguna razon algunos caracteres entre 127 y 160 lanza error en terminal
while (i < 255):
	if(i<127) or (i>160):
		print(str(i) + ": " + str(chr(i)))
	#print(chr(i))
	#if (i%10 == 0):
		#	print("\n")
	i += 1

#print(chr(160))