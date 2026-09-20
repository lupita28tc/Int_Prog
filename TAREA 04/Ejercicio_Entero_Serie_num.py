n= int(input("Dame un numero:"))
f= 0

print("Segun la funcion, la serie es:", f, end="")

for x in range (1, n + 1):
    f= 2 * f + x**2
    print(f,end="")