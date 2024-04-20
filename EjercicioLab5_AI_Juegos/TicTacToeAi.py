import copy  # Importa el módulo copy para realizar copias profundas de objetos
import random  # Importa el módulo random para generar números aleatorios

# Función para imprimir el tablero
def imprimir_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))  # Imprime cada fila del tablero con " | " como separador
        print("-" * 5)  # Imprime una línea horizontal para separar las filas

# Función para verificar si alguien ha ganado
def verificar_ganador(tablero):
    # Verificar filas
    for fila in tablero:
        if fila.count(fila[0]) == len(fila) and fila[0] != "-":
            return fila[0]  # Si todas las celdas en una fila son iguales y no están vacías, hay un ganador

    # Verificar columnas
    for col in range(len(tablero[0])):
        if all(tablero[fila][col] == tablero[0][col] and tablero[fila][col] != "-" for fila in range(len(tablero))):
            return tablero[0][col]  # Si todas las celdas en una columna son iguales y no están vacías, hay un ganador

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != "-":
        return tablero[0][0]  # Si las celdas en la diagonal principal son iguales y no están vacías, hay un ganador
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != "-":
        return tablero[0][2]  # Si las celdas en la diagonal secundaria son iguales y no están vacías, hay un ganador

    # Si no hay ganador
    return None

# Función para generar y almacenar todos los posibles movimientos restantes
def generar_movimientos(tablero, jugador):
    movimientos = []

    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if tablero[i][j] == "-":  # Verifica si la celda está vacía
                nuevo_tablero = copy.deepcopy(tablero)  # Copia el tablero para modificarlo sin afectar el original
                nuevo_tablero[i][j] = jugador  # Realiza el movimiento del jugador en la celda vacía
                movimientos.append(nuevo_tablero)  # Agrega el nuevo tablero a la lista de movimientos posibles

    return movimientos

# Función para que la computadora realice su movimiento de forma bruta
def movimiento_computadora(tablero):
    movimientos = generar_movimientos(tablero, "O")  # Genera todos los posibles movimientos de la computadora
    return random.choice(movimientos)  # Elige aleatoriamente uno de los movimientos posibles

# Función para imprimir los movimientos posibles
def imprimir_movimientos_posibles(tablero):
    movimientos_posibles = generar_movimientos(tablero, "O")  # Genera todos los posibles movimientos de la computadora
    print("Movimientos posibles de la computadora:")
    for i, movimiento in enumerate(movimientos_posibles):
        print(f"Posible movimiento {i+1}:")
        imprimir_tablero(movimiento)  # Imprime cada posible movimiento de la computadora

# Función principal del juego
def juego_gato():
    tablero = [["-" for _ in range(3)] for _ in range(3)]  # Inicializa un tablero vacío de 3x3
    jugador_actual = "X"  # El jugador X comienza el juego

    while True:  # Bucle principal del juego
        imprimir_tablero(tablero)  # Imprime el tablero actual

        resultado = verificar_ganador(tablero)  # Verifica si hay un ganador

        if resultado:  # Si hay un ganador o empate, termina el juego
            print("Resultado:", resultado)
            break

        if jugador_actual == "X":  # Turno del jugador humano
            print("Turno del jugador humano")
            fila = int(input("Ingrese el número de fila (0, 1, 2): "))
            columna = int(input("Ingrese el número de columna (0, 1, 2): "))

            if tablero[fila][columna] == "-":  # Verifica si la celda seleccionada está vacía
                tablero[fila][columna] = jugador_actual  # Realiza el movimiento del jugador humano
                jugador_actual = "O"  # Cambia al turno de la computadora
                imprimir_movimientos_posibles(tablero)  # Muestra los movimientos posibles de la computadora
            else:
                print("¡Esa casilla ya está ocupada! Intente nuevamente.")
        else:  # Turno de la computadora
            print("Turno de la computadora")
            tablero = movimiento_computadora(tablero)  # La computadora realiza su movimiento
            jugador_actual = "X"  # Cambia al turno del jugador humano

# Inicia el juego
juego_gato()
