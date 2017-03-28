def cuatro():
   A=0
   B=0
   C=0
A=int(input("ingrese un numero\n"))
B=int(input("ingrese otro numero\n"))
C=int(input("ingrese un nuemero\n"))

if(A > B and A > C):
 print("El numero mayor es " + str(A))
else:
 if(B > A and B > C):
  print("El numero mayor es " + str(B))
 else:
  print("El numero mayor es " + str(C))
cuatro()
