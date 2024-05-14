from sklearn.datasets import * #Carga el conjunto de datos de Wine
from sklearn.model_selection import train_test_split
import numpy as np


# Conjunto de datos Wine
wine = load_wine()
X = wine.data
y = wine.target

# Realiza lo mismo que Iris, solamente que esta vez con Wine
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y)

# Realiza lo mismo que Iris, solamente que esta vez con Wine
print("Proporcion de clases en el conjunto de entrenamiento:")
print(np.bincount(y_train))
print("\nProporcion de clases en el conjunto de prueba:")
print(np.bincount(y_test))
