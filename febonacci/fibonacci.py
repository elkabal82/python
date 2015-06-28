#!/etc/usr/env python
#-*-encoding:utf-8-*-

# Secuencia feebonacci
# 0+1=1
# 1+1=2
# 1+2=3
# 2+3=5

def fib(n):
	"""muestra la serie de fibonacci
	   hasta el numero n """
	x, y = 0, 1
	while x < n:
		print x
		x, y = y, x+y
		print "fin del siclo , X=", x, "Y= ", y
		
	

n = int(raw_input("ingresa el fin de la lista fibonacci"))
fib(n)

raw_input()
#x=0 1
#y=2 