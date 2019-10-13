import sys
EA = 1000
EV = EA
res = 1001
sum = 0
print ("***PROGRAMA DE CAJERO AUTOMÁTICO***")
name = str(input("Para acceder a su cuenta, digite su nombre"))
print("Bienvenido ",name,"el saldo actual de su cuenta bancaria es: $", EA ," USD." )
af = str(input("Desea hacer una transaccion? (S)i , (N)o"))
if (af=="N"):
    print("Gracias por hacer uso el sistema BHC")
    sys.exit(0)
if (af=="S"):
    print ("Que tipo de transaccion desea realizar?")
    ans=str(input("(R)etiro     (A)bono"))
    if (ans=="R"):
        while (res > EA):
            res = int(input("Cuanto desea retirar?: "))
            if (res>EA):
                print ("La cantidad de dinero que desea retirar es superior a su saldo actual")
        EA = EA - res
    if (ans=="A"):
        sum = int (input("Cuanto desea abonar?: "))
        EA = EA + sum

print ("Su saldo viejo era de: $", EV," USD")
print ("Su saldo actual ahora es de: $",EA,"USD")




    
