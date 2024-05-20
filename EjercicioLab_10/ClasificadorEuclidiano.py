import numpy as np
import pandas as pd
from sklearn.datasets import load_iris, load_breast_cancer
from sklearn.model_selection import train_test_split, KFold
from sklearn.metrics import accuracy_score
from scipy.spatial import distance

# Cargar datos Iris
iris = load_iris()
X_iris = iris.data
y_iris = iris.target

# Cargar datos Breast Cancer
breast_cancer = load_breast_cancer()
X_bc = breast_cancer.data
y_bc = breast_cancer.target

# Definición del Clasificador Euclidiano
class EuclideanClassifier:
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test):
        y_pred = []
        for x in X_test:
            distances = np.array([distance.euclidean(x, x_train) for x_train in self.X_train])
            nearest_index = np.argmin(distances)
            y_pred.append(self.y_train[nearest_index])
        return np.array(y_pred)

# Validación Hold-Out 70/30
def hold_out_validation(X, y, test_size=0.3):
    # División de los datos
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    # Creación y ajuste del modelo
    model = EuclideanClassifier()
    model.fit(X_train, y_train)
    # Predicción
    y_pred = model.predict(X_test)
    # Evaluación
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy

# Validación Hold-Out para Iris
accuracy_iris_hold_out = hold_out_validation(X_iris, y_iris)
print(f'Iris Hold-Out 70/30 Accuracy: {accuracy_iris_hold_out:.2f}')

# Validación Hold-Out para Breast Cancer
accuracy_bc_hold_out = hold_out_validation(X_bc, y_bc)
print(f'Breast Cancer Hold-Out 70/30 Accuracy: {accuracy_bc_hold_out:.2f}')

# Validación 10-Fold Cross-Validation
def cross_validation(X, y, n_splits=10):
    # Configuración del K-Fold Cross-Validation
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)
    accuracies = []
    # Iteración sobre cada fold
    for train_index, test_index in kf.split(X):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        # Creación y ajuste del modelo en cada fold
        model = EuclideanClassifier()
        model.fit(X_train, y_train)
        # Predicción y evaluación en cada fold
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        accuracies.append(accuracy)
    # Cálculo de la precisión promedio    
    return np.mean(accuracies)

# Cross-Validation para Iris
accuracy_iris_cv = cross_validation(X_iris, y_iris)
print(f'Iris 10-Fold Cross-Validation Accuracy: {accuracy_iris_cv:.2f}')

# Cross-Validation para Breast Cancer
accuracy_bc_cv = cross_validation(X_bc, y_bc)
print(f'Breast Cancer 10-Fold Cross-Validation Accuracy: {accuracy_bc_cv:.2f}')
