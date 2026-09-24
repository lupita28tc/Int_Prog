inicio_ciclo_exterior = int(input("Dame el inicio del ciclo exterior: "))
fin_ciclo_exterior = int(input("Dame el fin del ciclo exterior: "))
inicio_ciclo_interior = int(input("Dame el inicio del ciclo interior: "))
fin_ciclo_interior = int(input("Dame el fin del ciclo interior: "))

for i in range(inicio_ciclo_exterior, fin_ciclo_exterior + 1):
    print(f"T A B L A = {i}")
    for j in range(inicio_ciclo_interior, fin_ciclo_interior + 1):
        print(f"{i} X {j} = {i * j}")