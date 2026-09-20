n=int(input("Numero de terminos?:"))
if n <= 0:
    print("Error,el numero debe ser mayor que cero")
else:
    producto=1
    for i  in range (1, n + 1):
        if i % 2 == 1:
            producto = producto * (i + 1) / i
        else:
            producto = producto * i / (i + 1)
        
    pi = 2 * producto 
    print ("Valor aproximado de pi=", round (pi, 4))
        