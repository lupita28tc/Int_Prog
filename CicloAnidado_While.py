inicio_ciclo_exterior = int(input("Dame el inicio del ciclo exterior: "))
fin_ciclo_exterior = int(input("Dame el fin del ciclo exterior: "))
inicio_ciclo_interior = int(input("Dame el inicio del ciclo interior: "))
fin_ciclo_interior = int(input("Dame el fin del ciclo interior: "))

i = inicio_ciclo_exterior
while i <= fin_ciclo_exterior:
    print(f"T A B L A = {i}")
    
    j = inicio_ciclo_interior
    while j <= fin_ciclo_interior:
        print(f"{i} X {j} = {i * j}")
        j += 1  
        
    i += 1