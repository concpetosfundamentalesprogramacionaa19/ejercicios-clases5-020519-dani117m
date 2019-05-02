"""
file: run3.py
autor: dani117m
///
nota mayor o igual a 18: sobresaliente 
///
nota mayor o igual a 16 y menor 
a 18: muy bueno

nota mayor o igual a 13 y menor 
a 16: buena 

nota menor a 13: insuficiente   
"""
from misvariables import*

# ingreso de datos 
nota = input ("Ingrese su nota 1: ")

# en python de utiliza esta funcion para pasar los datos a entero o viceversa 
nota = int(nota)
# solucion if para coprobar la nota y se aprobo o no 
if nota>=18:
	print("%s con nota %d" % ("Sobresaliente",nota))
else:
	if (nota >= 16) and (nota <= 17):
		print("%s con nota %d" % ("muy buena",nota))	
	else:
		if (nota >=13) and (nota <= 15):
			print("%s con nota %d" % ("buena",nota))
		else:
			print("%s con nota %d" % ("Insuficiente", nota))