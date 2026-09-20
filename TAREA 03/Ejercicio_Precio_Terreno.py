largo=(float(input("Ingrese largo del terreno:")))
ancho=(float(input("Ingrese ancho del terreno:")))
precio=(float(input("Precio del terreno es:")))

area=largo*ancho
precio=area*precio

if area > 1000:
    precio=precio*0.75
    
elif area > 500:
    precio=precio*0.83

print("El precio total del terreno es: ",precio)