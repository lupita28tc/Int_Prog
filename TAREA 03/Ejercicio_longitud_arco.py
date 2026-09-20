import math 
H=float(input("Ingrese la altura: "))
W=float(input("Ingrese el ancho: "))

X= H / W

A= math.sqrt(X**2 + 1/16)
B= math.log(X + math.sqrt(X**2 + 1/16))
C= math.log (4)
S= 2 * W * (A + (1/(16*X)) * (B + C))

print("La longitud de arco de la parabola es:", S)