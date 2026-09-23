while True:
  a=float(input("Ingrese a:"))
  b=float(input("Ingrese b:"))
  op=input("Operación (+,-,*,/):")

  match op:
    case "+":
        resultado = a + b
        print("Resultado:",resultado)
    case "-":
        resultado = a - b
        print("Resultado:",resultado)
    case "*":
        resultado = a * b
        print("Resultado:",resultado)
    case "/":
        if b == 0:
           print("Error: no se puede dividir entre cero.")
        else:
           resultado = a / b
           print("Resultado:",resultado)
          
    case _:
        print("Operación no válida.")
        
  otra = input ("Quieres hacer otra operación? (si/no):").lower()
  if otra != "s" and otra != "si":
    print ("Programa terminado")
    break
 
 