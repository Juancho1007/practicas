# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 15:11:23 2021

@author: arell
"""
#entrada
print("Descomposición en factores primos")
print()
print("Muestra la descomposición factorial del número escogido por usted")
print()
opcion=input("¿Desea iniciar? S/N     ")

while opcion=="S" or opcion=="s" or opcion=="si" or opcion=="sí":
#opciones para mantener el programa corriendo, en el caso de ser una de ellas, correrlo
    
    n = int(input("Ingrese un número: "))
    print()

#proceso
    #Numeros  primos hasta n


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


    #divisores primo de n
    
    lista_pd=list()

    for x in lista_p:
        if x in lista_d:
            lista_pd.append(x)
        else:
            pass
    
    #descomposición extensa
    lista_fc=list()
    
    for y in lista_pd:
        k=1
        while n%(y**k)==0:
            lista_fc.append(y)
            k+=1
    
    #cantidad de veces que aparece el primo en la descomposición
    lista_power=list()
    
    for z in lista_pd:
        pow=lista_fc.count(z)
        lista_power.append(pow)
            
   



    #salida
    """
    print(lista_p)
    print()
    print(lista_d)
    print()
    print(lista_pd)
    print()
    print(lista_fc)
    print()
    print(lista_power)
    """
    print("La descomposición factorial del número es el producto de: ")
    #obtiene el par de cada iteración y lo imprime
    for par in zip(lista_pd, lista_power): 
    	print(par[0],"^", par[1])
    
    
    #condicion para continuar
    print("¿Desea continuar con otro número? S/N")
    opcion=input()
    print()

#fin de programa
print("Terminado")




















