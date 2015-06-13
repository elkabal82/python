#!/usr/bin/env python
#-*-encoding:utf-8-*-

#Crear una funcion que pida 2 valores y regrese el mayor

def saludo():
	'''Es un saludo de Bienvenida'''
 	nombre = raw_input("Hola, Cual es tu nombre: ") 
 	print "Hola", nombre, "bienvenido/a a mi primer script"
 	

def max2(): 
	num1 = raw_input("Ingresa el PRIMER valor: ")
	num2 = raw_input("Ingresa el SEGUNDO valor: ")
	if num1 > num2:
		print num1, " es mayor que ", num2
	if num2 > num1:
		print num2, " es mayor que ", num1
	if num1 == num2:
		print "Son iguales"

saludo()
max2()
