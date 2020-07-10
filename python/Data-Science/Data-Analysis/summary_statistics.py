import pandas as pd

presidents_df = pd.read_csv('https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
# Não é prático imprimir um conjunto de dados inteiro com um tamanho de amostra grande.
# Em vez disso, queremos resumir e caracterizar dados de amostra usando apenas alguns valores.
# As estatísticas resumidas incluem medidas de localização e medidas de propagação .
# Medidas de localização são quantidades que representam o valor médio de uma variável,
# enquanto medidas de dispersão representam quão semelhantes ou diferentes são os valores de uma variável.
#
# Medidas de localização - medidas mínimas , máximas e médias
print('Min / Max / Mean')

print('--------Mínimo')
print(presidents_df.min())
print('--------Máximo')
print(presidents_df.max())
print('--------Médias')
print(presidents_df.mean())

# Quantiles são pontos de corte que dividem o intervalo dos dados em intervalos contínuos com um número igual de observações.
# A mediana é o único ponto de corte nos 2-quantis, de modo que 50% dos dados estão abaixo da mediana e a outra metade acima dela.
#

print('-------Quantil')
print(presidents_df['age'].quantile([0.25, 0.5, 0.75, 1]))

print('-------Mediana')
print(presidents_df['age'].median())

# Em probabilidade e estatística, variância é o desvio médio
# quadrático de cada ponto de dados da média de todo o conjunto de dados.
# Você pode pensar nisso como a distância entre um conjunto de números e seu valor médio.
# O desvio padrão (std) é a raiz quadrada da variação.
# Um std alto implica uma propagação grande e um std baixo indica
# uma propagação pequena, ou a maioria dos pontos está próxima da média.
print('Variação e desvio padrão')

# Em um exemplo extremo, os dados consistem em todas as constantes 2, não há variação, portanto a variação é 0,0, assim como seu padrão:
print('--------------------')
const = pd.Series([2, 2, 2])
print(const.var())
print(const.std())

# A média de [2,3,4] é (2 + 3 + 4) / 3 = 3,0 e sua variação é (2-3) ^ 2 + (3-3) ^ 2 + (4-3) ^ 2 = 1 + 0 + 1 = 2.
# Observe que, em Python, .var () retornará a variação dividida por N-1 onde N é o comprimento dos dados, a saída será 2 / (3-1) = 1.
print('--------------------')
dat = pd.Series([2, 3, 4])

print(dat.mean())
print(dat.var())
# E o std é apenas a raiz quadrada da variação:
print(dat.std())

print('--------------------')
print(presidents_df['age'].var())
print(presidents_df['age'].std())

print('------Describe')
#  imprime quase todas as estatísticas de resumo mencionadas anteriormente, exceto a variação.
#  Além disso, conta todos os valores não nulos de cada coluna.
print(presidents_df['age'].describe())
print(presidents_df.describe())

print('-------Categorical Variable')
# A quarta coluna 'parte' foi omitida na saída de .describe () porque é uma variável categórica .
# Uma variável categórica é aquela que assume um único valor de um conjunto limitado de categorias.
# Não faz sentido calcular a média de partidos democráticos, republicanos, federalistas e outros.
print(presidents_df['party'].value_counts())
print(presidents_df['party'].describe())