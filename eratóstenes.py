# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math 

#entrada
print("Criba de Eratóstenes")
print()
print("Muestra los números primos hasta el número escogido por usted")
print()
opcion=input("¿Desea iniciar? S/N     ")

while opcion=="S" or opcion=="s" or opcion=="si" or opcion=="sí":
#opciones para mantener el programa corriendo, en el caso de ser una de ellas, correrlo
    
    n = int(input("Ingrese un número: "))
    print()

#proceso
    #Cantidad de numeros  primos hasta n


    lista_p = list(range(2, n+1))

    i = 0
    
    while(lista_p[i]*lista_p[i] <= n):
    #Mientras el cuadrado del elemento actual sea menor que el último elemento (Teorema)
        for num in lista_p:
            if num <= lista_p[i]:
                #Cada iteración del while hace que el for comience desde el primer elemento,esto es para omitir los números primos ya encontrados
                continue
            elif num % lista_p[i] == 0:
                # Si un número es divisible entre el elemento actual del while, entonces eliminarlo de la lista
                lista_p.remove(num)
            else:
               # Si no es divisible, entonces no hacer nada
               pass
        i += 1 #Incrementa al siguiente elemento de la lista
    
    #esta es la cantidad de primos
    cantidad_primos=len(lista_p)


    #Divisores de n 

    #crear listas para la nueva iteración de los divisores
    lista_d = list()
   
    j = 1
    
    while j<=n:
    #para cada entero menor o igual que n se ejecuta el while
        if n%j==0:
        #si el entero j actual del whiledivide exactamente a n, agregarlo a la lista
            lista_d.append(j)
        else:
        #si no lo divide exactamente no hacer nada
            pass
        j+=1#incrementa al siguiente entero
    
    # Esta es la cantidad de divisores
    cantidad_div=len(lista_d)

    #Suma de los divisores
    suma=sum(lista_d)
    
    #primos relativos
    
    #se crea una lista desde 1 hasta n
    enteros=list(range(1,n+1))
    #se crea una lista vasia para guardar los relativos
    relativos=list()
    
    for whole in enteros:
    #Una interación para el conjunto de enteros menores o iguales a n
        if math.gcd(whole,n)==1:
        #si el maximo común divisor entre el elemento actual del for y n es 1, añadirlo a la lista relativos
            relativos.append(whole)
        else: 
        #de lo contrario no hacer nada
            pass
    
    #primalidad
    if n in lista_p:
    #si n esta en la lista de primos decir que es primo
        primalidad="EL número es primo"
    
    else:
    #De lo contrario decir que es compuesto
        primalidad="El numero es compuesto"
    
    #perfecto
    
    #UN número es perfecto si es igual a la suma de sus divisores propios
    sumita=suma-n
    #Suma los divisores propios
    if sumita==n:
    #si cumple la deficion de perfectos decir que es perfecto
        perfect="El número es perfecto"
    else:
        #si no cumple la deficiion de perfectos decir que no es perfecto
        perfect="El número no es perfecto"



    #salida
    
    print("los números primos hasta ",n," son: ")
    print()          
    print(lista_p)
    print()
    print("la cantidad de primos hasta ",n," es: ",cantidad_primos)
    print()
    print("los divisores de ",n," son: ")
    print()          
    print(lista_d)
    print()
    print("la cantidad de divisores de ",n," es: ",cantidad_div)
    print()
    print("La suma de los divisores de ",n,": ",suma)
    print()
    print("Los primos relativos con ",n,": ",relativos)
    print()
    print(primalidad)
    print()
    print(perfect)
    print()
    
    #condicion para continuar
    print("¿Desea continuar con otro número? S/N")
    opcion=input()
    print()

#fin de programa
print("Terminado")