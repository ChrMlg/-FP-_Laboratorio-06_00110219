
num=int(input("Digite un numero: "))    #DECLARACION DE VARIABLES
txt=str(num)                            #CONVERSION DE INT A STR
size=len(txt)                           
last=txt[size-1]
i=0 #ITERADOR
invert=0    #VARIABLE CLAVE
i2=size #AUXILIAR DE PARAMETRO
while(i<i2):
    i=i+1   #COUNTER
    invert=size-1
    size=invert
    if (i==1):
        print("El numero con sus digitos invertidos es: ")
    print((txt[invert]),end="") #"end="" evita que el print se haga en diferentes lineas de codigo
    if (i==i2):
        break
print (" ") #ruptura de "end="""

