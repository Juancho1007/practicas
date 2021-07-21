# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 15:38:33 2021

@author: Juan David
"""
print("desea iniciar? S/N")
opcion=input()
while opcion=="s" or opcion=="S":

#entrada
    print("Inserte numero 1")
    print()
    n_1=int((input()))
    print()
    print("Inserte número 2")
    print()
    n_2=int(input())
    print()

#comparación
    if n_1>n_2:
        a=n_1
        b=n_2
    elif n_1<n_2:
        b=n_1
        a=n_2
    else:
        print("Los números tienen el mismo valor, terminando")

#cálculo
    r=a%b
    if r==0:
        print("mcd=",b)
    else:
        while r>0:
            R=r
            r=b%r
            b=R
        print("mcd=",R)
    print("desea seguir calculando? S/N: ")
    opcion=input()