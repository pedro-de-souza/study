#O conjunto de dados de moradias de Boston é o nosso conjunto de dados de amostra que fornece valores
# médios de residências em diferentes áreas ao redor de Boston.
# Para manipulações mais fáceis posteriormente, criamos um DataFrame do pandas 
# a partir dos ndarrays numpy armazenados em boston_dataset.data da seguinte maneira:
import pandas as pd

from sklearn.datasets import load_boston
boston_dataset = load_boston()
## build a DataFrame
boston = pd.DataFrame(boston_dataset.data,
                      columns=boston_dataset.feature_names)
boston['MEDV'] = boston_dataset.target

print(boston.columns)