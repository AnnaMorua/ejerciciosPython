#Mayor y menor de dos numeros

import math

def mayor():
    if n1>n2:
        print("Mayor",n1)
    else:
        print("Mayor",n2)
        
def menor():
    if n2<n1:
        print("Menor",n2)
    else:
        print("Menor",n1)

n1 = int(input("Ingresa el primer numero: "))
n2 = int(input("Ingresa el segundo numero: "))


print(mayor()," ",menor())
