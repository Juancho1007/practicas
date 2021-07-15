# -*- coding: utf-8 -*-
"""
Created on Wed May 19 11:15:42 2021

@author: Juancho
"""
print("primer medida")
a=(int(input("Introduce la hora:  ") ))
b=(int(input("Introduce el minuto:  ") ))
c=(int(input("Introduce el segundo:  ") ))
print("segunda medida")
d=(int(input("Introduce la hora:  ") ))
e=(int(input("Introduce el minuto:  ") ))
f=(int(input("Introduce el segundo:  ") ))
z=c+f #suma los segundos
S=z%60#segundos
y=(z-S)/60#segundos sobrantes
print(S,"seg")
o=b+e
u=o+y
M=y+o%60#minutos
m=M%60
if u>59:
    w=1
else:
    w=0
print(m,"min")
h=a+d+w
print(h,"hr")