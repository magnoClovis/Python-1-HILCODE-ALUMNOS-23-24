"""
1: Pedir un numero al primero jugador
2: Pedir que el segundo jugador intente adivinar el número
3: Repetir hasta que el segundo jugador adivine el número
"""
import random

def entrada():
    return int(input("Escribe un número"))

def adivinar(numero):
    fin = False
    while not fin:
        res = int(input("Adivine el número "))
        if res < numero:
            print("Tu número es menor que el número correcto")
        elif res > numero:
            print("Tu número es mayor que el número correcto")
        else:
            print("Has adivinado el número")
            fin = True

# numero = entrada()
# adivinar(numero)

num = random.randint(0,10)
print(num)

num = random.randrange(0,10)
print(num)








