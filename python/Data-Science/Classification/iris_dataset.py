# O conjunto de dados é armazenado em um arquivo csv, podemos carregá-lo como um DataFrame usando read_csv () nas pandas da biblioteca:
import pandas as pd
iris = pd.read_csv('https://sololearn.com/uploads/files/iris.csv')

print(iris.shape)

user = pd.read_csv('./data/user.csv')
user.drop('Email', axis=1, inplace=True)
print(user.head())