print ("***CAJA***")
print ("precio de pelicula 1")
x=int(input())
print ("precio de pelicula 2")
y=int(input())
print ("precio de pelicula 3")
z=int(input())
if (x>y and x>z):
    B=y+z
    print ("su total a pagar es" , B)
elif (y>x and y>z):
    B=x+z
    print ("su total a pagar es" ,  B)
elif (z>x and z>y):
    B=x+y
    print ("su total a pagar es" , B)
