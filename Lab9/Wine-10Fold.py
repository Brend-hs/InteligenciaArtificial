from sklearn.datasets import *
from sklearn.model_selection import StratifiedKFold
import numpy as np

# Conjunto de datos Wine
wine = load_wine()
X = wine.data
y = wine.target

# Objeto StratifiedKFold con 10 folds
skf = StratifiedKFold(n_splits=10)

# Se itera  sobre los folds y se realiza la validacion cruzada
for train_index, test_index in skf.split(X, y):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

    # Proporcion de clases en los conjuntos de entrenamiento y prueba para cada fold
    print("Fold:")
    print("Proporcion de clases en el conjunto de entrenamiento:")
    print(np.bincount(y_train))
    print("Proporcion de clases en el conjunto de prueba:")
    print(np.bincount(y_test))
