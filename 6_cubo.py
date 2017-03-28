import math
def seis():
    cad=""
    n = int(input("n numeros para elevar al cubo: "))
    
    for q in range(1,n+1):
        cad=cad+" "+str(pow(q,3))
    print(cad)
seis()
