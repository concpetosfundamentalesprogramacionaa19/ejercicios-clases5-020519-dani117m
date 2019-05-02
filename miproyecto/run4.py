"""
file: run4.py
autor: dani117m
///
deseamos saber el valor de una carra universitaria 
el valor promedio de cada ciclo es de 1200 dolares 
el valor promedio del seguro educativo es de 100 dolares si la edad del estudiante(por ciclo) es menor o igual a 20 
caso contrario sera de 150 $
si el estudiante tiene una modalidad a distancia el numero de ciclo a seguir es de 10 
caso contrario debera seguir 8 ciclos 
obtener la proyecion costo total de la carrera de un estudiante 

"""
#from misvariables import*

# ingreso de datos 
modalidad = input ("1:Precencial\t2:Distancia\nIngrese la modalidad elegida")
edad = input("Ingrese su edad")
# en python de utiliza esta funcion para pasar los datos a entero o viceversa 

modalidad = int(modalidad)
edad = int(edad) 

seguro = 100
seguro2 = 150
ciclo = 1200

# solucion if para coprobar la nota y se aprobo o no 
if modalidad = 1:
	costo = 8*ciclo
	print(" con nota" )
else:
	if = modalidad = 2:
		costo = 10*ciclo
		print("%s con no" )	

if (edad<=20) and (modalidad=1):
	costo2 = 100*
	print("%s con nota %d" % ("buena",nota))
else:
	costo2 = 
	print("%s con nota %d" % ("Insuficiente", nota))