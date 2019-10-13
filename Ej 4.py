import random

xh=0
intentos=0
ym = random.randint(1,10)
while (xh!=ym):
    intentos = intentos + 1
    
    xh = int(input("Digite el numero que pensó: "))
    if (xh>10)or(xh<1):
        print("Su numero no cumple con el parametro indicado")
    if (xh<ym):
        print("El numero es menor al de la maquina")
    if (xh>ym):
        print("El numero es mayor al de la maquina")
    if (xh==ym):
        print("Acertaste :D")
print("Su numero de intentos fue de: ",intentos)
   