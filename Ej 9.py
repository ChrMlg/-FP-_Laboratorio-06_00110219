print ("Especifique un rango de numeros")
RI=int(input("Digite un numero inicial : "))
RF=int(input("Digite un numero final: "))
MUL=int(input("Digite un numero de el cual se quiera saber sus multiplos dentro del rango especificado: "))
i=0
if (RF>RI):
    
    AUX=RI
    while(RI<RF-MUL):
        
        RI=RI+1
        if (RI==AUX):
            print("Los multiplos de ",RI," son: ",MUL)
        if (RI%MUL==0):
            print (RI,end=", ")
print ("y",RI+MUL,".")

if (RI>RF):
    
    AUX=RF
    while(RF<RI-MUL):
        
        RF=RF+1
        if (RF==AUX):
            print("Los multiplos de ",RF," son: ",MUL)
        if (RF%MUL==0):
            print (RF,end=", ")
print ("y",RF+MUL,".")





