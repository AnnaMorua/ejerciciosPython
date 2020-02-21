#Longitud de una cadena

def longitudCadena(x):
  cont=0
  for i in x:
    cont+=1
  return cont
def cadena(x):
  y=x.lower()
  return y[0].upper()+y[1:]
x=input("Ingresa una palabra y te dré la cantidad de caracteres:  ") or 'mADRId'
print(cadena(x),'tiene',longitudCadena(x),'caracteres.')
