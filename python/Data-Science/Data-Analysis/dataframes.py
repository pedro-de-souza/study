import pandas as pd

wine_dict = {
    'red_wine': [3, 6, 5],
    'white_wine':[5, 0, 10]
}
sales = pd.DataFrame(wine_dict, index=["adam", "bob", "charles"])
print(sales)

# Inspecionar um DataFrame
print('\nInspecionar um DataFrame')
presidents_df = pd.read_csv('https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')

print('-----Shape and Size')
# Semelhante a numpy, para obter as dimensões de um DataFrame, use .shape .
print(presidents_df.shape)
# Existem 45 linhas e 4 colunas neste DataFrame. Para obter o número de linhas, podemos acessar o primeiro elemento da tupla.
print(presidents_df.shape[0])
# Tamanho também funciona no DataFrame para retornar um número inteiro que representa o número de elementos nesse objeto.
print(presidents_df.size)

print('-----Head and Tail')
# Para ver as primeiras linhas em um DataFrame, use .head () ;
# se não especificarmos n (o número de linhas), por padrão, ele exibirá as cinco primeiras linhas. Aqui queremos ver as 3 principais linhas.
print(presidents_df.head(n=3))
# Em presidents_df, o índice é o nome do presidente, há quatro colunas: ordem, idade, altura e partido.
# Da mesma forma, se queremos ver as últimas linhas, podemos usar .tail () , o padrão também é cinco linhas.
print(presidents_df.tail())

print('----Informações')
# Use .info () para obter uma visão geral do DataFrame.
# Sua saída inclui índice, nomes de colunas, contagem de valores não nulos, tipos e uso de memória.
presidents_df.info()