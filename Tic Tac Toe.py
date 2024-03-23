def dibuja_tabla():
    tabla = """
     |       |
     |       |
     |       |
--------------------
     |       |
     |       |
     |       |
--------------------
     |       |
     |       |
     |       |
"""
    return tabla

def pregunta():
    opciones = ("X", "O")
    jugador1 = input("¿Que eliges, la 'X' o la 'O'? ")
    jugador1 = jugador1.upper()
    while jugador1 not in opciones:
        print("INVALIDO.")
        print("¿'X' o 'O'?")
        jugador1 = input("¿Que eliges, la 'X' o la 'O'? ")
        jugador1 = jugador1.upper()

    if jugador1 == opciones[0]:
        jugador2 = opciones[1]
    else:
        jugador2 = opciones[0]

    return jugador1, jugador2

def crear_lista():
    posiciones = ["@", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    return posiciones

def cambiar_posiciones(posiciones, jugador):
    eleccion = int(input("¿Dónde quieres jugar? Elija un número entre 1 y 9. "))
    while eleccion < 1 or eleccion > 9 or posiciones[eleccion] != " ":
        print("Valor invalido, elija un número entre 1 y 9.")
        eleccion = int(input("¿Dónde quieres jugar? Elija un número entre 1 y 9. "))
    posiciones[eleccion] = jugador
    print(posiciones)

def victoria(tabla, jugador):
    ganador = False
    if tabla[1] == jugador and tabla[2] == jugador and tabla[3] == jugador:
        ganador = jugador
    elif tabla[4] == jugador and tabla[5] == jugador and tabla[6] == jugador:
        ganador = jugador
    elif tabla[7] == jugador and tabla[8] == jugador and tabla[9] == jugador:
        ganador = jugador

    elif tabla[1] == jugador and tabla[4] == jugador and tabla[7] == jugador:
        ganador = jugador
    elif tabla[2] == jugador and tabla[5] == jugador and tabla[8] == jugador:
        ganador = jugador
    elif tabla[3] == jugador and tabla[6] == jugador and tabla[9] == jugador:
        ganador = jugador

    elif tabla[1] == jugador and tabla[5] == jugador and tabla[9] == jugador:
        ganador = jugador
    elif tabla[3] == jugador and tabla[5] == jugador and tabla[7] == jugador:
        ganador = jugador

    elif " " not in tabla:
        ganador = -1

    return ganador

tabla = dibuja_tabla()
print(tabla)
posiciones = crear_lista()
jugador1, jugador2 = pregunta()
ganador = False

while ganador not in ("X", "O", -1):
    cambiar_posiciones(posiciones, jugador1)
    ganador = victoria(posiciones, jugador1)
    print(ganador)
    if ganador not in ("X", "O", -1):
        cambiar_posiciones(posiciones, jugador2)
        ganador = victoria(posiciones, jugador2)

print("El ganador es: ", ganador)

















































































































































def click2(punto):
    x = punto[0]
    y = punto[1]
    fila = int()
    columna = int()
    colu_enc = False
    fila_enc = False

    tabla = [   [1,2,3],
                [4,5,6],
                [7,8,9] ]

    i = 100
    j = 0

    while i <= 300 and not (colu_enc and fila_enc):
        if y // i == j:
            fila = y//i
        j = 0
        while j < 3 and not fila_enc and not colu_enc:
            if x // i == j:
                columna = x // i
                colu_enc = True
            j+=1

        i+=100

    posicion = tabla[fila][columna]
    return posicion
