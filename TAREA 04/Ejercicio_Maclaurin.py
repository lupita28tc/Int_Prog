x = float(input("Teclee argumento x?: "))

if x <= -1 or x >= 1:
    print("Error, valor de x inválido")
else:
    n = int(input("Hasta cuantos términos de la serie: "))

    suma = 0
    signo = 1

    for i in range(1, n + 1):

        termino = signo * (x ** i) / i
        suma = suma + termino

        signo = signo * -1

    print("ln(1+x) =", round(suma, 6))
                    