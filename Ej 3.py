x=0
while (x%2==0)or(ans=="S"):
    x=int(input("Digite un numero par: "))
    if (x%2!=0):
        print("el numero ingresado no es par")
        break
    ans=str(input("Desea continuar: (S)i (N)o"))
print("FIN")


