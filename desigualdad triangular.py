#Programa que determina si tres números correponden a los lados de un triángulo
print("Inserta a")
a=float(input())
print("inserta b")
b=float(input())
print("inserta c")
c=float(input())
s=b+c
t=a+c
u=a+b
if a<s and b<t and c<u: 
    print("hace un triangulo")
else:
    print("no hace triangulo")
    
