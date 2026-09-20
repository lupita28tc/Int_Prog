numero = int(input("Dame un número para verificar si es perfecto: "))

while numero != 0:

    if numero < 0:
        print("El", numero, "no es positivo")

    else:
        suma = 0

        for divisor in range(1, numero):
            if numero % divisor == 0:
                suma = suma + divisor

        if suma == numero:
            print("El", numero, "sí es perfecto")
        else:
            print("El", numero, "no es perfecto")

    numero = int(input("Dame un número para verificar si es perfecto: "))

print("Fin de algoritmo")