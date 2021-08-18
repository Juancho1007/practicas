# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 16:30:50 2021

@author: arell

Programa que calcula el area de un polígono regular en función de los valores
ingresado por el usuario "número de lados" y "longitud del lado"

"""
#clases
import math
class poligono:
    def __init__(self,numero,longitud):
        self.numero=numero
        self.longitud=longitud
    def area(self):
        self.angulo=(360/self.numero)/2
        self.radian=math.radians(self.angulo)
        self.apotema=(self.longitud/2)/math.tan(self.radian)
        self.area=(self.numero*self.longitud*self.apotema)/2
        print("El área es: ",self.area)

#Entrada
print("Ingrese número de lados")
print()
cantidad=int(input())
print()
print("Ingrese medida de los lados")
print()
medida=float(input())
print()

#cálculos
figura=poligono(cantidad,medida)

#salida
print()
figura.area()
        
