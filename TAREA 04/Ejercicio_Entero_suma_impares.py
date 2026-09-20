numero1 = int(input("Dame el primer numero entero positivo:"))
numero2 = int(input("Dame el segundo numero entero positivo:"))

if numero1 < numero2:
    inicio = numero1
    fin=numero2
else:
    inicio=numero2
    fin=numero1
suma=0
for numero in range (inicio,fin + 1):
    if numero % 2 !=0:
        suma = suma + numero 
print("La suma de los numeros impares entre los numeros que me diste es:",suma)