import pandas as pd

from sklearn.datasets import load_boston
boston_dataset = load_boston()
## build a DataFrame
boston = pd.DataFrame(boston_dataset.data,
                      columns=boston_dataset.feature_names)
boston['MEDV'] = boston_dataset.target

print(boston[['CHAS', 'RM', 'AGE', 'RAD', 'MEDV']].head())
# É útil para testar rapidamente se o DataFrame possui o tipo certo de dados. Para ver as primeiras linhas de um DataFrame, use .head (n)