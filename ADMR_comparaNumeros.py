#Comparar numero aleatorio con uno ingresado
import random

num = int(input("Ingresa un numero: "))
numR = random.randrange(100)
print("Numero aleatorio",numR)

def mayor(num,numR):
    if num>numR:
        print("Numero mayor",num) 
    else :
        print("Numero mayor",numR)

print(mayor(num,numR))
