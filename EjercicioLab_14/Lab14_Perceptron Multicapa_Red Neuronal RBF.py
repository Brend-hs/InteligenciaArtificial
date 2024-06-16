# Importar las bibliotecas necesarias
import numpy as np
from sklearn.datasets import load_iris, load_wine, load_breast_cancer
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.neural_network import MLPClassifier
from sklearn.kernel_approximation import RBFSampler
from sklearn.linear_model import LogisticRegression

# Cargar los conjuntos de datos
datasets = {
    "Iris": load_iris(),  # Cargar el conjunto de datos Iris
    "Wine": load_wine(),  # Cargar el conjunto de datos Wine
    "Breast Cancer": load_breast_cancer()  # Cargar el conjunto de datos Breast Cancer
}

# Diccionario para almacenar los resultados de las evaluaciones
results = {}

# Definir una función para aplicar los modelos y validación
def evaluate_model(X, y, model, model_name, dataset_name):
    # División de datos Hold-Out 70/30
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    model.fit(X_train, y_train)  # Entrenar el modelo con los datos de entrenamiento
    y_pred = model.predict(X_test)  # Predecir las etiquetas para los datos de prueba
    accuracy_holdout = accuracy_score(y_test, y_pred)  # Calcular la precisión del modelo
    confusion_holdout = confusion_matrix(y_test, y_pred)  # Calcular la matriz de confusión
    
    # Validación cruzada de 10 pliegues
    kf = KFold(n_splits=10, random_state=42, shuffle=True)  # Definir el KFold con 10 pliegues
    cv_scores = cross_val_score(model, X, y, cv=kf)  # Evaluar el modelo utilizando validación cruzada
    accuracy_cv = np.mean(cv_scores)  # Calcular la precisión promedio de la validación cruzada
    
    # Guardar los resultados
    results[(dataset_name, model_name, "Hold-Out")] = (accuracy_holdout, confusion_holdout)
    results[(dataset_name, model_name, "10-Fold CV")] = (accuracy_cv, None)
    
# Evaluar los modelos en cada conjunto de datos
for dataset_name, dataset in datasets.items():
    X, y = dataset.data, dataset.target  # Separar las características y las etiquetas del conjunto de datos
    scaler = StandardScaler()  # Crear un escalador estándar
    X = scaler.fit_transform(X)  # Ajustar y transformar las características para que tengan media 0 y varianza 1
    
    # Evaluar el Perceptrón Multicapa
    mlp = MLPClassifier(random_state=42, max_iter=1000, learning_rate_init=0.001, tol=1e-4)  # Definir el modelo MLP
    evaluate_model(X, y, mlp, "MLP", dataset_name)  # Evaluar el modelo MLP
    
    # Evaluar la Red Neuronal RBF
    rbf_feature = RBFSampler(gamma=1, random_state=42)  # Crear un aproximador de funciones base radial
    X_features = rbf_feature.fit_transform(X)  # Transformar las características utilizando RBF
    rbf_model = LogisticRegression(random_state=42)  # Definir el modelo de regresión logística
    evaluate_model(X_features, y, rbf_model, "RBF", dataset_name)  # Evaluar el modelo RBF

# Mostrar los resultados de las evaluaciones
for key, value in results.items():
    dataset_name, model_name, validation_method = key # Obtener los nombres de los conjuntos de datos y modelos
    accuracy, confusion = value # Obtener la precisión y la matriz de confusión
    print(f"Dataset: {dataset_name}, Model: {model_name}, Validation: {validation_method}") # Mostrar los resultados
    print(f"Accuracy: {accuracy}") # Mostrar la precisión
    if confusion is not None: # Mostrar la matriz de confusión si está disponible
        print(f"Confusion Matrix:\n{confusion}")
    print()

# Encontrar los mejores resultados por conjunto de datos y método de validación
best_results = {} # Diccionario para almacenar los mejores resultados
# Iterar sobre los resultados
for (dataset_name, model_name, validation_method), (accuracy, _) in results.items():
    # Verificar si el conjunto de datos y el método de validación no están en el diccionario
    if (dataset_name, validation_method) not in best_results:
        # Guardar la precisión y el nombre del modelo
        best_results[(dataset_name, validation_method)] = (accuracy, model_name) 
    else: 
        # Verificar si la precisión es mayor que la mejor precisión
        if accuracy > best_results[(dataset_name, validation_method)][0]:
            # Guardar la precisión y el nombre del modelo
            best_results[(dataset_name, validation_method)] = (accuracy, model_name)

# Mostrar los mejores resultados
for key, value in best_results.items(): 
    dataset_name, validation_method = key # Obtener los nombres de los conjuntos de datos y métodos de validación
    accuracy, model_name = value # Obtener la precisión y el nombre del modelo
    print(f"Best Result for {dataset_name} with {validation_method}:") 
    print(f"Model: {model_name}, Accuracy: {accuracy}\n")
    