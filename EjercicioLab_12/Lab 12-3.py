#RAMIREZ VAZQUEZ
#CADENAS ACEVEDO
#GOMEZ JASSO
#HERNANDEZ SAUCEDO
#RODRIGUEZ ESCOGIDO

import pandas as pd
from sklearn.datasets import load_iris
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import BayesianEstimator
from pgmpy.inference import VariableElimination

# Cargar el conjunto de datos de iris desde scikit-learn
iris = load_iris()
data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
data['species'] = iris.target

# Definir la estructura de la red bayesiana
model = BayesianNetwork([('sepal length (cm)', 'species'),
                         ('sepal width (cm)', 'species'),
                         ('petal length (cm)', 'species'),
                         ('petal width (cm)', 'species')])

# Aprender las distribuciones de probabilidad condicional a partir de los datos de entrenamiento
model.fit(data, estimator=BayesianEstimator)

# Hacer inferencias sobre la red
inference = VariableElimination(model)

# Imprimir la probabilidad de cada especie dada ciertas características
print("Probabilidad de especie dado longitud y ancho del sépalo y del pétalo:")
print(inference.query(variables=['species'], evidence={'sepal length (cm)': 4.4, 'sepal width (cm)': 2.0, 'petal length (cm)': 1.2, 'petal width (cm)': 0.4}))