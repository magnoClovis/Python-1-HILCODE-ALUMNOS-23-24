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

def cambiar_posiciones(posiciones, jugador1, jugador2):

    eleccion_j1 = int(input("¿Dónde quieres jugar? Elija un número entre 1 y 9. "))
    while eleccion_j1 < 1 or eleccion_j1 > 9 or posiciones[eleccion_j1] != " ":
        print("Valor invalido, elija un número entre 1 y 9.")
        eleccion_j1 = int(input("¿Dónde quieres jugar? Elija un número entre 1 y 9. "))
    posiciones[eleccion_j1] = jugador1
    print(posiciones)

    eleccion_j2 = int(input("¿Dónde quieres jugar? Elija un número entre 1 y 9. "))
    while eleccion_j2 < 1 or eleccion_j2 > 9 or posiciones[eleccion_j2] != " ":
        print("Valor invalido, elija un número entre 1 y 9.")
        eleccion_j2 = int(input("¿Dónde quieres jugar? Elija un número entre 1 y 9. "))
    posiciones[eleccion_j2] = jugador2
    print(posiciones)

tabla = dibuja_tabla()
print(tabla)

jugador1, jugador2 = pregunta()

posiciones = crear_lista()
cambiar_posiciones(posiciones, jugador1, jugador2)














































































































































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
