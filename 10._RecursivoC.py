import math
def siete():

    suma=0
    cad=""
    n = int(input("n numeros para elevar al cuadrado: "))
    for q in range(1,n+1):
        c=pow(q,2)
        cad=cad+" "+str(c)
        suma+=c
    print(cad)
    print("La suma de los cuadrads es: ", suma)
siete()
