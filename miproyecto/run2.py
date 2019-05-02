"""
file: run2.py
autor: dani117m

"""
from misvariables import*


nota = input ("Ingrese su nota 1: ")
nota2 = input("Ingrese su nota 2: ")

nota = int(nota)
nota2 = int(nota2)

if nota>=18:
	print("%s con nota: %d" % (mensaje,nota))
else:
	print("%s con nota %d" % (mensaje2,nota))	

if nota2>=18:
	print("%s con nota: %d" % (mensaje,nota2))
else:
	print("%s con nota: %d" % (mensaje2,nota2))