# Escribe tu código aquí :-)
puntos_j1 = 0
puntos_j2 = 0
empates = 0
eleccion_jugador1 = ""
eleccion_jugador2 = ""
opciones = ["papel", "piedra", "tijeras"]
indice_ganador = opciones.index("piedra")-opciones.index("tijeras")
for rondas in range(0,5):
    eleccion_jugador1 = input("Jugador 1, cuál eliges: Piedra, papel o tijeras? ")
    eleccion_jugador1 = eleccion_jugador1.lower()
    while eleccion_jugador1 not in opciones:
        print("")
        print(eleccion_jugador1, "no es una opción valida.")
        eleccion_jugador1 = input("Jugador 1, cuál eliges: Piedra, papel o tijeras? ")
        eleccion_jugador1 = eleccion_jugador1.lower()

    eleccion_jugador2 = input("Jugador 2, cuál eliges: Piedra, papel o tijeras? ")
    eleccion_jugador2 = eleccion_jugador2.lower()
    while eleccion_jugador2 not in opciones:
        print("")
        print(eleccion_jugador2, "no es una opción valida.")
        eleccion_jugador2 = input("Jugador 2, cuál eliges: Piedra, papel o tijeras? ")
        eleccion_jugador2 = eleccion_jugador2.lower()
    # opciones = ["piedra", "papel", "tijeras"]
    # opciones[-2]
    # opciones[1]
    # opciones[1]
    indice = opciones.index(eleccion_jugador1)-opciones.index(eleccion_jugador2)
    if opciones[indice]==opciones[indice_ganador]:
        print("Punto al jugador 1.")
        puntos_j1 += 1 # lo mismo que puntos = puntos + 1
    elif indice == 0:
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
