# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 15:56:21 2021
Programa que determina si tres números correponden a los lados de un triángulo,
lo clasifica según sus lados y sus ángulos.


@author: Juancho1007
"""

#ENTRADA

print("Inserta a")
a=float(input())
print("inserta b")
b=float(input())
print("inserta c")
c=float(input())

#CALCULOS

#Desigualdad triangular
s=b+c
t=a+c
u=a+b

#Pitágoras
p_1=a**2+b**2
p_2=a**2+c**2
p_3=b**2+c**2

#AREA
sp=(a+b+c)/2
area=(sp*(sp-a)*(sp-b)*(sp-c))**(1/2)

#SALIDAS

if a<s and b<t and c<u: 
    print("hace un triángulo")

    if a==b and b==c and c==a: 
        print("Triángulo equilátero")
    elif a==b or b==c or a==c:
        print("triángulo isóceles")
    else:
        print("triángulo escaleno")
    
    if c**2==p_1 or b**2==p_2 or a**2==p_3:
        print("triángulo rectángulo")
    elif c**2>p_1 or b**2>p_2 or a**2>p_3:
        print("triángulo obtusángulo")
    else:
        print("triángulo agudo")
    print("perímetro", a+b+c)
    print("área", area)
else:
    print("no hace triángulo")
    


