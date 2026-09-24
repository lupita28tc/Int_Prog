inicio_ciclo_exterior = int(input("Dame el inicio del ciclo exterior: "))
fin_ciclo_exterior = int(input("Dame el fin del ciclo exterior: "))
inicio_ciclo_interior = int(input("Dame el inicio del ciclo interior: "))
fin_ciclo_interior = int(input("Dame el fin del ciclo interior: "))

if inicio_ciclo_exterior <= fin_ciclo_exterior and inicio_ciclo_interior <= fin_ciclo_interior:
    i = inicio_ciclo_exterior
    while True:
        print(f"T A B L A = {i}")
        
        j = inicio_ciclo_interior
        while True:
            print(f"{i} X {j} = {i * j}")
            j += 1
            if j > fin_ciclo_interior:  
                break
                
        i += 1
        if i > fin_ciclo_exterior: 
            break