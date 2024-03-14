import random

minimo = 0
maximo = 1000000000000

num = int(input(f"Escriba un numero entre {minimo} y {maximo}. "))
encontrado = False
mitad = (maximo+minimo)//2
numero = mitad

while not encontrado:
    print(numero)
    if numero < num:
        print("El número correcto es más grande.")
        minimo = numero
        mitad = (maximo+minimo)//2
        numero = mitad

    elif numero > num:
        print("El número correcto es más pequeño.")
        maximo = numero
        mitad = (maximo+minimo)//2
        numero = mitad
    else:
        print("El número es igual!")
        encontrado = True


