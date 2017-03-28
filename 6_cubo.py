import math
def seis():
    suma=0
    cad=""
    n = int(input("n numeros para elevar al cubo: "))
    for q in range(1,n+1):
        C=pow(q,3)
        cad=cad+" "+str(C)
        suma+=C
    print(cad)
    print("La suma de los cuadrads es: ", suma)
seis()
