numero = int(input("Elige un número: "))
respuesta = int(input("Ahora tienes que intentar acertar el número: "))
while respuesta != numero:
    if respuesta > numero:
        print("Tu número es mayor que el número correcto")
    elif respuesta < numero:
        print("Tu número es menor que el número correcto")
    respuesta = int(input("Ahora tienes que intentar acertar el número: "))
print("El número es el correcto.")

#########################################################

numero = int(input("Elige un número: "))
fin = False
while not fin:
    respuesta = int(input("Ahora tienes que intentar acertar el número: "))
    if respuesta > numero:
        print("Tu número es mayor que el número correcto")
    elif respuesta < numero:
        print("Tu número es menor que el número correcto")
    else:
        fin = True

print("El número es el correcto.")
