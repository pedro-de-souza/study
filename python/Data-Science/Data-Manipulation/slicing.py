# E se quisermos inspecionar os três primeiros elementos da primeira linha em um 2darray? Usamos ":"
# para selecionar todos os elementos do índice até, mas não incluindo, o índice final. Isso é chamado de corte .

import numpy as np

heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180,
           168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185,
           191]

ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56,
        55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]

heights_and_ages = heights + ages

heights_and_ages_arr = np.array(heights_and_ages)
heights_and_ages_arr = heights_and_ages_arr.reshape((2, 45))
print(heights_and_ages_arr[0, 0:3])
print(heights_and_ages_arr[:3])
print(heights_and_ages_arr[1:3])

# Às vezes, você precisa alterar os valores de elementos específicos na matriz.
# Por exemplo, percebemos que a quarta entrada no heights_arr estava incorreta;
# ela deveria ser 165 em vez de 163; podemos atribuir novamente o número correto

print(heights_and_ages_arr[1:3])
heights_and_ages_arr[1:3] = 165
print(heights_and_ages_arr[1:3])

print(heights_and_ages_arr[0,:])
heights_and_ages_arr[0,:] = 180
print(heights_and_ages_arr[0,:])

print(heights_and_ages_arr[:2,: 2])
heights_and_ages_arr[:2,: 2] = 0
print(heights_and_ages_arr[:2,: 2])

# Atribuindo uma matriz a uma matriz
new_record = np.array([[180, 183, 190], [54, 50, 69]])
heights_and_ages_arr[:, 42:] = new_record

# Combinando duas matrizes
# Muitas vezes, obtemos dados armazenados em diferentes matrizes e precisamos combiná-los em um para mantê-los em um só lugar.
# Por exemplo, em vez de ter as idades armazenadas em uma lista, ela pode ser armazenada em um 2darray:
# Se remodelarmos o heights_arr para (45,1), o mesmo que 'ages_arr', podemos empilhá-los horizontalmente
# (por coluna) para obter um 2darray usando ' hstack ':
heights_arr = np.array(heights)
ages_arr = np.array(ages)

heights_arr = heights_arr.reshape((1,45))
ages_arr = ages_arr.reshape((1,45))

height_age_arr = np.vstack((heights_arr, ages_arr))
print(height_age_arr.shape)
print(height_age_arr[:,:3])

# Concatenar
# De maneira mais geral, podemos usar a função numpy.concatenate. Se quisermos concatenar,
# vincule duas matrizes ao longo das linhas e passe 'axis = 1' para obter o
# mesmo resultado que usar numpy.hstack; e passe 'axis = 0' se desejar combinar matrizes verticalmente.

height_age_arr = np.concatenate((heights_arr, ages_arr), axis=1)
print(height_age_arr.shape)
print(height_age_arr[:3,:])