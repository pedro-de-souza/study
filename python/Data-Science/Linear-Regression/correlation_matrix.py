import pandas as pd

from sklearn.datasets import load_boston
boston_dataset = load_boston()
## build a DataFrame
boston = pd.DataFrame(boston_dataset.data,
                      columns=boston_dataset.feature_names)
boston['MEDV'] = boston_dataset.target

corr_matrix = boston.corr().round(2)
print(corr_matrix)
# Para entender a relação entre os recursos (colunas), uma matriz de correlação é muito útil na análise exploratória dos dados.
# A correlação mede relações lineares entre variáveis.
# Podemos construir uma matriz de correlação para mostrar coeficientes de correlação entre variáveis.