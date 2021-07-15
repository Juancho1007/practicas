# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 15:28:20 2021

@author: Juan David
"""
#ingreso de dato
print("inserte ancho rectangulo ")
ancho=float(input())
print("inserte largo rectangulo")
largo=float(input())

#calculo
perimetro=(ancho+largo)*2
area=(ancho*largo)
diagonal=((ancho)**(2)+(largo)**(2))**(1/2)

#resultados
print("perimetro: ",perimetro)
print("area ",area)
print("diagonal ",diagonal)

