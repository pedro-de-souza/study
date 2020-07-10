import pandas as pd
import numpy as np
presidents_df = pd.read_csv('https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')

# Para encontrar o valor com base em uma condição, podemos usar a operação groupby .
# Pense em grupo executando três etapas: dividir, aplicar e combinar.
# A etapa de divisão divide o DataFrame em vários DataFrames com base no valor da chave especificada;
# a etapa de aplicação é executar a operação dentro de cada DataFrame menor; a última etapa combina as peças novamente no DataFrame maior.
print(presidents_df.groupby('party'))

# O .groupby ("party") retorna um objeto DataFrameGroupBy, não um conjunto de DataFrames.
# Para produzir um resultado, aplique um agregado (.mean ()) a este objeto DataFrameGroupBy:
print(presidents_df.groupby('party').mean())

print('-----Agregação')
# Também podemos executar várias operações no objeto groupby usando o método .agg () .
# É preciso uma string, uma função ou uma lista dos mesmos.
# Por exemplo, gostaríamos de obter os valores mínimo, mediano e máximo das alturas agrupadas por parte:
print(presidents_df.groupby('party')['height'].agg(['min', np.median, max]))