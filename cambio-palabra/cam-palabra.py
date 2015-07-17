#!/usr/bin/env python
#-*-encoding:utf-8-*-

#Este escrip consiste en que, tienen que ingresar una palabra y el scrip 
#cambia la palabra segun las siguientes reglas.
#1.-Si la palabra empieza con vocal, solo se le agrega al final de la palabra
#"ie"
#2.-Si temina en consonante, se quita la primera letra y se coloca al final de
#la palabra + el "ie"
#NOTA: esta idea fue sacada de www.codecademy.com

import modulos

palabra = modulos.saludo()
palabra2 = modulos.confirmacion(palabra)
#print palabra2
if palabra2 != None:
	modulos.traduccion(palabra2)
else:
	print "no es una palabra correcta"