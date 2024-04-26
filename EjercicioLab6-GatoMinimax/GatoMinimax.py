import random
import time

def imprimir_tablero(tablero):
    for fila in tablero:
        print("|".join(fila))
        print("-----")

def verificar_ganador(tablero, jugador):
    for fila in tablero:
        if all(cell == jugador for cell in fila):
            return True

    for i in range(3):
        if all(tablero[j][i] == jugador for j in range(3)):
            return True

    if all(tablero[i][i] == jugador for i in range(3)) or \
       all(tablero[i][2 - i] == jugador for i in range(3)):
        return True

    return False

def verificar_empate(tablero):
    return all(all(cell != " " for cell in row) for row in tablero)

def mover_jugador(tablero, jugador):
    while True:
        fila = int(input(f"Jugador {jugador} - Ingrese el número de fila (0, 1, 2): "))
        columna = int(input(f"Jugador {jugador} - Ingrese el número de columna (0, 1, 2): "))
        if tablero[fila][columna] == " ":
            tablero[fila][columna] = jugador
            break
        else:
            print("¡Esa casilla ya está ocupada! Intenta de nuevo.")

def minimax(tablero, jugador):
    if verificar_ganador(tablero, "X"):
        return -1
    elif verificar_ganador(tablero, "O"):
        return 1
    elif verificar_empate(tablero):
        return 0

    if jugador == "O":
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == " ":
                    tablero[i][j] = jugador
                    score = minimax(tablero, "X")
                    tablero[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == " ":
                    tablero[i][j] = jugador
                    score = minimax(tablero, "O")
                    tablero[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

def mejor_movimiento(tablero, jugador):
    best_move = None
    best_score = float('-inf') if jugador == "O" else float('inf')
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == " ":
                tablero[i][j] = jugador
                score = minimax(tablero, "X" if jugador == "O" else "O")
                tablero[i][j] = " "
                if jugador == "O":
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
                else:
                    if score < best_score:
                        best_score = score
                        best_move = (i, j)
    return best_move

def mover_computadora(tablero, jugador):
    print(f"La Computadora ({jugador}) está pensando...")
    time.sleep(1)
    fila, columna = mejor_movimiento(tablero, jugador)
    print(f"La Computadora ({jugador}) ha jugado en la fila {fila}, columna {columna}.")
    tablero[fila][columna] = jugador


def jugar_gato_computadora_vs_computadora():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugadores = ["X", "O"]
    jugador_actual = jugadores[0]

    while True:
        imprimir_tablero(tablero)

        mover_computadora(tablero, jugador_actual)

        if verificar_ganador(tablero, jugador_actual):
            imprimir_tablero(tablero)
            print(f"¡El jugador {jugador_actual} ha ganado!")
            break

        if verificar_empate(tablero):
            imprimir_tablero(tablero)
            print("¡Empate!")
            break

        jugador_actual = jugadores[1] if jugador_actual == jugadores[0] else jugadores[0]

def jugar_gato():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugadores = ["X", "O"]
    jugador_actual = jugadores[0]

    while True:
        imprimir_tablero(tablero)

        if jugador_actual == "X":
            mover_jugador(tablero, jugador_actual)
        else:
            mover_computadora(tablero, jugador_actual)

        if verificar_ganador(tablero, jugador_actual):
            imprimir_tablero(tablero)
            print(f"¡El jugador {jugador_actual} ha ganado!")
            break

        if verificar_empate(tablero):
            imprimir_tablero(tablero)
            print("¡Empate!")
            break

        jugador_actual = jugadores[1] if jugador_actual == jugadores[0] else jugadores[0]

if __name__ == "__main__":
    print("¡Bienvenido al juego de Gato (Tic Tac Toe)!")
    print("Modo de juego:")
    print("1. Humano vs Computadora")
    print("2. Computadora vs Computadora")
    modo = input("Seleccione el modo de juego (1 o 2): ")

    if modo == "1":
        jugar_gato()
    elif modo == "2":
        jugar_gato_computadora_vs_computadora()
    else:
        print("Modo de juego no válido. Por favor, seleccione 1 o 2.")
