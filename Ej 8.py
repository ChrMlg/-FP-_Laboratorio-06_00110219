mult=(int(input("Digite numero, se le mostraran las tablas de multiplicacion de dicho numero: ")))
i=0
tab=mult
while (i!=9):
    i=i+1
    mult=mult-1
    print (tab,"*",i,"=",tab*i)