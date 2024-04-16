import heapq
import random

def generate_maze(rows, cols, wall_density):
    """
    Genera un laberinto aleatorio con las dimensiones dadas y densidad de paredes especificada.

    Args:
    - rows (int): Número de filas del laberinto.
    - cols (int): Número de columnas del laberinto.
    - wall_density (float): Densidad de paredes en el laberinto (valor entre 0 y 1).

    Returns:
    - list: Laberinto generado representado como una lista de listas.
    """
    maze = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if random.random() < wall_density:
                maze[i][j] = 1
    return maze

def heuristic(node, goal):
    """
    Calcula la heurística para el nodo dado utilizando la distancia de Manhattan.

    Args:
    - node (tuple): Coordenadas del nodo actual (fila, columna).
    - goal (tuple): Coordenadas del nodo objetivo (fila, columna).

    Returns:
    - int: Valor de la heurística.
    """
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def get_neighbors(node, maze, visited):
    """
    Obtiene los vecinos válidos (pasillos) del nodo dado en el laberinto y los marca como visitados.

    Args:
    - node (tuple): Coordenadas del nodo actual (fila, columna).
    - maze (list): Laberinto representado como una lista de listas.
    - visited (set): Conjunto de nodos visitados durante la búsqueda.

    Returns:
    - list: Lista de nodos vecinos válidos.
    """
    neighbors = []
    for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        neighbor = (node[0] + direction[0], node[1] + direction[1])
        if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]) and maze[neighbor[0]][neighbor[1]] == 0:
            neighbors.append(neighbor)
            visited.add(neighbor)
    return neighbors

def a_star(maze, start, goal):
    """
    Implementa el algoritmo A* para encontrar el camino más corto desde el nodo inicial hasta el nodo objetivo en un laberinto.

    Args:
    - maze (list): Laberinto representado como una lista de listas.
    - start (tuple): Coordenadas del nodo inicial (fila, columna).
    - goal (tuple): Coordenadas del nodo objetivo (fila, columna).

    Returns:
    - tuple: Tupla que contiene el camino encontrado y el conjunto de nodos visitados.
    """
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {(i, j): float('inf') for i in range(len(maze)) for j in range(len(maze[0]))}
    g_score[start] = 0
    f_score = {(i, j): float('inf') for i in range(len(maze)) for j in range(len(maze[0]))}
    f_score[start] = heuristic(start, goal)
    visited = set()

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1], visited

        for neighbor in get_neighbors(current, maze, visited):
            tentative_g_score = g_score[current] + 1
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None, None

def print_maze_with_path(maze, path, visited, start, goal):
    """
    Imprime el laberinto con el camino resaltado.

    Args:
    - maze (list): Laberinto representado como una lista de listas.
    - path (list): Lista de nodos que forman el camino encontrado.
    - visited (set): Conjunto de nodos visitados durante la búsqueda.
    - start (tuple): Coordenadas del nodo inicial (fila, columna).
    - goal (tuple): Coordenadas del nodo objetivo (fila, columna).
    """
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if (i, j) == start:
                print("S", end=" ")
            elif (i, j) == goal:
                print("G", end=" ")
            elif (i, j) in path:
                print("X", end=" ")
            elif (i, j) in visited:
                print(".", end=" ")
            elif maze[i][j] == 1:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()

def solve_random_maze():
    """
    Resuelve un laberinto aleatorio generado al azar.
    """
    maze_random = generate_maze(25, 25, 0.3)
    start_random = (0, 0)
    goal_random = (24, 24)

    path_random, visited_random = a_star(maze_random, start_random, goal_random)
    if path_random:
        print("Camino encontrado en el laberinto aleatorio:")
        print_maze_with_path(maze_random, path_random, visited_random, start_random, goal_random)
    else:
        print("No se encontró un camino en el laberinto aleatorio.")

def solve_fixed_maze():
    # Laberinto fijo
    maze_fixed = [
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    start_fixed = (0, 0)
    goal_fixed = (24, 24)

    path_fixed, visited_fixed = a_star(maze_fixed, start_fixed, goal_fixed)
    if path_fixed:
        print("\nCamino encontrado en el laberinto fijo:")
        print_maze_with_path(maze_fixed, path_fixed, visited_fixed, start_fixed, goal_fixed)
    else:
        print("No se encontró un camino en el laberinto fijo.")

def main():
    """
    Función principal que controla el flujo del programa.
    """
    while True:
        print("\n¿Qué laberinto desea resolver?")
        print("1. Laberinto Aleatorio")
        print("2. Laberinto Fijo")
        print("3. Salir")
        choice = input("Ingrese el número correspondiente a su elección: ")

        if choice == '1':
            solve_random_maze()
        elif choice == '2':
            solve_fixed_maze()
        elif choice == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese 1, 2 o 3.")

if __name__ == "__main__":
    main()

