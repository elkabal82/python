#!/usr/bin/env python
#-*-encoding:utf-8-*-

def saludo():
	'''pide el nombre para hacer un saludo'''
	nombre = raw_input("Hola,  ¿Cual es tu nombre? ")
	print "Bienvenido", nombre, "a mi script"

def suma():
	num1 = int(raw_input("Ingresa el primer numero: "))
	num2 = int(raw_input("Ingresa el segundo numero: "))
	print "la suma es: ", num1 + num2

