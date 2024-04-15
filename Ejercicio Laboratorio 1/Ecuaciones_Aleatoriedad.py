from random import randint

def GeneraArrayAleatorios():
    aleatorios = []
    #Con el siguiente for vamos a generar un arreglo de 4 elementos con numeros enteros aleatorios.
    for i in range(0,4):
        #Utilizamos el metodo randint para generar un numero aleatorio entero entre -70 - 0 y lo guardamos en el arreglo en la posicion correspondiente
        aleatorios.append(randint(-100,101))
    return aleatorios

def DistanciaEuclidiana(solucion, aleatorios):
    #Generamos una variable donde vamos a guardar la suma
    sum = 0
    for i in range(0,4):
        #Sumamos el cuadrado de la diferencia de los elementos respectivos de cada arreglo
        sum += (solucion[i]-aleatorios[i])**2
    #Regresamos la raiz cuadrada de la suma
    return sum ** 0.5

def SimilitudCoseno(solucion, aleatorios):
    #Calcularemos las magnitudes de cada uno de los vectores y el producto punto

    #Creamos la variable para guardar la magnitud del vector solucion
    m_solucion = 0
    #Creamos la variable para guardar la magnitud del vector aleatorios
    m_aleatorios = 0
    #Creamos la variable para guardar el producto punto de los vectores
    pp = 0
    for i in range(0,4):
        #Calculamos la suma del cuadrado de cada elemento del vector solucion
        m_solucion += solucion[i]**2
        #Calculamos la suma del cuadrado de cada elemento del vector aleatorios
        m_aleatorios += aleatorios[i]**2
        #Calculamos el producto punto
        pp += solucion[i] * aleatorios[i]
    #Terminamos de calcular la magnitud del vector solucion
    m_solucion = m_solucion ** 0.5
    #Terminamos de calcular la magnitud del vector aleatorios
    m_aleatorios = m_aleatorios ** 0.5
    
    #Retornamos el coseno del angulo entre los vectores
    return pp/(m_solucion*m_aleatorios)


if __name__ == '__main__':
    #Declaramos un arreglo con los resultados correctos
    solucion = [-36,-64,-4,-64]
    #Declaramos un arreglo en donde vamos a guardar los numeros aleatorios
    aleatorios = []

    #Llammamos a la funcion para generar nuestro arreglo de numeros aleatorios
    aleatorios = GeneraArrayAleatorios()
    #Imprimimos los valores
    print(f'El vector generado fue: {aleatorios}')

    #A continuacion vamos a calcular la distancia euclidiana entre los vectores para ver que tan similares son, asi que llamamos a la funcion que lo hace
    d_Euclidiana = DistanciaEuclidiana(solucion,aleatorios)
    #Imprimimos la distancia
    print(f'La distancia entre los vectores es: {d_Euclidiana}')

    #A continuacion vamos a calcular la similitud coseno entre vectores para ver que tan similares son, asi que llamamos a la funcion que lo hace
    coseno = SimilitudCoseno(solucion, aleatorios)
    #Imprimimos el coseno similitud
    print(f'El coseno similitud entre los vectores fue: {round(coseno,1)}')
