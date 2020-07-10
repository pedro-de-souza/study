# Podemos usar a indexação de matriz para selecionar elementos individuais de matrizes. Como nas listas Python, o índice numpy começa em 0.
# Para acessar a altura do 3º presidente Thomas Jefferson no array de 1 dia 'heights_arr':

import numpy as np

heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180,
           168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185,
           191]
ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56,
        55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]

heights_arr = np.array(heights)
heights_and_ages = heights + ages
heights_and_ages_arr = np.array(heights_and_ages)
heights_and_ages_arr = heights_and_ages_arr.reshape((2, 45))

print(heights_arr[2])

# Em uma matriz 2, existem dois eixos, eixo 0 e 1. O eixo 0 corre para baixo nas linhas, enquanto o eixo 1 corre horizontalmente pelas colunas.
# No 2darrary heights_and_ages_arr, lembre-se de que suas dimensões são (2, 45).
# Para encontrar a idade de Thomas Jefferson no início de sua presidência,
# você precisaria acessar a segunda linha em que as idades são armazenadas:
print(heights_and_ages_arr[1, 2])
