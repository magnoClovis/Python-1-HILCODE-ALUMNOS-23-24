# Escribe tu código aquí :-)

dinero = float(input("Cuánto dinero tienes?"))
chuche = 1
pastel = 3.5
pan = 0.85
nocilla = 3.5
compra = chuche + pastel + pan + nocilla

print("Total de la compra:", compra)
if dinero >= compra:
    print("Compra aceptada.\nTienes ahora", dinero - compra,"euritos en la tarjeta.")
else:
    print("Tarjeta denegada (es decir, eres pobre)")
    print("Te faltan:", compra - dinero, "euritos.")

#########################################################################
num = int(input("Numero: "))

if num > 50:
    print("El número es mayor que 50.")
elif num == 50:
    print("EL número es 50.")
elif num < 50:
    print("El número es menor que 50.")
elif num < 50 or num == 50:
    print("El número es menor o igual que 50.")
elif num > 50 or num == 50:
    print("El número es mayor o igual que 50.")
else:
    print("Que número???")


if num > 50 and num < 100:
    print("El numero está entre 50 y 100.")
elif num < 50 or num > 100:
    print("El número no está entre 50 y 100.")
else:
    print("El número o es 50 o es 100.")


if num > 50 and num < 100:
    print("El numero está entre 50 y 100.")
else:
    if num < 50 or num > 100:
        print("El número no está entre 50 y 100.")

    else:
        print("El número o es 50 o es 100.")
