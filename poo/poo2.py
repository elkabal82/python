#!/usr/bin/env python
#-*-encoding:utf-8-*-

class MiPerro:
	"""Segundo ejemplo para el manejo y comprensión de clases, 
	   objetos y métodos. Con método __init__"""
	def __init__(self):
		"""Este metodo se se ejuta de inmediato cuando se instancia"""
		print("HOLA")

	def ladrar(self, ladrido):
		print(ladrido)

	def juego(self, jugar):
		print(jugar)

	def proteger(self, cuidar):
		print(cuidar)

gertrudis = MiPerro() # si lo ejetutamos ahora el script lo unico que saldria
parker = MiPerro() # HOLA, que tienen el metodo __init__

gertrudis.ladrar("Guau Guau soy gertrudis")
parker.ladrar("Guau Guau soy parker")