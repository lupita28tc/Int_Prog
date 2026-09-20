n1=(float(input("Dame el numero n1:")))
n2=(float(input("Dame el numero n2:")))
n3=(float(input("Dame el numero n3:")))

if n1 <= 0 or n2 <= 0 or n3 <= 0:
    print("Alguno o varios de los numeros no son positivos")

else:
    enteral1=int(n1)
    enteral2=int(n2)
    enteral3=int(n3)
    
    decimal1=round((n1 - int(n1))*10000)
    decimal2=round((n2 - int(n2))*10000)
    decimal3=round((n3 - int(n3))*10000)

    suma1= enteral1 + decimal1
    suma2= enteral2 + decimal2
    suma3= enteral3 + decimal3

    print("La suma resultante de n1 =",suma1)
    print("La suma resultante de n2 =",suma2)
    print("La suma resultante de n3 =",suma3)

    mayor=max(suma1,suma2,suma3)
    print("El mayor de las sumas es:", mayor)