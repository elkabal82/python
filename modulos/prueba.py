#!/usr/bin/env python
#-*-encoding:utf-8-*-

#(import nombre del modulo)
#(import paquete.modulo as como la llamaremos despues)
#(from paquete.modulo import constante)

#import modulos as m
#m.saludo()
#m.suma()

#import modulos
#modulos.saludo()
#modulos.suma()

'''PEP 8: importación
La importación de módulos debe realizarse al comienzo del
documento, en orden alfabético de paquetes y módulos.
Primero deben importarse los módulos propios de Python.
Luego, los módulos de terceros y finalmente, los módulos propios
de la aplicación.
Entre cada bloque de imports, debe dejarse una línea en blanco. '''

from modulos import saludo, suma
import this

saludo()
suma()

