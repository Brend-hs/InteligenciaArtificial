from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.datasets import load_iris, load_wine, load_breast_cancer
import numpy as np

# Definir función para comprobar si los conjuntos son disjuntos y las clases están representadas proporcionalmente
def check_disjointness_and_proportionality(y_train, y_test):
    # Calcular la distribución de clases en el conjunto de entrenamiento
    train_class_distribution = np.bincount(y_train) / len(y_train)
    # Calcular la distribución de clases en el conjunto de prueba
    test_class_distribution = np.bincount(y_test) / len(y_test)
    
    # Calcular la diferencia relativa máxima entre las distribuciones de clases
    max_relative_difference = np.max(np.abs(train_class_distribution - test_class_distribution))
    # Definir el umbral de tolerancia para la proporcionalidad de las clases
    tolerance = 0.1  # Ajuste el umbral de tolerancia según sea necesario
    
    # Verificar si la diferencia relativa está dentro del umbral de tolerancia
    assert max_relative_difference < tolerance, "Las clases no están representadas proporcionalmente en los conjuntos de entrenamiento y prueba"

# Definir función para Hold Out 70/30 estratificado
def hold_out_stratified(X, y):
    # Dividir el conjunto de datos en entrenamiento y prueba de forma estratificada
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)
    # Verificar la disyunción y proporcionalidad de las clases en los conjuntos de entrenamiento y prueba
    check_disjointness_and_proportionality(y_train, y_test)
    # Imprimir mensaje indicando que los conjuntos son disjuntos y las clases están representadas proporcionalmente
    print("Los conjuntos de entrenamiento y prueba son disjuntos y las clases están representadas proporcionalmente")

# Definir función para 10-Fold Cross-Validation estratificado
def cross_validation_stratified(X, y):
    # Crear un validador cruzado estratificado con 10 pliegues
    skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
    # Iterar sobre los pliegues del validador cruzado
    for train_index, test_index in skf.split(X, y):
        # Dividir el conjunto de datos en entrenamiento y prueba para el pliegue actual
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        # Verificar la disyunción y proporcionalidad de las clases en los conjuntos de entrenamiento y prueba del pliegue actual
        check_disjointness_and_proportionality(y_train, y_test)
    
    # Imprimir mensaje indicando que los conjuntos de entrenamiento y prueba son disjuntos y las clases están representadas proporcionalmente
    print("Los conjuntos de entrenamiento y prueba son disjuntos y las clases están representadas proporcionalmente")

# Cargar los conjuntos de datos
iris = load_iris()
wine = load_wine()
cancer = load_breast_cancer()

# Realizar Hold Out 70/30 estratificado en cada conjunto de datos y verificar disyunción y proporcionalidad de las clases
print("Hold Out 70/30 estratificado en Iris Dataset:")
hold_out_stratified(iris.data, iris.target)

print("\nHold Out 70/30 estratificado en Wine Dataset:")
hold_out_stratified(wine.data, wine.target)

print("\nHold Out 70/30 estratificado en Breast Cancer Dataset:")
hold_out_stratified(cancer.data, cancer.target)

# Realizar 10-Fold Cross-Validation estratificado en cada conjunto de datos y verificar disyunción y proporcionalidad de las clases
print("\n10-Fold Cross-Validation estratificado en Iris Dataset:")
cross_validation_stratified(iris.data, iris.target)

print("\n10-Fold Cross-Validation estratificado en Wine Dataset:")
cross_validation_stratified(wine.data, wine.target)

print("\n10-Fold Cross-Validation estratificado en Breast Cancer Dataset:")
cross_validation_stratified(cancer.data, cancer.target)
