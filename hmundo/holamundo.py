#!/usr/bin/env python
#-*-coding:utf-8-*-

# Solo es el famoso hola mundo
def saludo():
	'''Es un saludo de Bienvenida'''
	#pide y almacena la información en la variable nombre
 	nombre = raw_input("Hola, Cual es tu nombre: ") 
 	print "Hola", nombre, "bienvenido a mi primer script"
 	#Lo usamos para un salto de linea
 	raw_input() 
 
saludo() #llamamos a la funcion
print "hola mundo"
