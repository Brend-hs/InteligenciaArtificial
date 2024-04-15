import numpy as np

def simulated_annealing(func, x0, T, cooling_rate, max_iter):
    x = x0
    f_current = func(x)
    history = [(x, f_current)]
    
    for i in range(max_iter):
        T *= cooling_rate  # Enfriamiento exponencial
        x_new = x + np.random.normal(0, 1)  # Genera un nuevo punto
        f_new = func(x_new)
        
        # Calcula la diferencia de la función
        delta_E = f_new - f_current
        
        # Si el nuevo punto es mejor, acéptalo
        # Si no es mejor, acéptalo con una probabilidad que depende de la temperatura y delta_E
        if delta_E < 0 or np.exp(-delta_E / T) > np.random.random():
            x = x_new
            f_current = f_new
            history.append((x, f_current))
    
    # Devuelve el punto con el menor valor de la función encontrado
    x_min = min(history, key=lambda x: x[1])
    return x_min, history

# Definición de las funciones a minimizar
def f1(x):
    return x**4 + 3*x**3 + 2*x**2 - 1

def f2(x):
    return x**2 - 3*x - 8

# Parámetros del algoritmo
x0 = np.random.uniform(-10, 10)  # Punto inicial aleatorio
T_initial = 10.0  # Temperatura inicial
cooling_rate = 0.99  # Tasa de enfriamiento
max_iter = 1000  # Máximo número de iteraciones

# Aplicar templado simulado a cada función
min_f1, history_f1 = simulated_annealing(f1, x0, T_initial, cooling_rate, max_iter)
min_f2, history_f2 = simulated_annealing(f2, x0, T_initial, cooling_rate, max_iter)

# Mostramos el resultado
print("Minimo de f1(x):", min_f1)
print("Minimo de f2(x):", min_f2)
