#!/usr/bin/env python
#-*-encoding:utf-8-*-

# vamos a ver los tipos de datos que utiliza python

entero = 10
real = 13.595
cadena = "Hola mundo"
tipo_bool = True
tuplas = ("hola", 3, True,  # no se puede modificar y van entre ()  
		 (5, "hola", 5))  
listas = [6, "hola",  # si se pueden modificar despues de creadas y van / [] 
		 3.678, False]  
diccionario = {"autor":"Pancho", "clave2":4}  # van entre {}

print entero
print real
print cadena
print tipo_bool
print tuplas
print listas
print diccionario["autor"]