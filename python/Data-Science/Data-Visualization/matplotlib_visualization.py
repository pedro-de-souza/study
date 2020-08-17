#"Uma imagem vale mais que mil palavras." soa verdadeiro na ciência de dados.
# A visualização de dados pode revelar padrões que não são óbvios e comunicar os insights de maneira mais eficaz.
# Nesta parte, examinaremos a biblioteca Matplotlib , uma das ferramentas de visualização de dados mais populares,
# operando em matrizes numpy, bem como pandas Series e DataFrames. Por convenção, importamos a biblioteca com um nome mais curto:

import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes()
plt.show()

# Para todos os gráficos matplotlib, primeiro crie uma figura e um objeto de eixos; para mostrar a plotagem, chame “plt.show ()”.
# A figura contém todos os objetos, incluindo eixos, gráficos, textos e etiquetas.