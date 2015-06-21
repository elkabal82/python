#!/usr/bin/env python
#-*-encoding:utf-8-*-

# Crearemos una tabla de multiplicar utilizando la estructura de control 
# iterativa FOR

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

tabla = int(raw_input("¿Que tabla de multiplicar quieres:? "))

for numero in lista:
	print  numero, " x ", tabla, " = ",  numero * tabla
