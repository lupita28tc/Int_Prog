numero = int(input("Dame un número entero positivo: "))
suma = 0
for divisor in range(1, numero + 1):
    if numero % divisor == 0:
        suma = suma + divisor
print("La suma de todos sus divisores menores o iguales es el es:")
print(suma)