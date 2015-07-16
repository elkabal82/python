#!usr/bin/env python
#-*-encoding:utf-8-*-

def saludo():
	"""Pide y almacena la palabra"""
	print "Hola bienvenido a este nuevo script"
	palabra = raw_input("Ingresa una palabra: ")
	return palabra


def confirmacion(palabra):
	"""Valida la palabra"""
	palabra = palabra.lower()
	if len(palabra) != 0 and palabra.isalpha() == True:
		print "perfecto"
		return palabra
	else:
		print "ingresa una palabra, si espacios, ni numeros"
		

