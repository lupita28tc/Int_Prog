monto=(float(input("Monto de la compra $:")))
descuento=0
if monto < 500:
    descuento = 0
elif monto <1000:
    descuento = 0.05
elif monto < 7000:
    descuento =  0.10
elif monto < 15000:
    descuento = 0.15
else:
    descuento = 0.25

total=monto - (monto*descuento)
print("El total a pagar incluye el descuento es $: ",total)