"""
1. 5 rondas 👌🏾
2. Si elige algo diferente de piedra, papel o tijeras,
   hay que pedir otro valor, hasta que se pase un valor valido por teclado
3. Decir el vencedor de cada ronda, y sumarle 1 punto. Decir también si hay empate
4. Decir el ganador final (el jugador con más puntos), enseñar los puntos de
   los dos jugadores.
"""
puntos_j1 = 0
puntos_j2 = 0
empates = 0
eleccion_jugador1 = ""
eleccion_jugador2 = ""

for rondas in range(0,5):
    eleccion_jugador1 = input("Jugador 1, cuál eliges: Piedra, papel o tijeras? ")
    eleccion_jugador1 = eleccion_jugador1.lower()
    while not(eleccion_jugador1 == "piedra" or eleccion_jugador1 == "papel" or eleccion_jugador1 == "tijeras"):
        print("")
        print(eleccion_jugador1, "no es una opción valida.")
        eleccion_jugador1 = input("Jugador 1, cuál eliges: Piedra, papel o tijeras? ")
        eleccion_jugador1 = eleccion_jugador1.lower()

    eleccion_jugador2 = input("Jugador 2, cuál eliges: Piedra, papel o tijeras? ")
    eleccion_jugador2 = eleccion_jugador2.lower()
    while not(eleccion_jugador2 == "piedra" or eleccion_jugador2 == "papel" or eleccion_jugador2 == "tijeras"):
        print("")
        print(eleccion_jugador2, "no es una opción valida.")
        eleccion_jugador2 = input("Jugador 2, cuál eliges: Piedra, papel o tijeras? ")
        eleccion_jugador2 = eleccion_jugador2.lower()

    if eleccion_jugador1 == "piedra" and eleccion_jugador2 == "tijeras":
        print("Punto al jugador 1.")
        puntos_j1 += 1 # lo mismo que puntos = puntos + 1
    elif eleccion_jugador1 == "papel" and eleccion_jugador2 == "piedra":
        print("Punto al jugador 1.")
        puntos_j1 += 1 # lo mismo que puntos = puntos + 1
    elif eleccion_jugador1 == "tijeras" and eleccion_jugador2 == "papel":
        print("Punto al jugador 1.")
        puntos_j1 += 1 # lo mismo que puntos = puntos + 1
    elif eleccion_jugador1 == eleccion_jugador2:
        print("Empate. Nadie suma puntos")
        empates += 1
    else:
        print("Punto al jugador 2.")
        puntos_j2 += 1 # lo mismo que puntos = puntos + 1

print("El jugador 1 tiene", puntos_j1,"puntos.")
print("El jugador 2 tiene", puntos_j2,"puntos.")
print("Total de empates:", empates)
if puntos_j1 > puntos_j2:
    print("Gana el jugador 1.")
elif puntos_j2 > puntos_j1:
    print("Gana el jugador 2.")
else:
    print("Nadie gana. Empate")
