# RAMIREZ VAZQUEZ
# CADENAS ACEVEDO
# GOMEZ JASSO
# HERNANDEZ SAUCEDO
# RODRIGUEZ ESCOGIDO

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris, load_wine, load_breast_cancer
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix

# Cargamos los conjuntos de datos y los organizamos en un nuevo dataset para trabajar en ellos
iris = load_iris()
wine = load_wine()
breast_cancer = load_breast_cancer()

datasets = {
    "Iris": (iris.data, iris.target),
    "Wine": (wine.data, wine.target),
    "Breast Cancer": (breast_cancer.data, breast_cancer.target)
}

results={}

for name, (X, y) in datasets.items():
    print(f"Dataset a evaluar: {name}")

    # Hold-Out 70/30
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Naive Bayes
    nb = GaussianNB()
    nb.fit(X_train, y_train)
    y_pred = nb.predict(X_test)
    accuracy_nb_holdout = accuracy_score(y_test, y_pred)
    cm_nb_holdout = confusion_matrix(y_test, y_pred)

    # 10-Fold Cross Validation
    kf = KFold(n_splits=10, shuffle=True, random_state=42)
    accuracy_nb_cv = cross_val_score(nb, X, y, cv=kf, scoring='accuracy').mean()

    # Resultados
    results[name] = {
        "Naive Bayes": {
            "Puntuacion Hold-Out": accuracy_nb_holdout,
            "Matriz de Confusion Hold-Out ": cm_nb_holdout,
            "Puntuacion 10-Fold CV": accuracy_nb_cv
        }
    }

print(results)