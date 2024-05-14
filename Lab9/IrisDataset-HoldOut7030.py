from sklearn.datasets import load_iris #Carga el conjunto de datos de Iris
from sklearn.model_selection import train_test_split #Funcion para dividir conjuntos de datos en conjuntos de entrenamiento y prueba 
import numpy as np 

# Conjunto de datos Iris
iris = load_iris()
X = iris.data
y = iris.target

# Se divide el conjunto entre entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y)

# Proporcion de clases en los conjuntos de entrenamiento y prueba
print("Proporcion de clases en el conjunto de entrenamiento:")
print(np.bincount(y_train))
print("\nProporcion de clases en el conjunto de prueba:")
print(np.bincount(y_test))
