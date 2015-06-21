#!/usr/bin/env python
#-*-encoding:utf-8-*-

# Como funciona la estructura de control iterativa WHILE, veremos si el numero
# es positivo o negativo

respuesta = "si"

while respuesta == "si":
	numero = int(raw_input("ingresa un numero: "))
	if numero > 0:
		print "El numeor es positivo."
	elif numero < 0:
		print "El numero es negativo."
	else:
		print "El numero es 0."
	respuesta = raw_input("¿Quieres ingresar otro numero? (si/no)")