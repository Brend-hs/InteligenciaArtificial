# Codigo proporcionado por el profesor: 

def solve_maze(maze, start, end): #Se declara la función para resolver el laberinto
    stack = [start] #guarda la pocisión de inicio del laberinto en una pila
    while stack: #mientras la pila NO este vacia entra al bucle
        x, y = stack[-1] #se guarda la ultima posición de la pila en las variables "x" (fila) y "y" (columna)

        # Si se llega a la posición final, entonces:
        if (x, y) == end:
            return True, stack #regresa un True y la el camino que se ha seguido

        # Marca como visitado la posición del laberinto
        maze[x][y] = '2'

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]: #Se itera derecha, abajo, izquierda y arriba.
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]): #Condición de la posición, si esta dentro de los limites del laberinto entonces:
                if maze[nx][ny] == '0' or maze[nx][ny] == 'E': #Condición de la posición, si esa posición es un 0 o el estado E, entonces:
                    stack.append((nx, ny)) #Se añade a la pila la posición que se encontro
                    break #Se rompe el bucle for
        else: #Si no
            stack.pop() #Se realiza un pop a la pila

    return False, [] #Si no se encuentra una solución para el laberinto, entonces retorna un False y una pila vacia


if __name__ == "__main__":
    # 0 = camino abierto, 1 = muro, S = inicio, E = fin
    maze = [ #se crea la matriz, la cual será nuestro laberinto
        ['1', '1', '1', '1', '1'],
        ['S', '0', '1', '0', '1'],
        ['1', '0', '1', '0', '1'],
        ['1', '0', '0', '0', 'E'],
        ['1', '1', '1', '1', '1']
    ]

    start = (1, 0) #se coloca la posición desde la cual empieza el laberinto
    end = (3, 4) #se coloca la posición final del laberinto (el destino al cual debe llegar)
    solved, path = solve_maze(maze, start, end) #se manda a llamar a la función, la cual retornará la matriz resultante si se resolvio el laberinto, de igualmanera se retorna si se pudo resolver o no 

    if solved: #condición, si solved es verdadero, entonces:
        print("Maze Solved!") #se imprime que si se pudo resolver el laberinto
        for x, y in path: #Este for imprime el laberinto final en pantalla
            if maze[x][y] != 'S' and maze[x][y] != 'E': #condición, si es diferente de "S" y "E" entonces:
                maze[x][y] = '*' #Se imprimen los asteristos, los cuales significan la ruta que tomo el laberinto para poder llegar al destino
        for row in maze:
            print("".join(row))
    else: #condición, si solved NO es verdadero, entonces:
        print("No solution found.") #Se imprime que no se pudo resolver el laberinto
