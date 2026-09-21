mes=int(input("Escribe el numero del mes :"))
match mes:
    case 1|2|12:
        print ("Invierno")
    case 3|4|5:
        print ("Primavera")
    case 6|7|8:
        print ("Verano")
    case 9|10|11:
        print( "Otoño")
    case _:   
        print ("Error")
