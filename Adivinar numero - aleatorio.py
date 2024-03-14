import random

minimo = 0
maximo = 1000000

num = int(input("Escriba un numero entre 0 y 10. "))
encontrado = False

numero = random.randrange(minimo,maximo) # random.randrange(inicio, fin)
while not encontrado:
    if numero < num:
        print("El número elegido es más grande.")
        numero = random.randrange(minimo,maximo) # random.randrange(inicio, fin)

    elif numero > num:
        print("El número elegido es más pequeño.")
        numero = random.randrange(minimo,maximo) # random.randrange(inicio, fin)
    else:
        print("El número es igual!")
        encontrado = True

    print(numero)
