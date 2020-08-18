import pandas as pd
urlFilmes = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula4.1/movies.csv"
urlNotas = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula1.2/ratings.csv"
filmes = pd.read_csv(urlFilmes)
notas = pd.read_csv(urlNotas)


filmes.columns = ["filmeID","titulo","generos"]
notas.columns =["usuarioID","filmeID","nota","momento"]

print(notas['nota'].unique())
