#Código proporcionado por el profesor:
#Antes de comenzar a analizar el código comentamos algunas de sus lineas para poder tener un mejor entendimiento sobre como funciona
from collections import deque #Importa clase "deque" del modulo "collections"

def solve_maze(maze, start, end): #Se declara la función para resolver el laberinto
    queue = deque([(start, [start])]) #Inicializa una cola llamada queue utilizando deque
    while queue: #Inicia un bucle while que se ejecutará mientras haya elementos en la cola.
        (x, y), path = queue.popleft() #Dentro del bucle, extrae una tupla de la cola utilizando popleft(), que extrae el elemento de la izquierda de la cola.

        # Si se llega a la posición final, entonces:
        if (x, y) == end:
            return True, path #regresa un True y la el camino que se ha segu

        # Mark as visited
        maze[x][y] = '2'

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]: #Se itera derecha, abajo, izquierda y arriba.
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]): #Condición de la posición, si esta dentro de los limites del laberinto entonces:
                if maze[nx][ny] == '0' or maze[nx][ny] == 'E': #Condición de la posición, si esa posición es un 0 o el estado E, entonces:
                    queue.append(((nx, ny), path + [(nx, ny)])) #se agrega un nuevo elemento a la cola
                    if maze[nx][ny] != 'E':
                        maze[nx][ny] = '2'

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
    solved, path = solve_maze(maze, start, end)  #se manda a llamar a la función, la cual retornará la matriz resultante si se resolvio el laberinto, de igualmanera se retorna si se pudo resolver o no 

    if solved: #condición, si solved es verdadero, entonces:
        print("Maze Solved!") #se imprime que si se pudo resolver el laberinto
        for x, y in path: #Este for imprime el laberinto final en pantalla
            if maze[x][y] != 'S' and maze[x][y] != 'E': #condición, si es diferente de "S" y "E" entonces:
                maze[x][y] = '*' #Se imprimen los asteristos, los cuales significan la ruta que tomo el laberinto para poder llegar al destino
        for row in maze:
            print("".join(row))
    else: #condición, si solved NO es verdadero, entonces:
        print("No solution found.") #Se imprime que no se pudo resolver el laberinto
