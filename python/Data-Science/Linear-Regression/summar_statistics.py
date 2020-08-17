# Lembre-se de que não é prático imprimir um conjunto de dados inteiro com um tamanho de amostra grande.
# Em vez disso, queremos resumir e caracterizar
# dados de amostra usando apenas alguns valores. Para verificar as estatísticas resumidas do conjunto de dados
import pandas as pd

from sklearn.datasets import load_boston
boston_dataset = load_boston()
## build a DataFrame
boston = pd.DataFrame(boston_dataset.data,columns=boston_dataset.feature_names)
boston['MEDV'] = boston_dataset.target

print(boston.describe().round(2))