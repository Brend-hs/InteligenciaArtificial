import numpy as np

# Funcion para cargar los datos del archivo
def cargar_datos(archivo):
    # Se define el nombre de las columnas
    nombres_columnas = ['Columna_1', 'Columna_2', 'Columna_3', 'Categoria']
    
    # Cargando los datos desde el archivo .data, asumiendo que esta en el mismo directorio que este script
    datos = np.genfromtxt(archivo, delimiter=',', names=nombres_columnas)
    
    return datos

# Funcion para calcular promedio, varianza y desviacion estandar de una columna numerica
def calcular_estadisticas(columna):
    promedio = np.mean(columna)
    varianza = np.var(columna)
    desviacion_estandar = np.std(columna)
    
    return promedio, varianza, desviacion_estandar

# Funcion para separar los datos por categoria y calcular estadisticas para cada categoria
def calcular_estadisticas_por_categoria(datos):
    categorias_unicas = np.unique(datos['Categoria'])
    estadisticas_por_categoria = {}
    
    for categoria in categorias_unicas:
        # Filtrar los datos por la categoria actual
        datos_categoria = datos[datos['Categoria'] == categoria]
        
        # Separar las columnas numericas
        columnas_numericas = datos_categoria[['Columna_1', 'Columna_2', 'Columna_3']]
        
        # Calcular estadisticas para cada columna numerica
        estadisticas_columnas = {}
        for columna in columnas_numericas.dtype.names:
            estadisticas_columnas[columna] = calcular_estadisticas(columnas_numericas[columna])
        
        # Agregar estadisticas por categoria al diccionario
        estadisticas_por_categoria[categoria] = estadisticas_columnas
    
    return estadisticas_por_categoria

# Archivo de datos
archivo = 'bezdekIris.data'

# Cargar los datos
datos = cargar_datos(archivo)

# Calcular estadisticas para todas las columnas numericas
estadisticas_totales = {}
for columna in datos.dtype.names[:-1]:  # Excluyendo la ultima columna que es la categoria
    estadisticas_totales[columna] = calcular_estadisticas(datos[columna])

# Calcular estadisticas por categoria
estadisticas_por_categoria = calcular_estadisticas_por_categoria(datos)

# Mostrar resultados
print("Estadisticas totales:")
for columna, estadisticas in estadisticas_totales.items():
    print(f"{columna}:")
    print(f"  Promedio: {estadisticas[0]}")
    print(f"  Varianza: {estadisticas[1]}")
    print(f"  Desviacion estandar: {estadisticas[2]}")
    print()

print("Estadisticas por categoria:")
for categoria, estadisticas_columnas in estadisticas_por_categoria.items():
    print(f"Categoria: {categoria}")
    for columna, estadisticas in estadisticas_columnas.items():
        print(f"  {columna}:")
        print(f"    Promedio: {estadisticas[0]}")
        print(f"    Varianza: {estadisticas[1]}")
        print(f"    Desviacion estandar: {estadisticas[2]}")
    print()
