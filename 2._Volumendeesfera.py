import math
def radio():
    radio_esfera=float(input("Ingrese el radio de la esfera: "))
    volumen_esfera=(math.pi * radio_esfera**2) / 3
    print ("El volumen de la esfera es:",volumen_esfera)

radio()

