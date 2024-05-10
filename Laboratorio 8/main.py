import pandas as pd
import matplotlib.pyplot as plt

# Carga de los datos de entrenamiento y prueba
train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')


def crearGrafica(claseflor):
    #Creamos las clases para la asignación de colores
    clases=['Iris-setosa','Iris-versicolor','Iris-virginica']
    colores=['red','blue','green']
    # Crear la figura y el eje
    fig, ax = plt.subplots()
    # Dibujar una línea en y=0 para la recta numérica
    ax.plot([0, train_data[claseflor].max()+0.2], [0, 0], 'k-', lw=2)
    # Graficar puntos por cada clase con un color diferente
    for clase, color in zip(clases, colores):
        puntos_clase = train_data[train_data['class'] == clase][claseflor]
        ax.plot(puntos_clase, [0]*len(puntos_clase), 'o', label=clase, color=color)
    # Configuraciones adicionales del gráfico
    ax.set_xlim([0, train_data[claseflor].max()+0.2])
    ax.set_ylim([-0.5, 0.5])
    ax.yaxis.set_visible(False)
    ax.legend(title="Recta del Atributo "+claseflor+" por Clase")
    # Mostrar la gráfica
    plt.show()

def clasificador_Length(data_class):
    #Creamos variables para contar el numero de objetos de cada clase
    clase_1, clase_2, clase_3 = 0,0,0
    resultado = {}
    #Clasificacion del atributo petallenght
    for datos in data_class:
        #Crearemos los umbrales para la clasificacion de cada clase
        if datos <= 1.8:
            clase_1+=1
        elif datos > 1.8 and datos <= 4.9:
            clase_2+=1
        else:
            clase_3+=1
    print("Numero de objetos Petal Length de la clase Iris-sentosa: ",clase_1)
    print("Numero de objetos Petal Length de la clase Iris-versicolor: ",clase_2)
    print("Numero de objetos Petal Length de la clase Iris-virginica: ",clase_3)

def clasificador_Width(data_class):
    #Creamos variables para contar el numero de objetos de cada clase
    clase_1, clase_2, clase_3 = 0,0,0
    #Clasificacion del atributo petalwidth
    for datos in data_class:
        #Crearemos los umbrales para la clasificacion de cada clase
        if datos <= 0.6:
            clase_1+=1
        elif datos > 0.6 and datos <= 1.7:
            clase_2+=1
        else:
            clase_3+=1
    print("Numero de objetos Petal Width de la clase Iris-sentosa: ",clase_1)
    print("Numero de objetos Petal Width de la clase Iris-versicolor: ",clase_2)
    print("Numero de objetos Petal Width de la clase Iris-virginica: ",clase_3)


#crearGrafica('petallength')
#crearGrafica('petalwidth')
clasificador_Length(test_data['petallength'])
clasificador_Width(test_data['petalwidth'])



