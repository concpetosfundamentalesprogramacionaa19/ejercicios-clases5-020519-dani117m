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
modalidad = input ("1:Precencial\t2:Distancia\nIngrese la modalidad elegida\n")
edad = input("Ingrese su edad\n")
# en python de utiliza esta funcion para pasar los datos a entero o viceversa 
#
modalidad = int(modalidad)
edad = int(edad) 
costo = int
costo1 = int
ciclo = int 
costot = int 
# solucion en esta primera parte se decide q tipo de modalidad se sige y segun el mismo se altera la variable ciclo 
if (modalidad == 1) :
	ciclo = 8
	costo = 1200*ciclo	
else:
	ciclo = 10
	costo = 1200*ciclo
# en la funcion edad se lee que tipo de seguro se va a dar utilisando la variable ciclo anteriormente asiganada 	
if (edad <= 20) :
	costo1 = 100*ciclo
else:
	costo1 = 150*ciclo
# aquie se hace la suma total para obtener el valor total de tramite 
costot = costo+costo1 
print("El precio total de la carrera mas el seguro es de %d" % (costot))