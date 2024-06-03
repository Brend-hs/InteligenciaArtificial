import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_predict, cross_val_score
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import OneHotEncoder
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import BayesianEstimator

# Cargar el conjunto de datos de iris desde scikit-learn
iris = load_iris()
data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
data['species'] = iris.target

# Codificar las etiquetas de las clases usando One-Hot Encoding
encoder = OneHotEncoder(sparse_output= False)
encoded_species = encoder.fit_transform(data[['species']])
data = pd.concat([data.drop(columns=['species']), pd.DataFrame(encoded_species, columns=[f'species_{i}' for i in range(encoded_species.shape[1])])], axis=1)

# Definir la estructura de la red bayesiana
model = BayesianNetwork([('sepal length (cm)', 'species_0'),
                         ('sepal width (cm)', 'species_0'),
                         ('petal length (cm)', 'species_0'),
                         ('petal width (cm)', 'species_0')])

# Aprender las distribuciones de probabilidad condicional a partir de los datos utilizando el estimador de BayesianEstimator
model.fit(data, estimator=BayesianEstimator)

# Dividir el conjunto de datos en entrenamiento y prueba (Hold-Out 70/30)
X_train, X_test, y_train, y_test = train_test_split(data.drop(columns=['species_0', 'species_1', 'species_2']), data[['species_0', 'species_1', 'species_2']], test_size=0.3, random_state=42)

# Entrenar el modelo con el conjunto de entrenamiento
model.fit(X_train, estimator=BayesianEstimator)

# Hacer predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# Calcular el accuracy
accuracy = accuracy_score(y_test.values.argmax(axis=1), y_pred.values.argmax(axis=1))
print(f"Accuracy (Hold-Out 70/30): {accuracy}")

# Calcular la matriz de confusión
conf_matrix = confusion_matrix(y_test.values.argmax(axis=1), y_pred.values.argmax(axis=1))
print("Matriz de confusión (Hold-Out 70/30):\n", conf_matrix)

# Realizar 10-Fold Cross Validation
y_pred_cv = cross_val_predict(model, data.drop(columns=['species_0', 'species_1', 'species_2']), data[['species_0', 'species_1', 'species_2']], cv=10)

# Calcular el accuracy promedio de 10-Fold Cross Validation
accuracy_cv = accuracy_score(data[['species_0', 'species_1', 'species_2']].values.argmax(axis=1), y_pred_cv.values.argmax(axis=1))
print(f"Accuracy (10-Fold Cross Validation): {accuracy_cv}")

# Calcular la matriz de confusión de 10-Fold Cross Validation
conf_matrix_cv = confusion_matrix(data[['species_0', 'species_1', 'species_2']].values.argmax(axis=1), y_pred_cv.values.argmax(axis=1))
print("Matriz de confusión (10-Fold Cross Validation):\n", conf_matrix_cv)

