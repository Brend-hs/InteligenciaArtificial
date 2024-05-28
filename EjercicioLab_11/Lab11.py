#RAMIREZ VAZQUEZ
#CADENAS ACEVEDO
#GOMEZ JASSO
#HERNANDEZ SAUCEDO
#RODRIGUEZ ESCOGIDO

from sklearn.datasets import load_iris, load_wine, load_breast_cancer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

def evaluate_classifier(dataset, dataset_name):
    print("\n-------------------------------------------Evaluación del conjunto de datos", dataset_name)
    # Dividir el conjunto de datos en entrenamiento y prueba (70% entrenamiento, 30% prueba)
    X_train, X_test, y_train, y_test = train_test_split(dataset.data, dataset.target, test_size=0.3, random_state=42)

    # Entrenar el clasificador 1-NN
    knn_1 = KNeighborsClassifier(n_neighbors=1)
    knn_1.fit(X_train, y_train)
    y_pred_1 = knn_1.predict(X_test)
    accuracy_1 = accuracy_score(y_test, y_pred_1)
    confusion_matrix_1 = confusion_matrix(y_test, y_pred_1)

    print("Exactitud del clasificador 1-NN:", accuracy_1)
    print("Matriz de confusión del clasificador 1-NN:")
    print(confusion_matrix_1)

    # Entrenar el clasificador K-NN con diferentes valores de K y encontrar el mejor
    best_accuracy = 0
    best_k = 1
    for k in range(1, 11):
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train, y_train)
        y_pred = knn.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_k = k

    print("\nEl mejor valor de K encontrado:", best_k)
    print("Exactitud correspondiente:", best_accuracy)

    # Entrenar el clasificador K-NN con el mejor valor de K encontrado
    knn_best = KNeighborsClassifier(n_neighbors=best_k)
    knn_best.fit(X_train, y_train)
    y_pred_best = knn_best.predict(X_test)
    accuracy_best = accuracy_score(y_test, y_pred_best)
    confusion_matrix_best = confusion_matrix(y_test, y_pred_best)

    print("\nExactitud del clasificador K-NN con el mejor valor de K:", accuracy_best)
    print("Matriz de confusión del clasificador K-NN con el mejor valor de K:")
    print(confusion_matrix_best)

    # Realizar validación cruzada de 10-Fold
    knn_best_cv = KNeighborsClassifier(n_neighbors=best_k)
    cv_scores = cross_val_score(knn_best_cv, dataset.data, dataset.target, cv=10)

    print("\nPuntuaciones de validación cruzada:")
    print(cv_scores)
    print("Exactitud promedio:", cv_scores.mean())

# Cargar el conjunto de datos Iris
iris = load_iris()
evaluate_classifier(iris, "Iris")

# Cargar el conjunto de datos Wine
wine = load_wine()
evaluate_classifier(wine, "Wine")

# Cargar el conjunto de datos Breast Cancer Wisconsin
breast_cancer = load_breast_cancer()
evaluate_classifier(breast_cancer, "Breast Cancer Wisconsin")
