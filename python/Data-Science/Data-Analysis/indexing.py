import pandas as pd

presidents_df = pd.read_csv('https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
print('-----Linhas com .loc')
# Em vez de memorizar as posições inteiras para localizar as
# informações de ordem, idade, altura e festa de Abraham Lincoln, com o DataFrame, podemos acessá-lo pelo nome usando .loc :
print(presidents_df.loc['Abraham Lincoln'])
print(type(presidents_df.loc['Abraham Lincoln']))
print(presidents_df.loc['Abraham Lincoln'].shape)
print(presidents_df.iloc[15:18])

print('-----More with .loc')
# Se quisermos acessar a ordem, a idade e a altura das colunas, podemos fazê-lo com .loc .
# .loc nos permite acessar qualquer uma das colunas.
# Por exemplo, se quisermos acessar colunas da ordem à altura dos três primeiros presidentes:
print(presidents_df.loc[:, 'order':'height'].head(n=3))

print('------Colunas')
# Podemos recuperar uma coluna inteira de presidents_df por nome. Primeiro, acessamos todos os nomes de colunas:
print(presidents_df.columns)
# O que retorna um objeto de índice que contém todos os nomes de colunas. Em seguida, podemos acessar a altura da coluna:
print(presidents_df['height'])
print(presidents_df['height'].shape)
# Para selecionar várias colunas, passamos os nomes em uma lista, resultando em um DataFrame.
# Lembre-se, podemos usar .head () para acessar as 3 primeiras linhas, como mostrado abaixo:
print(presidents_df[['height', 'age']].head(n=3))