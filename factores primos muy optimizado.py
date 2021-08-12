# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 16:20:20 2021

@author: arell
"""
#bibliotecas
from math import sqrt

#Proceso: utiliza una fubnción para los cálculos
def prime_factors(num):
    #esta función recoge todos los factores primos del número dado e imprime la descomposición
    prime_factors_list = [] #crea una lista vacía donde se guardarán los factores primos
    while num % 2 == 0:  #caso que el número sea par
        prime_factors_list.append(2)
        num /= 2
    for i in range(3, int(sqrt(num))+1, 2):
        if num % i == 0:
            prime_factors_list.append(i)
            num /= i
    if num > 2:
        prime_factors_list.append(int(num))
    
    lista_pd=list(set(prime_factors_list))
    lista_power=list()
    
    #para guardar una lista con las potencias de cada primo
    for z in lista_pd:
        pow=prime_factors_list.count(z)
        lista_power.append(pow)
    
    #salida de la función
    for par in zip(lista_pd, lista_power): 
    	print("(",par[0],"^", par[1],") ", end="")


#entrada
print("Descomposición en factores primos")
print()
print("Muestra la descomposición factorial del número escogido por usted")
print()
opcion=input("¿Desea iniciar? S/N     ")

while opcion=="S" or opcion=="s" or opcion=="si" or opcion=="sí":
#opciones para mantener el programa corriendo, en el caso de ser una de ellas, correrlo

#opciones para mantener el programa corriendo, en el caso de ser una de ellas, correrlo
    
    n = int(input("Ingrese un número: "))
    print()
    print("La descomposición factorial del número es: ")
    print()
    prime_factors(n)
    print()
    
 #condicion para continuar
    print("¿Desea continuar con otro número? S/N")
    opcion=input()
    print()

#fin de programa
print("Terminado")