#!/usr/bin/env python
#-*-encoding:utf-8-*-

# veremos los primeros pasos de la programacion orientada a objetos

class MiClaseEjemplo: # la clase va en camelcase y en singular
	"""Esto es un ejemplo 
	   Clase, objeto y métodos"""
	entrero = 4321
	def mensaje(self, msj): # una funcion dentro de un clase se le llama Metodos
		print(msj)
#instanciamos de la clase y asignamos el objeto a la variable
x = MiClaseEjemplo() 
y = MiClaseEjemplo()

print (x.entrero)
print (y.mensaje("hola :)"))
x.mensaje("mmm")