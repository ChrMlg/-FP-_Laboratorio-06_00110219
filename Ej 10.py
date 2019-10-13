import os
def menu ():

    os.system('clear')

    print ("MENU DE OPCIONES")
    print ("1. Convertidor de Celcius a Farenheit")
    print ("2. Convertidor de Celcius a Kelvin")
    print ("3. Convertidot de Farenheit a Kelvin ")
    print ("4. Convertidor de Farenheit a Celcius")
    print ("5. Convertidor de kelvin a Farenheit")
    print ("6. Convertidor de Kelvin a Celcius")

   

    

def fCelFar(x):
    Far=(x*(9/5))+32
    return (Far)

def fCelKel(x):
    Kel=x+273
    return (Kel)

def fFarKel(x):
    Kel=273+fFarCel(x)
    return (Kel)

def fFarCel(x):
    Cel=(x-32)*(5/9)
    return (Cel)

def fKelFar(x):
    Far=(fKelCel(x)*(9/5))+32
    return(Far)

def fKelCel(x):
    Cel=x-273
    return(Cel)


Bans=""
while (Bans!="N"):
    menu()
    ans=int(input("Escoja una opción: "))

    if (ans==1):
        Cel=int(input("Digite temperatura en grados Celcius: "))
        print ("La conversión de ",Cel," grados Celcius a Farenheit es: ",(float(fCelFar(Cel))))

    if (ans==2):
        Cel=int(input("Digite temperatura en grados Celcius: "))
        print ("La conversión de ",Cel," grados Celcius a Kelvin es: ",(float(fCelKel(Cel))))

    if (ans==3):
        Far=int(input("Digite temperatura en grados Farenheit: "))
        print ("La conversión de ",Far," grados Farenheit a Kelvin es: ",(float(fFarKel(Far))))

    if (ans==4):
        Far=int(input("Digite temperatura en grados Farenheit: "))
        print ("La conversión de ",Far," grados Farenheit a Celcius es: ",(float(fFarCel(Far))))

    if (ans==5):
        Kel=int(input("Digite temperatura en Kelvin: "))
        print ("La conversión de ",Kel," Kelvin a grados Farenheit es: ",(float(fKelFar(Kel))))

    if (ans==6):
        Kel=int(input("Digite temperatura en Kelvin: "))
        print ("La conversión de ",Kel," Kelvin a grados Celcius es: ",(float(fKelCel(Kel))))

    Bans=str(input("Desea Continuar? (S)i   (N)o    :   "))

    if (Bans=="N"):
        print("Gracias por Hacer uso del programa xd")