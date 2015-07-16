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
		print "ingresa una palabra, sin espacios, ni numeros"

def traduccion(palabra):
	"""Hace el cambio de la palabra"""
	add = "ei"
	print "Ahora vamos a cambiar tu palabra"
	if palabra[0] == "a" or palabra[0] == "e" or palabra[0] == "i" or palabra[0] == "o" or palabra[0] == "u":
		palabra = palabra + add
		print palabra
	else:
		letra = palabra[0]
		palabra = palabra[1:] + letra + add 
		print palabra
		

