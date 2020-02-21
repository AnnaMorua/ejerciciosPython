#Area de circulo
"""Calcula el area de un circulo segun su radio o diametro"""
import math

medida = int(input("Ingresar medida conocida del circulo. 1)Radio 2)Diametro"))
pi = 3.1416

    if medida == 1:
        r = float(input("Ingresa el radio del circulo: "))
        r2 = math.pow(r,2)
        a = r2*pi
        print("El area del circulo es: ")
        print(a)
    elif medida == 2:
        d = float(input("Ingresa el diametro del circulo"))
        r = d/2
        r2 = math.pow(r,2)
        a = r2*pi
        print("El area del circulo es: ")
        print(a)
    else:
        print("Operación no válida")
