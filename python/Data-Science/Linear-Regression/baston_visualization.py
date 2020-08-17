import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
boston_dataset = load_boston()
## build a DataFrame
boston = pd.DataFrame(boston_dataset.data,columns=boston_dataset.feature_names)
boston.hist(column='CHAS')
plt.show()

# As estatísticas de resumo fornecem uma idéia geral de cada recurso e do destino,
# mas a visualização revela as informações mais claramente.