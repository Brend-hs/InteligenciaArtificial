from sklearn.datasets import * #Carga el conjunto de datos de BreastCancer
from sklearn.model_selection import train_test_split
import numpy as np


# Conjunto de datos Breast Cancer Wisconsin
breast_cancer = load_breast_cancer()
X = breast_cancer.data
y = breast_cancer.target

# Realiza lo mismo que Iris, solamente que esta vez con Breast Cancer 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y)

# Realiza lo mismo que Iris, solamente que esta vez con Breast Cancer 
print("Proporcion de clases en el conjunto de entrenamiento:")
print(np.bincount(y_train))
print("\nProporcion de clases en el conjunto de prueba:")
print(np.bincount(y_test))
