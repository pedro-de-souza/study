import pandas as pd
iris = pd.read_csv('https://sololearn.com/uploads/files/iris.csv')

# O conjunto de dados contém 3 classes de 50 instâncias cada. Podemos verificar isso por:
print(iris.groupby('species').size())

# Ou simplesmente use value_counts ():
print(iris['species'].value_counts())

# O método value_counts () é um ótimo utilitário para entender rapidamente a distribuição dos dados.
# Quando usado nos dados categóricos, conta o número de valores exclusivos na coluna de interesse.

# Iris é um conjunto de dados balanceado, pois os pontos de dados de cada classe são distribuídos igualmente.