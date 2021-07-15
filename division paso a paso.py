# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 10:17:47 2021

@author: Juan David
"""

"""
Spyder Editor

This is a temporary script file.
"""
a=(input("Introduce el dividendo:  ") )
b=(input("Introduce el divisor:  ") )
A=int(a)
B=int(b)
if A<B :  #si el dividendo es menor que el divisor
    c=A//B
    r=A-B*c
    print("el residuo es: ", r, " y el cociente es: ", c)
else:
    lista_a = [ ]
    lista_b=[ ]
    while A>0:
        m=A%10
        A=A/10
        lista_a.append(m)
    lista_b.reverse()
    while B>0:
        n=B%10
        B=B/10
        lista_b.append(n)
    lista_b.reverse()
    digitos_a=len(lista_a)
    digitos_b=int(len(lista_b))
    partir_a= a[:(digitos_b) ]
    print(digitos_a)
    print(partir_a)
    


    
##print("6. pntenciacion")
##opcion=int(input())
##if opcion==1:
##    print("la suma es: ",a+b)
##elif opcion==2:
##    print("la resta es: ", a-b)
##elif opcion==3:
#    print("la mulptiplicacion es: ", a*b)
#elif opcion==4:
#    print("la division es:", a/b)
#elif opcion==5:
#    A=int(a)
#    B=int(b)
#    c=A//B
#    r=A-B*c
#    print("el residuo es:", r)
#elif opcion==6:
#    print("la poteciacion es:", a**b)