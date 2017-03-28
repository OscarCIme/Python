import math
def siete():
    
    cad=""
    n = int(input("n numeros para elevar al cuadrado: "))
    a = 100
    for q in range(1,n+1):
        c=pow(q,2)
        if (c>=a):
            cad=cad+" "+str(c)
    print(cad)
siete()
